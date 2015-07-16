import werkzeug
from openerp.addons.web import http
from openerp.addons.web.http import request
import pprint
import base64

class snippet_latest_posts_controller(http.Controller):
    @http.route(['/snippet_latest_posts/render/<base>/<int:page>'], type='http', auth='public', website=True)
    def render_latest_posts(self, page, base, template='snippet_last_articles.liste_article', **post):
        cr, uid, context = request.cr, request.uid, request.context
        page_obj = request.registry['ir.ui.view']
        
        if base == 'ir.ui.view': 
            page_ids = page_obj.search(cr, uid, [('page','=','True'),('id','<',page),('active','=','True')], limit=3, order='create_date desc', context=context)
        else : 
            page_ids = page_obj.search(cr, uid, [('page','=','True'),('active','=','True')], limit=3, order='create_date desc', context=context)
        
        posts = page_obj.browse(cr, uid, page_ids, context=context)

        return request.render("last_articles_block.liste_last", {'posts': posts})
        
    @http.route(['/snippet_latest_posts/updimage/<base>/<int:page>'], type='http', auth='public', methods=['POST','GET'], website=True)
    def array_latest_image(self, base, page, **args):
        cr, uid, context, registry = request.cr, request.uid, request.context, request.registry
        page_pool = registry.get('ir.ui.view')

        page = page_pool.browse(cr, uid, page)

        page.website_meta_image = base64.encodestring(args["image"].read())
        return request.render("last_articles_block.donnee_get",{})# {'posts': post})



