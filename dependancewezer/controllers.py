# -*- coding: utf-8 -*-
from openerp import http

# class Dependancewezer(http.Controller):
#     @http.route('/dependancewezer/dependancewezer/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dependancewezer/dependancewezer/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dependancewezer.listing', {
#             'root': '/dependancewezer/dependancewezer',
#             'objects': http.request.env['dependancewezer.dependancewezer'].search([]),
#         })

#     @http.route('/dependancewezer/dependancewezer/objects/<model("dependancewezer.dependancewezer"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dependancewezer.object', {
#             'object': obj
#         })