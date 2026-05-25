from odoo import fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    cash_rounding_id = fields.Many2one(
        "account.cash.rounding",
        string="Cash Rounding",
        copy=False,
        help="Cash rounding method applied automatically to vendor bills from this purchase order.",
    )

    def _apply_company_cash_rounding(self):
        for order in self:
            rounding = order.company_id.invoice_cash_rounding_id
            if rounding and not order.cash_rounding_id:
                order.cash_rounding_id = rounding
        return True

    def button_confirm(self):
        self._apply_company_cash_rounding()
        return super().button_confirm()

    def _prepare_invoice(self):
        vals = super()._prepare_invoice()
        rounding = self.cash_rounding_id or self.company_id.invoice_cash_rounding_id
        if rounding:
            vals["invoice_cash_rounding_id"] = rounding.id
        return vals
