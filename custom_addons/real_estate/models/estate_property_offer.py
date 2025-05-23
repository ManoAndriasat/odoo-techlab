from odoo import models, fields, api
from datetime import date, timedelta

class estate_property_offer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Estate Property Offer'

    @api.depends('validity')
    def _compute_date_deadline(self):
        for record in self:
            record.date_deadline = date.today() + timedelta(days=record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            print(record.date_deadline)
            record.validity = (record.date_deadline - date.today()).days

    price = fields.Float(required=True)
    status = fields.Selection(
        [('accepted', 'Accepted'),
        ('refused', 'Refused')],
        copy = False
    )
    partner_id = fields.Many2one('res.partner', required=True)
    property_id = fields.Many2one('estate.property', required= True)
    validity = fields.Integer()
    date_deadline = fields.Date(compute='_compute_date_deadline', inverse='_inverse_date_deadline')