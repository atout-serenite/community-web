import werkzeug
from openerp.addons.web import http
from openerp.addons.web.http import request


class snippet_latest_posts_controller(http.Controller):
	@http.route(['/snippet_latest_posts/render'], type='http', auth='public', website=True)
	def render_latest_posts(self, template='snippet_last_articles.liste_article', limit=3, order='create_date desc', **post):
		cr, uid, context = request.cr, request.uid, request.context
		page_obj = request.registry['ir.ui.view']

		page_ids = page_obj.search(cr, uid, [('page','=','True'),('page','=','True')], limit=3, order='create_date desc', context=context)
		posts = page_obj.browse(cr, uid, page_ids, context=context)
		page_obj = request.registry['blog.post']

		return request.render("last_articles_block.liste_last", {'posts': posts})
		
	@http.route(['/snippet_latest_posts/array'], type='json', auth='public', website=True)
	def array_latest_posts(self, template='snippet_last_articles.liste_article', limit=3, order='create_date desc', **post):
		cr, uid, context = request.cr, request.uid, request.context
		page_obj = request.registry['ir.ui.view']

		page_ids = page_obj.search(cr, uid, [('page','=','True'),('page','=','True')], limit=3, order='create_date desc', context=context)
		posts = page_obj.browse(cr, uid, page_ids, context=context)
		page_obj = request.registry['blog.post']
		
		return {'posts': posts}
