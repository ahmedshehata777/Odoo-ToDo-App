from odoo import fields, models


class Ticket(models.Model):
    _name = "todo.ticket"
    _description = "Ticket"

    name = fields.Char()
    number = fields.Integer()
    tag = fields.Char()
    state = fields.Selection([
        ('new', 'New'),
        ('doing', 'Doing'),
        ('done', 'Done'),
    ])
    file = fields.Char()
    description = fields.Text()
