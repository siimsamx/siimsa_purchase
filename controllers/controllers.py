# -*- coding: utf-8 -*-
from odoo import http

# class SiimsaPurchase(http.Controller):
#     @http.route('/siimsa_purchase/siimsa_purchase/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/siimsa_purchase/siimsa_purchase/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('siimsa_purchase.listing', {
#             'root': '/siimsa_purchase/siimsa_purchase',
#             'objects': http.request.env['siimsa_purchase.siimsa_purchase'].search([]),
#         })

#     @http.route('/siimsa_purchase/siimsa_purchase/objects/<model("siimsa_purchase.siimsa_purchase"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('siimsa_purchase.object', {
#             'object': obj
#         })