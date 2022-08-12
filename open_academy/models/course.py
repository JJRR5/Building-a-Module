from odoo import models,fields


class course(models.Model):
    _name = 'open_academy.course'
    _description = 'open_academy.course'
    # _title = "Javascript for beginners"
    
    name = fields.Char()
    description = fields.Text()
    
    