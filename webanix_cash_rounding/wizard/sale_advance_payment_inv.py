import logging

from odoo import models

_logger = logging.getLogger(__name__)


class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    def _prepare_down_payment_invoice_values(self, order, so_lines):
        res = super()._prepare_down_payment_invoice_values(order, so_lines)
        company = order.company_id
        if company.x_invoice_cash_rounding_id:
            res["invoice_cash_rounding_id"] = company.x_invoice_cash_rounding_id.id
        return res
