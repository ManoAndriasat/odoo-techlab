from odoo import models, fields, api

class DocConsultingPatient(models.Model):
    _name = 'doc.consulting.patient'
    _description = 'Doc Consulting Patient'

    name = fields.Char(string='Name')
    phone = fields.Char(string='Phone')
    consultation_ids = fields.One2many('doc.consulting.consultation', 'patient_id', string='Consultations')