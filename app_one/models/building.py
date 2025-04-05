from odoo import models, fields



class Building(models.Model) :

    _name="building"
    _description = 'Building Record'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    no = fields.Integer(string="No")
    code = fields.Char(string="Code")
    description = fields.Text(string="Description")
    name = fields.Char()
    active = fields.Boolean(default=True)
