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
    'name': 'Website Community Home',
    'category': 'Website',
    'version': '1.0',
    'description': """
        """,
    'author': 'Author Name • WebByBrains <author@webbybrains.com>, Igor Krivonos <igor.krivonos@xpansa.com>',
    'depends': [
        'auth_signup',
        'website_marketplace',
        'website_event',
    ],
    'data': [
        'views/templates/home.xml',
    ],
    'installable': True
}
