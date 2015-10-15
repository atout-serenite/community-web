import werkzeug
from openerp.addons.web import http
from openerp.addons.web.http import request
from openerp.addons.web.controllers.main import *
from openerp.tools.translate import _
from openerp.addons.auth_signup.res_users import SignupError

class website_community_template_controller(Home):
    @http.route()
    def web_login(self, redirect=None, **kw):    
        ensure_db()

        if request.httprequest.method == 'GET' and redirect and request.session.uid:
            return http.redirect_with_hash(redirect)

        if not request.uid:
            request.uid = openerp.SUPERUSER_ID

        values = request.params.copy()
        if not redirect:
            redirect = '/web?' + request.httprequest.query_string
        values['redirect'] = redirect

        try:
            values['databases'] = http.db_list()
        except openerp.exceptions.AccessDenied:
            values['databases'] = None

        if request.httprequest.method == 'POST':
            old_uid = request.uid
            uid = request.session.authenticate(request.session.db, request.params['login'], request.params['password'])
            if uid is not False:
                return http.redirect_with_hash(redirect)
            request.uid = old_uid
            values['error'] = _("Please check your email address and password")
        if request.env.ref('web.login', False):
            return request.render('web.login', values)
        else:
            # probably not an odoo compatible database
            error = 'Unable to login on database %s' % request.session.db
            return werkzeug.utils.redirect('/web/database/selector?error=%s' % error, 303)

    @http.route('/web/signup', type='http', auth='public', website=True)
    def web_auth_signup(self, *args, **kw):
        qcontext = self.get_auth_signup_qcontext()
        if not qcontext.get('token') and not qcontext.get('signup_enabled'):
            raise werkzeug.exceptions.NotFound()

        if not qcontext.get('name'):
            qcontext['name']= _('New user')

        if 'error' not in qcontext and request.httprequest.method == 'POST':
            try:
                self.do_signup(qcontext)
                return super(website_community_template_controller, self).web_login(*args, **kw)
            except (SignupError, AssertionError), e:
                qcontext['error'] = _(e.message)

        return request.render('auth_signup.signup', qcontext)

    def get_auth_signup_config(self):
        """retrieve the module config (which features are enabled) for the login page"""

        icp = request.registry.get('ir.config_parameter')
        return {
            'signup_enabled': icp.get_param(request.cr, openerp.SUPERUSER_ID, 'auth_signup.allow_uninvited') == 'True',
            'reset_password_enabled': icp.get_param(request.cr, openerp.SUPERUSER_ID, 'auth_signup.reset_password') == 'True',
        }

    def get_auth_signup_qcontext(self):
        """ Shared helper returning the rendering context for signup and reset password """
        qcontext = request.params.copy()
        qcontext.update(self.get_auth_signup_config())
        if qcontext.get('token'):
            try:
                # retrieve the user info (name, login or email) corresponding to a signup token
                res_partner = request.registry.get('res.partner')
                token_infos = res_partner.signup_retrieve_info(request.cr, openerp.SUPERUSER_ID, qcontext.get('token'))
                for k, v in token_infos.items():
                    qcontext.setdefault(k, v)
            except:
                qcontext['error'] = _("Invalid signup token")
        return qcontext

    def do_signup(self, qcontext):
        """ Shared helper that creates a res.partner out of a token """
        values = dict((key, qcontext.get(key)) for key in ('login', 'name', 'password'))
        assert any([k for k in values.values()]), "The form was not properly filled in."
        assert values.get('password') == qcontext.get('confirm_password'), "Passwords do not match; please retype them."
        values['lang'] = request.lang
        self._signup_with_values(qcontext.get('token'), values)
        request.cr.commit()

    def _signup_with_values(self, token, values):
        db, login, password = request.registry['res.users'].signup(request.cr, openerp.SUPERUSER_ID, values, token)
        request.cr.commit()     # as authenticate will use its own cursor we need to commit the current transaction
        uid = request.session.authenticate(db, login, password)
        if not uid:
            raise SignupError(_('Authentification Failed.'))

