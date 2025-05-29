from odoo import models, fields, api

class RoomPatient(models.Model):
    _name = 'room.patient'
    _description = 'hospital room patient'

    patient_record_id = fields.Many2one('hospital.patient.record', string='Patient Record', required=True, readonly=True, ondelete='cascade')
    room_id = fields.Integer(string='Room')
    state = fields.Selection([
        ('in_treatment', 'In Treatment'),
        ('remission', 'Remission'),
        ('go_home', 'Go Home'),
    ], string='State', default='in_treatment')
    round_ids = fields.One2many('room.round', 'room_patient_id', string='Rounds')