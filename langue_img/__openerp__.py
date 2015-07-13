# -*- coding: utf-8 -*-
{
    'name': "Gestion des Langues / Drapeaux (Menu Website)",

    'summary': """
        Gestionnaire de Menu des Langues avec Images
    """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Yann LE GOFF Atout-Serenite.com",
    'website': "http://www.Atout-Serenite.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'website',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['website', 'website_community_template'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],    
    'installable': True,
    'application': True,
}