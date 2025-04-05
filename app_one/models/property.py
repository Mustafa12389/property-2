from odoo import models, fields, api

from odoo.exceptions import ValidationError

from email.policy import default
from encodings.punycode import digits


class Property (models.Model) :

    _name="property"
    _description = 'Property'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name=fields.Char(required=1, default='new', size=17)
    description=fields.Text(tracking=1)
    postcode=fields.Char(required=1)
    expected_selling_date=fields.Date(tracking=1)
    date_availability=fields.Date(tracking=1)
    is_late=fields.Boolean()
    expected_price=fields.Float()
    selling_price=fields.Float()
    diff = fields.Float(compute='_compute_diff', store=1)
    bedrooms=fields.Integer()
    living_area=fields.Integer ()
    facades=fields.Integer()
    garage=fields.Boolean ()
    garden=fields.Boolean ()
    garden_area=fields.Integer()
    garden_orientation=fields.Selection([
         ('north' , 'NORTH'),
         ('south' , 'SOUTH'),
         ('east', 'EAST'),
         ('west', 'WEST'),
    ], default='north')
    owner_id = fields.Many2one('owner')
    tag_ids = fields.Many2many('tag')
    owner_address = fields.Char(related='owner_id.address',readonly=0)
    owner_phone = fields.Char(related='owner_id.phone',readonly=0)

    state = fields.Selection( [
        ('draft', 'Draft'),
        ('pending', 'Pending'),
        ('sold', 'Sold'),
        ('closed', 'Closed'),
    ], default='draft')
    active = fields.Boolean(default=True)
    # lw 3ndy 7aga bt5alf el constraints dah msh hetb2a y3ni lw 2 fatora be nafs el esm msh hattb2ael constraints


    _sql_constraints = [
        ('unique_name', 'unique("name")', 'This name already exists!')
    ]
    line_ids =fields.One2many('property.line','property_id')

    def action_draft(self):
        for rec in self:
            print("inside draft action")
            rec.state = 'draft'

    def action_pending(self):
        for rec in self:
            print("inside pending action")
            rec.state = 'pending'

    def action_sold(self):
        for rec in self:
            print("inside sold action")
            rec.state = 'sold'

    # def action_closed(self):
    #     for rec in self:
    #         print("inside closed action")
    #         rec.state = 'closed'

    def check_expected_selling_date(self):
        property_ids = self.search([])
        for rec in property_ids:
            if rec.expected_selling_date and rec.expected_selling_date < fields.date.today():
                rec.is_late = True

    @api.depends('expected_price', 'selling_price')
    def _compute_diff(self):
        for rec in self:
            print("inside _compute_diff method")
            rec.diff = rec.expected_price - rec.selling_price

        @api.onchange('expected_price')
        def _onchange_expected_price(self):
            for rec in self:
                print("inside _onchange_expected_price method")
    @api.constrains('bedrooms')
    def _check_bedrooms_greater_zero(self):
        for rec in self:
            if rec.bedrooms <= 0:
                raise ValidationError('Please enter a valid number of bedrooms)')



            # CRUD operation  (create , read ,update , delete)

    @api.model_create_multi
    def create(self, vals):
        res = super(Property, self).create(vals)
        print("inside create method:", res)
        # logical
        return res

    @api.model
    def _search(self, domain, offset=0, limit=None, order=None, access_rights_uid=None):
        res = super(Property, self)._search(domain, offset, limit, order, access_rights_uid)
        print("Inside search method:", res)
        # logic
        return res

    def write(self, vals):
        res = super(Property, self).write(vals)
        print("inside write method:", res)
        # logical
        return res

    def unlink(self):
        res = super(Property, self).unlink()
        print("inside unlink method:", res)
        # logical
        return res

class PropertyLines(models.Model) :

   _name="property.line"

   property_id = fields.Many2one('property')
   area = fields.Float()
   description = fields.Char()
