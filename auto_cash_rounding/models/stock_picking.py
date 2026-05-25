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

    @api.depends(
        "name",
        "origin",
        "picking_type_id",
        "picking_type_id.name",
        "picking_type_id.code",
        "location_id",
        "location_id.name",
        "location_dest_id",
        "location_dest_id.name",
    )
    def _compute_is_cash_rounding_scrap_picking(self):
        for picking in self:
            picking_type = picking.picking_type_id
            locations = picking.location_id | picking.location_dest_id
            has_scrap_location = any(
                (
                    ("is_scrap_location" in location._fields and location.is_scrap_location)
                    or ("scrap_location" in location._fields and location.scrap_location)
                    or "scrap" in (location.display_name or location.name or "").lower()
                )
                for location in locations
            )
            document_text = " ".join(
                value
                for value in (
                    picking.name or "",
                    picking.origin or "",
                )
                if value
            ).lower()
            picking.is_cash_rounding_scrap_picking = bool(
                has_scrap_location
                or (
                    picking_type
                    and (
                        picking_type.code == "scrap"
                        or "scrap" in (picking_type.name or "").lower()
                    )
                )
                or "scrap" in document_text
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
