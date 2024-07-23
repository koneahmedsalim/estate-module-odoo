from odoo import models,fields

class EstateProperty(models.Model):
    _name = "estate_property"
    _description = "Maison"
    
    name = fields.Char()
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float()
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(selection=[
            ('north', 'North'),
            ('south', 'South'),
            ('east', 'East'),
            ('west', 'West'),
            ('northeast', 'North East'),
            ('northwest', 'North West'),
            ('southeast', 'South East'),
            ('southwest', 'South West'),
        ],
        string='Garden Orientation',
        help='Select the orientation of the garden')