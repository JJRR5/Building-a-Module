from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import date, timedelta


class Session(models.Model):
    _name = 'session'
    name = fields.Char(required=True)
    start_date = fields.Date(default=date.today(), required=True)
    end_date = fields.Date(compute='_compute_end_date')
    duration = fields.Integer(required=True, string="Duration (days)")
    number_of_seats = fields.Integer()
    instructor_id = fields.Many2one(
        'res.partner', domain='["|", ("is_instructor","=",True), ("teacher_type","!=",False)]'
    )
    course_id = fields.Many2one('course', required=True)
    attendees_ids = fields.Many2many('res.partner')
    number_of_attendees = fields.Integer(compute='_compute_number_of_attendees', store=True)
    active = fields.Boolean(default=True)
    taken_seats = fields.Integer(compute='_compute_taken_seats')

    @api.depends('number_of_seats', 'attendees_ids')
    def _compute_taken_seats(self):
        for record in self:
            taken_seats = 0
            if record.number_of_seats > 0:
                taken_seats = round((len(record.attendees_ids) * 100) / record.number_of_seats)
            record.taken_seats = taken_seats

    @api.onchange('number_of_seats', 'attendees_ids')
    def _onchange_invalid_values(self):
        if self.number_of_seats < 0:
            return {
                'warning': {
                    'title': _("Something bad happened."),
                    'message': _("Number of seats must be greater than 0.")
                }
            }
        if len(self.attendees_ids) > self.number_of_seats:
            return {
                'warning': {
                    'title': _("Something bad happened."),
                    'message': _("Number of attendees cannot be greater than the number of available seats.")
                }
            }

    @api.constrains('attendees_ids')
    def _check_attendees_ids(self):
        for record in self:
            if record.instructor_id in record.attendees_ids:
                raise ValidationError(_("An instructor cannot be an attendee of his own session"))

    @api.depends('duration', 'start_date')
    def _compute_end_date(self):
        for record in self:
            difference = timedelta(days=record.duration)
            record.end_date = record.start_date + difference

    @api.depends('attendees_ids')
    def _compute_number_of_attendees(self):
        for record in self:
            record.number_of_attendees = len(record.attendees_ids)
