# -*- coding: utf-8 -*-
##############################################################################
#
#    Website Marketplace
#    Copyright (C) 2014 Xpansa Group (<http://xpansa.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import openerp
from openerp.addons.auth_signup.controllers.main import AuthSignupHome
from openerp.addons.auth_signup.res_users import SignupError
from openerp.addons.website.models.website import slug
from openerp.addons.website_blog.controllers.main import QueryURL
from openerp.addons.web import http
from openerp.tools import DEFAULT_SERVER_DATETIME_FORMAT, DEFAULT_SERVER_DATE_FORMAT
from openerp.tools.translate import _
from openerp.http import request

from datetime import datetime
from HTMLParser import HTMLParser
import werkzeug


class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)


def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


def get_date_format(cr, uid, context):
    """ Return date format from locale of current user 
    to parse dates from forms. 
    """
    if context is None:
        context = {}
    lang = context.get('lang')
    if lang:
        res_lang = request.registry.get('res.lang')
        ids = res_lang.search(cr, uid, [('code', '=', lang)])
        if ids:
            lang_params = res_lang.read(cr, uid, ids[0], ['date_format'])
            return lang_params['date_format']
    return DEFAULT_SERVER_DATE_FORMAT


def format_date(value, with_time=False):
    """ Convert UTC date to user locale format
    """
    cr, uid, context, registry = request.cr, request.uid, \
                                 request.context, request.registry
    if context is None:
        context = {}
    user_date = datetime.strptime(
        value, with_time and
        DEFAULT_SERVER_DATETIME_FORMAT or DEFAULT_SERVER_DATE_FORMAT
    )
    if context and context.get('tz'):
        tz_name = context['tz']
    else:
        tz_name = registry.get('res.users').read(cr, uid, uid, ['tz'])['tz']
        if tz_name:
            utc = pytz.timezone('UTC')
            context_tz = pytz.timezone(tz_name)
            user_datetime = user_date + datetime.timedelta(hours=12.0)
            local_timestamp = context_tz.localize(user_datetime, is_dst=False)
            user_datetime = local_timestamp.astimezone(utc)
            return user_datetime.strftime(get_date_format(cr, uid, context))
    return user_date.strftime(get_date_format(cr, uid, context))


def format_text(text, length=300):
    """ Cut long descriptions 
    """
    if not text:
        return ''
    text = text[0:length]
    dot_pos = text.rfind('.')
    if dot_pos:
        text = text[0:dot_pos]
    else:
        text = text[0:text.rfind(' ')]
    return text + ' '*(length - len(text))


class MarketPlaceHome(AuthSignupHome):

    @http.route('/web/signup', type='http', auth='public', website=True)
    def web_auth_signup(self, *args, **kw):
        """
        Extend signup page to redirect user to step 2 of registration
        """
        qcontext = self.get_auth_signup_qcontext()
        if not qcontext.get('token') and not qcontext.get('signup_enabled'):
            raise werkzeug.exceptions.NotFound()

        if 'error' not in qcontext and request.httprequest.method == 'POST':
            try:
                self.do_signup(qcontext)
                return super(AuthSignupHome, self).\
                    web_login(redirect='/marketplace/register-part2')
            except (SignupError, AssertionError), e:
                qcontext['error'] = _(e.message)

        return request.render('auth_signup.signup', qcontext)
