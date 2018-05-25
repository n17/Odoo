# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class partner_company_code(models.Model):
#     _name = 'partner_company_code.partner_company_code'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100