from odoo import models, fields

class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Hospital Doctor'

    user_id = fields.Many2one('res.users', string='User')
    name = fields.Char(string='Name', required=True)
    door = fields.Integer(string='Door Number')
    consultation_ids = fields.One2many('hospital.consultation', 'doctor_id', string='Consultations')
    active = fields.Boolean(string='Active', default=True)
