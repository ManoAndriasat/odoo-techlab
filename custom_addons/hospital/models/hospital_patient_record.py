from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import timedelta

class HospitalPatientRecord(models.Model):
    _name = 'hospital.patient.record'
    _description = 'Hospital Patient Record'

    consultation_id = fields.Many2one('hospital.consultation', string='Consultation', readonly=True, ondelete='cascade')
    disease_ids = fields.Many2many('hospital.disease', string='Diseases')
    severity_level = fields.Selection([
        ('mild', 'Mild'),
        ('moderate', 'Moderate'),
        ('severe', 'Severe')
    ], string='Severity Level')
    tips = fields.Text(string='Tips')
    prescription_ids = fields.One2many('hospital.prescription', 'patient_record_id', string='Prescriptions')
    decision = fields.Selection([
        ('go_home', 'Go Home'),
        ('hospitalized', 'Hospitalized')
    ], string='Decision',compute = '_compute_decision', store=True)
    duration = fields.Integer(string='Duration')
    date_begin = fields.Date(string='Date Begin', default=fields.Date.today)
    date_end = fields.Date(string='Date End', compute='_compute_duration', inverse='_inverse_duration', store=True)
    state = fields.Selection([
        ('on_progress', 'On Progress'),
        ('done', 'Done')
    ], string='State', default='on_progress')
    active = fields.Boolean(string='Active', default=True)

    @api.depends('date_begin', 'duration')
    def _compute_duration(self):
        for record in self:
            if record.date_begin and record.duration:
                record.date_end = record.date_begin + timedelta(days=record.duration)
            else:
                record.date_end = False
    
    def _inverse_duration(self):
        for record in self:
            if record.date_begin and record.date_end:
                record.duration = (record.date_end - record.date_begin).days
            else:
                record.duration = 0

    @api.depends('severity_level')
    def _compute_decision(self):
        for record in self:
            if record.severity_level in ['mild', 'moderate']:
                record.decision = 'go_home'
            elif record.severity_level =='severe':
                record.decision = 'hospitalized'
            else:
                record.decision = False

    @api.constrains('date_begin', 'date_end')
    def _check_dates(self):
        for record in self:
            if record.date_begin and record.date_end and record.date_begin > record.date_end:
                raise UserError("The start date cannot be later than the end date.")
    
    @api.constrains('prescription_ids', 'severity_level')
    def _check_prescriptions(self):
        for record in self:
            if not record.prescription_ids and record.severity_level in ['moderate', 'severe']:
                raise UserError("Severe cases must have at least one prescription.")

    def send_to_hospital(self):
        if 'room.patient' not in self.env:
            raise UserError("Install the 'room' module to manage room patients.")

        for record in self:
            self.env['room.patient'].create({
                'patient_record_id': record.id,
                'state': 'in_treatment',
            })

class HospitalPrescription(models.Model):
    _name = 'hospital.prescription'
    _description = 'Hospital Prescription'
    patient_record_id = fields.Many2one('hospital.patient.record', string='Patient Record', required=True, readonly=True, ondelete='cascade')
    medication_id = fields.Many2one('product.template', string='Medication', required=True)
    medication_variant_id = fields.Many2one(
        'product.product',
        string='Medication Variant',
        domain="[('product_tmpl_id', '=', medication_id)]",
        required=True,
    )
    quantity = fields.Integer(string='Quantity', required=True)
    notes = fields.Text(string='Notes')

    @api.onchange('medication_id')
    def _onchange_medication_id(self):
        self.medication_variant_id = False
