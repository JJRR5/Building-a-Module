from odoo import models, fields


class sessions(models.Model):
    _name = 'open_academy.sessions'
    _description = 'This is a sessions model'
    
    name = fields.Char()
    start_date = fields.Date(required=True)
    duration = fields.Integer()
    number_of_seats = fields.Integer()
    instructor_id = fields.Many2one('res.partner')
    courses_id = fields.Many2one('open_academy.course') 
    attendees_ids = fields.Many2many("res.partner", string="Attendees")
