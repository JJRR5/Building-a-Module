from odoo import models, fields


class Session(models.Model):
    _name = 'sessions'
    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Integer()
    number_of_seats = fields.Integer()
