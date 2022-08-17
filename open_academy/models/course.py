from odoo import models, fields


class course(models.Model):
    _name = 'open_academy.course'
    _title = 'open_academy.course'
    _description = 'open_academy.course'
    
    name = fields.Char()
    title = fields.Text()
    description = fields.Text()
    responsible_user_id = fields.Many2one('res.users')
    session_id = fields.One2many('open_academy.sessions','courses_id')   
