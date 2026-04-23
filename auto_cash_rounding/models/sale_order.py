import logging

from odoo import models

_logger = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _create_invoices(self, grouped=False, final=False, date=None):
        moves = super()._create_invoices(grouped=grouped, final=final, date=date)
        if not moves:
            return moves
        company = moves[0].company_id
        rounding = company.invoice_cash_rounding_id
        if rounding:
            moves.write({"invoice_cash_rounding_id": rounding.id})
        return moves
