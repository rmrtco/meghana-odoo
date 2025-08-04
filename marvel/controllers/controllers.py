# -*- coding: utf-8 -*-
# from odoo import http


# class DevanshInsurance(http.Controller):
#     @http.route('/devansh_insurance/devansh_insurance', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/devansh_insurance/devansh_insurance/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('devansh_insurance.listing', {
#             'root': '/devansh_insurance/devansh_insurance',
#             'objects': http.request.env['devansh_insurance.devansh_insurance'].search([]),
#         })

#     @http.route('/devansh_insurance/devansh_insurance/objects/<model("devansh_insurance.devansh_insurance"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('devansh_insurance.object', {
#             'object': obj
#         })
