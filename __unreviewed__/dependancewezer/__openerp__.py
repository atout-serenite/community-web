# -*- coding: utf-8 -*-
{
    'name': "Dependance Wezer",

    'summary': """
        Installation des dependances pour wezer 
    """,

    'description': """
        Installation des dependances pour wezer
    """,

    'author': "Yann LE GOFF",
    'website': "http://www.atout-serenite.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'marketplace',
        'website',
        'website_community_home',
        'disable_openerp_online',
        'website_community_template',
        'website_membership_users',
        'website_marketplace',
        'website_last_articles_snippet',
        'website_language_flags',
        'website_event',
        'website_forum'
        ],

    # always loaded
    'data': [
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}