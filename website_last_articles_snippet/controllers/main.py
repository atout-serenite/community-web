import werkzeug
from openerp.addons.web import http
from openerp.addons.web.http import request
import pprint


class snippet_latest_posts_controller(http.Controller):


    #
    # Render the 3 articles deposited before the one specified 
    # or the last 3 articles written if the page isn't a standard webpage
    # 
    @http.route(['/website_last_articles_snippet/render/<base>/<int:page>'], type='http', auth='public', website=True)
    def render_latest_posts(self, page, base, template='snippet_last_articles.liste_article', **post):
        cr, uid, context = request.cr, request.uid, request.context
        page_obj = request.registry['ir.ui.view']
        
        if base == 'ir.ui.view': 
            domain = [('page','=','True'),('id','<',page),('active','=','True')]
            page_ids = page_obj.search(cr, uid, domain, limit=3, order='create_date desc', context=context)
        else : 
            domain  [('page','=','True'),('active','=','True')]
            page_ids = page_obj.search(cr, uid, domain, limit=3, order='create_date desc', context=context)
        
        posts = page_obj.browse(cr, uid, page_ids, context=context)

        return request.render("website_last_articles_snippet.liste_articles", {'posts': posts})
