from odoo import models, fields, api

class DocConsultingConsultationLine(models.Model):
    _name = 'doc.consulting.consultation.line'
    _description = 'Doc Consulting Consultation Line'

    consultation_id = fields.Many2one('doc.consulting.consultation', string='Consultation', readonly=True)
    drug_id = fields.Many2one('doc.consulting.drug', string='Drug')
    quantity = fields.Integer(string='Quantity')
    unit_price = fields.Float(string='Price', compute='_set_price', store=True)
    price = fields.Float(string='price', compute='_compute_price', store=True)

    @api.depends('unit_price', 'quantity')
    def _compute_price(self):
        for record in self:
            record.price = record.unit_price * record.quantity

    @api.depends('drug_id')
    def _set_price(self):
        for record in self:
            record.unit_price = record.drug_id.price