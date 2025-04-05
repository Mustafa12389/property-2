from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    property_id = fields.Many2one('property')
   # type number one fe model inheritance esmo tradational inheritance

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        print("inside action_confirm action")
        # da paython intheritance
        return res

