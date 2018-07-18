from odoo import fields, models, api, exceptions

class Partner(models.Model):
    _inherit = 'res.partner'

    # Adds a new field to the res.partner model.
    company_code = fields.Char(string="Company code")

    # Adds a constraint to the company_code field.
    @api.constrains('company_code')
    def _check_cc_number(self):
        for r in self:
            if self.env['res.partner'].search_count([('company_code','=', r.company_code)]) > 3:
                raise exceptions.ValidationError("No more than 3 companies may have the same company code!")

