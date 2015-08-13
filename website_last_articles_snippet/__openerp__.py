# -*- coding: utf-8 -*-
#
#
#    Website Last Articles Snippet
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
    'name': 'Website Last Articles Snippet',
    'category': 'Website',
    'summary': 'Display the articales created just before the current article',
    'version': '1.0',
    'description': """
Introduce a sniipt that displays the last 3 articles posted

        """,
    'author': 'Author Name • David Mills <dmills@atout-serenite.com>',
    'depends': [
        'website',
        'website_blog',
    ],
    'data': [
        'views/snippets.xml',
    ],
    'installable': True
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
