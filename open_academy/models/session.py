from odoo import models, fields


class Session(models.Model):
    _name = 'session'
    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Integer()
    number_of_seats = fields.Integer()
    instructor_id = fields.Many2one('res.partner', domain='["|", ("is_instructor","=",True), ("teacher_type","!=",False)]')
    course_id = fields.Many2one('course', required=True)
    attendees_ids = fields.Many2many('res.partner')
