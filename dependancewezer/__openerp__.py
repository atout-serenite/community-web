# -*- coding: utf-8 -*-
{
    'name': "Dependance Wezer",

    'summary': """
        Installation des depenses pour wezer 
    """,

    'description': """
        Installation des depenses pour wezer
    """,

    'author': "Yann LE GOFF",
    'website': "http://www.atout-serenite.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['marketplace','website','website_community_home','disable_openerp_online','website_community_template','website_membership_users','website_marketplace','langue_img','website_event'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}