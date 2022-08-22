from odoo import models, fields


class Course(models.Model):
    _name = 'course'
    _title = 'open_academy.course'
    _description = 'Open Academy Course'
    name = fields.Char(required=True)
    title = fields.Text()
    description = fields.Text()
    responsible_user_id = fields.Many2one('res.users')
    session_ids = fields.One2many('session', 'course_id')
