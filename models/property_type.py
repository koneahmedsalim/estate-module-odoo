from odoo import fields, models

class EstateTenantType(models.Model):
    _name = 'estate.tenant.type'
    _description = 'Type de Locataire'

    name = fields.Char(string='Type de Locataire', required=True)
#f