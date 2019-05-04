# -*- coding: utf-8 -*-

from odoo import models, api
from odoo.exceptions import UserError
import datetime

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.onchange('date_invoice')
    def change_date(self):
        if not self.date_invoice:
            return

        if self.date_invoice > str(datetime.datetime.now().date()):
            self.date_invoice = None
            print(self.partner_id.property_stock_customer.name)
            raise UserError('No puedes guardar facturas con fechas futuras')

