from odoo import models, fields, api, _
from datetime import date, timedelta
from odoo.exceptions import ValidationError

class DocConsultingConsultation(models.Model):
    _name = 'doc.consulting.consultation'
    _description = 'Doc Consulting Consultation'

    purpose = fields.Char(string='Purpose')
    patient_id = fields.Many2one('doc.consulting.patient', string='Patient')
    doctor_id = fields.Many2one('doc.consulting.doctor', string='Doctor', readonly=True)
    consultation_date = fields.Date(string='Consultation Date', required=True, default=fields.Date.today)
    consultation_line_ids = fields.One2many('doc.consulting.consultation.line', 'consultation_id', string='Consultation Lines')
    total_price = fields.Float(string='Total Price', store=True, compute='_compute_total_price')
    active = fields.Boolean(string='Active', default=True)
    state = fields.Selection([
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
    ], string='State', default='not_started')

    @api.depends('consultation_line_ids.price','consultation_line_ids')
    def _compute_total_price(self):
        for record in self:
            record.total_price = sum(line.price for line in record.consultation_line_ids)

    @api.constrains('doctor_id', 'consultation_date')
    def _check_doctor_availability(self):
        for record in self:
            on_progress_consultation = self.search([
                ('doctor_id', '=', record.doctor_id.id),
                ('consultation_date', '=', record.consultation_date),
                ('state', '=', 'in_progress'),
                ('id', '!=', record.id)
            ])
            if len(on_progress_consultation) >= 3:
                raise ValidationError("HI %s ,The doctor already has 3 consultations in progress for the day: %s"  % (record.doctor_id.name, record.consultation_date))