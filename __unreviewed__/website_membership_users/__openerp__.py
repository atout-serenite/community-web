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
    'name': 'Website Membership Users',
    'category': 'Website',
    'summary': 'Website addition to marketplace module',
    'version': '1.0',
    'description': """
        """,
    'author': 'Author Name • WebByBrains <author@webbybrains.com>, Igor Krivonos <igor.krivonos@xpansa.com>',
    'depends': [
        'website',
        'product_price_currency',
        'website_sale',
        'association',
        'membership_users',
        'membership',
        'website_marketplace'
    ],
    'data': [
        'views/assets.xml',
        'views/templates/profile_edit_template.xml',
        'views/templates/profile_view_template.xml',
        'views/templates/member_list_view.xml',
        'views/templates/single_member_view.xml',
        'views/templates/user_notify_sms.xml',
    ],
    'installable': True
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
