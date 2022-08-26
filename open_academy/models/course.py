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
    _sql_constraints = [
        ('unique_course_name', 'UNIQUE (name)', 'This course already exists'),
        (
            'check_title_description',
            'CHECK (title NOT LIKE description)',
            'The title must be different than the description'
        )
    ]

    def copy(self, default=None):
        default = default or {}
        copied_count = self.search_count([('name', '=like', 'Copy of %s' % self.name)])
        new_name = 'Copy of %s' % self.name
        new_name += '(%s)' % copied_count if copied_count > 0 else ''
        default.update({'name': new_name})
        return super().copy(default=default)
