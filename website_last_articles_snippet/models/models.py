# -*- coding: utf-8 -*-

from openerp import models,api
from openerp.osv import orm, osv, fields
# class testmodule(models.Model):
#     _name = 'testmodule.testmodule'

#     name = fields.Char()

class website_seo_metadata(osv.Model):
    _inherit = 'ir.ui.view'

    _columns = {
        'website_meta_image': fields.binary("Image"),
    }
