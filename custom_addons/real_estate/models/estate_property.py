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

    @api.onchange('garden')
    def _onchange_garden(self):
        if self.garden:
            self.garden_orientation = 'north'
            self.garden_area = 10

    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends('offer_ids','offer_ids.price')
    def _compute_best_offer(self):
        for record in self:
            record.best_price = max(record.offer_ids.mapped('price') ,default=0)


    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False, default=_next_availability)
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    garden_area = fields.Integer()
    total_area = fields.Integer(compute='_compute_total_area')
    facades = fields.Integer()
    garage = fields.Boolean(default=False)
    garden = fields.Boolean(default=False)
    property_type_id = fields.Many2one('estate.property.type')
    tag_ids = fields.Many2many('estate.property.tag', string='Tags')
    offer_ids = fields.One2many('estate.property.offer', 'property_id',  string='Offers')
    best_price = fields.Float(compute='_compute_best_offer', string='Best Offer')
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


    def cancel_property(self):
        for record in self:
            if record.state != 'sold':
                record.state = 'cancelled'
        return True

    def sold_property(self):
        for record in self:
            if record.state != 'cancelled':
                record.state = 'sold'
        return True