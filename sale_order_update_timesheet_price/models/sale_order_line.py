from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    show_update_price_btn = fields.Boolean(compute="_compute_show_update_price_btn")
    price_unit_updated = fields.Boolean(
        help="Technical field to know if the price has been updated"
    )

    @api.depends("qty_invoiced", "qty_delivered_method", "name")
    def _compute_show_update_price_btn(self):
        for rec in self:
            rec.show_update_price_btn = (
                rec.qty_invoiced != 0
                and rec.qty_delivered_method == "timesheet"
                and not rec.price_unit_updated
            )
