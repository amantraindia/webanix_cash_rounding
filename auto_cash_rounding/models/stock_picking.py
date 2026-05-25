from odoo import api, fields, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    cash_rounding_id = fields.Many2one(
        "account.cash.rounding",
        string="Cash Rounding",
        copy=False,
        help="Company cash rounding method captured when validating scrap receipts.",
    )
    is_cash_rounding_scrap_picking = fields.Boolean(
        string="Scrap Picking",
        compute="_compute_is_cash_rounding_scrap_picking",
    )

    @api.depends("picking_type_id", "picking_type_id.name", "picking_type_id.code")
    def _compute_is_cash_rounding_scrap_picking(self):
        for picking in self:
            picking_type = picking.picking_type_id
            picking.is_cash_rounding_scrap_picking = bool(
                picking_type
                and (
                    picking_type.code == "scrap"
                    or "scrap" in (picking_type.name or "").lower()
                )
            )

    def _apply_company_cash_rounding(self):
        for picking in self.filtered("is_cash_rounding_scrap_picking"):
            rounding = picking.company_id.invoice_cash_rounding_id
            if rounding and not picking.cash_rounding_id:
                picking.cash_rounding_id = rounding
        return True

    def button_validate(self):
        self._apply_company_cash_rounding()
        return super().button_validate()
