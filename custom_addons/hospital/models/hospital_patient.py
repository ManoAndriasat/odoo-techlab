from odoo import models, fields, api

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'

    user_id = fields.Many2one('res.users', string='User')
    name = fields.Char(string='Full Name', compute='_compute_name', store=True)
    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    consultation_ids = fields.One2many('hospital.consultation', 'patient_id', string='Consultations')
    record_ids = fields.One2many('hospital.patient.record', 'consultation_id', string='Records')

    @api.depends('first_name', 'last_name')
    def _compute_name(self):
        for record in self:
            record.name = f"{record.first_name} {record.last_name}"