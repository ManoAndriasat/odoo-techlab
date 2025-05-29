from odoo import models, fields

class HospitalNurse(models.Model):
    _name = 'hospital.nurse'
    _description = 'Hospital Nurse'

    user_id = fields.Many2one('res.users', string='User')
    name = fields.Char(string='Name', required=True)
