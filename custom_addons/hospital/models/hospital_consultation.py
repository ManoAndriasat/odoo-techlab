from odoo import models, fields, api

class HospitalConsultation(models.Model):
    _name = 'hospital.consultation'
    _description = 'Hospital Consultation'

    patient_id = fields.Many2one('hospital.patient', string='Patient')
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor')
    symptoms = fields.Text(string='Symptoms', required=True)
    date = fields.Datetime(string='Date')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done')
    ], string='State', default='draft', compute='_confirmed', store=True)
    active = fields.Boolean(string='Active', default=True)

    @api.depends('doctor_id','date')
    def _confirmed(self):
        for record in self:
            if record.doctor_id and record.date:
                record.state = 'confirmed'
            else:
                record.state = 'draft'

    @api.depends('state')
    def _done(self):
        for record in self:
            if record.state == 'done':
                record.active = False

    def make_diagnosis(self):
        for record in self:
            if record.state == 'confirmed':
                record.state = 'done'
        patient_record = self.env['hospital.patient.record'].create({
            'consultation_id': self.id,
        })
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'hospital.patient.record',
            'res_id': patient_record.id,
            'view_mode': 'form',
            'target': 'current',
        }