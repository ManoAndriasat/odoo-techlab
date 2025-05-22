from odoo import models, fields, api, _
from datetime import date, timedelta
from odoo.exceptions import ValidationError

class DocConsultingDoctor(models.Model):
    _name = 'doc.consulting.doctor'
    _description = 'Doc Consulting Doctor'

    name = fields.Char(string='Name')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    consultation_ids = fields.One2many('doc.consulting.consultation', 'doctor_id', string='Consultations')