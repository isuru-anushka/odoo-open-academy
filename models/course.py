from odoo import models, fields

class Course(models.Model):
    _name = "course.model"

    title = fields.Char(string="Title",required=True)
    desc = fields.Text(string="Description")
