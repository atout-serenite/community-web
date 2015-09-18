# -*- coding: utf-8 -*-

from openerp.tools.translate import _
from openerp.osv import fields, orm

class res_partner_sms(orm.Model):
    """ Update partner to add a field about notification preferences """
    _name = "res.partner"
    _inherit = 'res.partner'

    _columns = {
        'notify_sms': fields.selection([
            ('yes', 'Oui'),
            ('no', 'Non'),
            ], 'Receive Inbox Notifications by Sms', required=True,
            ),
    }

    _defaults = {
        'notify_sms': lambda *args: 'yes'
    }