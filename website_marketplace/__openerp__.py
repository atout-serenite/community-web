# -*- coding: utf-8 -*-
#
#
#    Website Marketplace
#    Copyright (C) 2014 Xpansa Group (<http://xpansa.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#

{
    'name': 'Website Marketplace',
    'category': 'Website',
    'summary': 'Website addition to marketplace module',
    'version': '1.0',
    'description': """
Custom Theme
Website Marketplace

        """,
    'author': 'Author Name • WebByBrains <author@webbybrains.com>, Igor Krivonos <igor.krivonos@xpansa.com>',
    'depends': [
        'website',
        'marketplace',
        'marketplace_groups',
        'website_base_community'
    ],
    'data': [
        'data/menu.xml',
        'data/marketplace_announcement_category.xml',
        'data/users.xml',
        'views/assets.xml',
        'views/templates/mp_search.xml',
        'views/templates/mp_search_form.xml',
        'views/templates/mp_single_item.xml',
        'views/templates/mp_single_item_parent.xml',
        'views/templates/mp_four_item.xml',
        'views/templates/single_reply.xml',
        'views/templates/view_announcement.xml',
        'views/templates/edit_announcement.xml',
        'views/templates/new_announcement.xml',
        'security/ir.model.access.csv',
        'security/website_marketplace_security.xml',
    ],
    'installable': True
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
