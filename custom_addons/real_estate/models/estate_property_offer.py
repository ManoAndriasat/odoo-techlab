from odoo import models, fields

class estate_property_offer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Estate Property Offer'

    price = fields.Float(required=True)
    status = fields.Selection(
        [('accepted', 'Accepted'),
        ('refused', 'Refused')],
        copy = False
    )
    partner_id = fields.Many2one('res.partner', required=True)
    property_id = fields.Many2one('estate.property', required= True)