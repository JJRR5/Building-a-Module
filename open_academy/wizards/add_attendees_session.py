from odoo import fields, models


class AddAttendeesSession(models.TransientModel):
    _name = 'add.attendees.session'
    _description = 'Wizard for session model'

    session_ids = fields.Many2many('session', default=lambda self: self._context.get('active_ids'))
    attendees_ids = fields.Many2many('res.partner')

    def add_attendees(self):
        for session in self.session_ids:
            session.attendees_ids |= self.attendees_ids
