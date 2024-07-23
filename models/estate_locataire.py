from odoo import models, fields

class EstateTenant(models.Model):
    _name = 'estate_tenant'
    _description = 'Locataire'
    
    name = fields.Char(string="Nom du locataire")
    description = fields.Text()
    move_in_date = fields.Date(string="Date d'emménagement")
    move_out_date = fields.Date(string="Date de départ")
    rent = fields.Float(string="Loyer")
    property_id = fields.Many2one('estate_property', string="Propriété")
