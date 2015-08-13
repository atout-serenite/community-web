# -*- coding: utf-8 -*-

from openerp import models,api
from openerp.osv import orm, osv, fields
from openerp.addons.website.models.website import slug


class blog_post(osv.Model):
    _inherit = 'blog.post'

    def get_slug(self, cr, uid, ids, name, args, context):

    	result = {}

    	for post in self.browse(cr, uid, ids):       
	    	result[post.id] = '/blog/%(blog_slug)s/post/%(post_slug)s' % {
        	    'blog_slug': slug(post.blog_id),
                'post_slug': slug(post),
        	}

        return result


    _columns = {
        'slug': fields.function(get_slug, string='Slug', type='char'),
    }