# -*- coding: utf-8 -*-
from odoo import http

# class /odoo11/custom/addons/invocingFutureDateValidation(http.Controller):
#     @http.route('//odoo11/custom/addons/invocing_future_date_validation//odoo11/custom/addons/invocing_future_date_validation/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//odoo11/custom/addons/invocing_future_date_validation//odoo11/custom/addons/invocing_future_date_validation/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/odoo11/custom/addons/invocing_future_date_validation.listing', {
#             'root': '//odoo11/custom/addons/invocing_future_date_validation//odoo11/custom/addons/invocing_future_date_validation',
#             'objects': http.request.env['/odoo11/custom/addons/invocing_future_date_validation./odoo11/custom/addons/invocing_future_date_validation'].search([]),
#         })

#     @http.route('//odoo11/custom/addons/invocing_future_date_validation//odoo11/custom/addons/invocing_future_date_validation/objects/<model("/odoo11/custom/addons/invocing_future_date_validation./odoo11/custom/addons/invocing_future_date_validation"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/odoo11/custom/addons/invocing_future_date_validation.object', {
#             'object': obj
#         })