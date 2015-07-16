# -*- coding: utf-8 -*-

from openerp import models,api
from openerp.osv import orm, osv, fields
# class testmodule(models.Model):
#	 _name = 'testmodule.testmodule'

#	 name = fields.Char()

class website_seo_metadata(osv.Model):
    _inherit = 'ir.ui.view'

    _columns = {
        'website_meta_image': fields.binary("Image"),
    }

    @api.model
    def get_image_base64(self):
        return "data:image/png;base64,%s" % (self.website_meta_image)
    @api.model
    def page_url(self):
    	page = 'website.%s' % self.id
    	return page

class snippet_latest_posts_controller(models.Model):
	_name = 'last_articles_block.render_latest_posts'
	def render_latest_posts(self, template='snippet_last_articles.liste_article', limit=3, order='create_date desc', **post):
		cr, uid, context = request.cr, request.uid, request.context
		page_obj = request.registry['ir.ui.view']

		page_ids = page_obj.search(cr, uid, [('page','=','True'),('page','=','True')], limit=3, order='create_date desc', context=context)
		posts = page_obj.browse(cr, uid, page_ids, context=context)
		page_obj = request.registry['blog.post']

		# page_ids = page_obj.search(cr, uid, [], limit=3, order='create_date desc', context=context)
		# posts = page_obj.browse(cr, uid, page_ids, context=context)
		#post_ids = blog_obj.search(cr, uid, [], context=context)
		return {'posts': posts}


# class last_articles_block(models.Model) : 
# 	_name = 'last_articles_block.last_articles_block'
# 	projet = request.registry['testmodule.gestionnaire']
# 	projet_aff = projet.browse(cr, uid, [], context=context)
# 	values = {
# 			'projet': projet_aff,
# 	}
# 	response = request.website.render("last_articles_block.website_last_article_snippet", values)
# 	return response
