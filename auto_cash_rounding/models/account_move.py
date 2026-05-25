from odoo import models


class AccountMove(models.Model):
    _inherit = "account.move"

    def _auto_cash_rounding_documents(self):
        return self.filtered(
            lambda move: move.move_type
            in ("out_invoice", "in_invoice", "out_refund", "in_refund")
        )

    def _apply_company_cash_rounding(self):
        for move in self._auto_cash_rounding_documents():
            rounding = move.company_id.invoice_cash_rounding_id
            if rounding and not move.invoice_cash_rounding_id:
                move.invoice_cash_rounding_id = rounding
        return True

    def action_post(self):
        self._apply_company_cash_rounding()
        return super().action_post()
