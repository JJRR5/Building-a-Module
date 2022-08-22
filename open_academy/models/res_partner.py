from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_instructor = fields.Boolean()
    teacher_type = fields.Selection(
        selection=[('level1', 'Level 1'), ('level2', 'Level 2')],
    )
    session_ids = fields.Many2many('session')
