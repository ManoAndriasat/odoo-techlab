from odoo import models, fields, api

class RoomRound(models.Model):
    _name = 'room.round'
    _description = 'hospital room round'

    nurse_id = fields.Many2one('hospital.nurse', string='Nurse', required=True)
    room_patient_id = fields.Many2one('room.patient', string='Room Patient', required=True)
    datetime = fields.Datetime(string='Date Time', required=True, default=fields.Datetime.now)
    note = fields.Text(string='Note')