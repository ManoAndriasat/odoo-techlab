from odoo import models, fields

class HospitalDisease(models.Model):
    _name = 'hospital.disease'
    _description = 'Hospital Disease'

    name = fields.Char(string='Disease Name', required=True)
    symptoms = fields.Text(string='Symptoms', required=True)
    severity = fields.Selection([
        ('mild', 'Mild'),
        ('moderate', 'Moderate'),
        ('severe', 'Severe'),
    ], string='Severity', default='mild')