# The company field is defined in data/ir_model_fields.xml so Apps > Import Module (ZIP)
# can install the field and company form without loading Python. Manual field names must
# use the x_ prefix (Odoo constraint). Sale order / wizard logic still requires Python
# from the addons path (registry does not load imported ZIP modules as code).
{
    "name": "Sale Invoice Cash Rounding Default",
    "summary": """
        Apply default cash rounding when invoicing sale orders.
    """,
    "author": "Mint System GmbH",
    "website": "https://www.mint-system.ch/",
    "category": "Sale",
    "version": "19.0.2.0.0",
    "license": "AGPL-3",
    "depends": ["account", "sale"],
    "data": [
        "data/ir_model_fields.xml",
        "views/res_company_views.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": ["images/screen.png"],
}
