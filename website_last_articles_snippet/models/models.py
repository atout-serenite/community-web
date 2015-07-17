# -*- coding: utf-8 -*-

from openerp import models,api
from openerp.osv import orm, osv, fields
# class testmodule(models.Model):
#     _name = 'testmodule.testmodule'

#     name = fields.Char()

class website_seo_metadata(osv.Model):
    _inherit = 'ir.ui.view'


    def get_slug(self, cr, uid, ids, name, args, context):

        result = {}
        for id in ids:
            model_pool = self.pool.get("ir.model.data")
            ids = model_pool.search(cr, uid, [('module','=','website'), ('res_id','=', id)])
            if not ids:
                raise ValueError('External ID not found in the system: %s' % (id))
            # the sql constraints ensure us we have only one result
            res = model_pool.read(cr, uid, ids[0], ['name'])
            if not res['name']:
                raise ValueError('External ID not found in the system: %s' % (id))
            result[id] = res['name']
            
        return result


    _columns = {
        'website_meta_image': fields.binary("Image"),
        'slug': fields.function(get_slug, string='Slug', type='char'),
    }
