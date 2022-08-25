from odoo import models, fields, api


class Session(models.Model):
    _name = 'session'
    name = fields.Char(required=True)
    start_date = fields.Date(default=fields.Date.today())
    duration = fields.Integer()
    number_of_seats = fields.Integer()
    instructor_id = fields.Many2one('res.partner', domain='["|", ("is_instructor","=",True), ("teacher_type","!=",False)]')
    course_id = fields.Many2one('course', required=True)
    attendees_ids = fields.Many2many('res.partner')
    active = fields.Boolean(default=True)
    taken_seats = fields.Integer(compute='_compute_taken_seats')

    @api.depends('number_of_seats', 'attendees_ids')
    def _compute_taken_seats(self):
        for record in self:
            taken_seats = 0
            if record.number_of_seats > 0:
                taken_seats = round((len(record.attendees_ids) * 100) / record.number_of_seats)
            record.taken_seats = taken_seats
