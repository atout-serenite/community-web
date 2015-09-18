# -*- coding: utf-8 -*-
##############################################################################
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
##############################################################################

import openerp
from openerp.addons.auth_signup.controllers.main import AuthSignupHome
from openerp.addons.auth_signup.res_users import SignupError
from openerp.addons.website.models.website import slug
from openerp.addons.website_blog.controllers.main import QueryURL
from openerp.addons.web import http
from openerp.tools import DEFAULT_SERVER_DATETIME_FORMAT, DEFAULT_SERVER_DATE_FORMAT
from openerp.tools.translate import _
from openerp.http import request

from datetime import datetime
from HTMLParser import HTMLParser
import werkzeug
from openerp.addons.website_base_community.controllers.main import strip_tags, format_text


class Website(http.Controller):

    ANNOUNCEMENT_LIMIT = 3

    def get_last_announcements(self, ttype):
        cr, uid, context, registry = request.cr, \
            request.uid, request.context, request.registry
        announcement_pool = registry.get('marketplace.announcement')
        announcement_ids = announcement_pool.search(
            cr, uid, [('state','=', 'open'), ('type', '=', ttype)],
            limit=self.ANNOUNCEMENT_LIMIT, order="date_from DESC",
            context=context
        )
        return announcement_pool.browse(
            cr, uid, announcement_ids, context=context
        )

    def get_last_event(self):
        """
        Get one last event
        :return: browse_record
        """
        cr, uid, context, registry = request.cr, \
            request.uid, request.context, request.registry
        event_pool = registry.get('event.event')
        event_id = event_pool.search(
            cr, uid, [('state','=','confirm')], order="date_begin DESC",
            limit=1, context=context
        )
        return event_pool.browse(
            cr, uid, event_id, context=context
        )[0] if event_id else False

    def get_last_blog_post(self):
        """
        Get one last blog post
        :return: browse_record
        """
        cr, uid, context, registry = request.cr, \
            request.uid, request.context, request.registry
        post_pool = registry.get('blog.post')
        post_id = post_pool.search(
            cr, uid, [('website_published','=',True)], order="id DESC",
            limit=1, context=context
        )
        return post_pool.browse(
            cr, uid, post_id, context=context
        )[0] if post_id else False

    @http.route('/page/homepage', type='http', auth="public", website=True)
    def page(self):
        """
        Homepage
        """
        blog_url = QueryURL('', ['blog', 'tag'])
        values = {
            'wants': self.get_last_announcements('want'),
            'offers': self.get_last_announcements('offer'),
            'format_text': format_text,
            'event': self.get_last_event(),
            'strip_tags': strip_tags,
            'blog_post': self.get_last_blog_post(),
            'blog_url': blog_url,
        }
        return request.render('website_community_home.homepage', values)
