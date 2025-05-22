from odoo import models, fields, api

class DocConsultingDrug(models.Model):
    _name = 'doc.consulting.drug'
    _description = 'Doc Consulting Drug'

    name = fields.Char(string='Name')
    price = fields.Float(string='Price')
