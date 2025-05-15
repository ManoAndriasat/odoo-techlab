from odoo import models, fields, api
from datetime import date, timedelta

class EstateProperty(models.Model):    
    _name = 'estate.property'
    _description = 'Estate Property'

    @api.model
    def _next_availability(self):
        return date.today() + timedelta(days=90)

    @api.model
    def _default_user(self):
        return self.env.user

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False, default=_next_availability)
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    property_type_id = fields.Many2one('estate.property.type')
    tag_ids = fields.Many2many('estate.property.tag', string='Tags')
    offer_ids = fields.One2many('estate.property.offer', 'property_id',  string='Offers')
    garden_area = fields.Integer()
    sales_person_id = fields.Many2one('res.users',default=_default_user)
    buyer_id = fields.Many2one('res.partner',copy=False)
    active = fields.Boolean(default=True)
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West'),
    ])
    state = fields.Selection([
        ('new', 'New'),
        ('offer_received', 'Offer Received'),
        ('offer_accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('cancelled', 'Cancelled')
    ], required=True, copy=False, default='new')