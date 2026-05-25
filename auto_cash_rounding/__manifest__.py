{
    'name': 'Automatic Cash Rounding for Odoo',
    'version': '19.0.1.0.6',
    'summary': 'Automatic cash rounding for sales orders and invoices',
    'description': """
Advanced Cash Rounding for Odoo

This module enables automatic cash rounding for sales orders and customer invoices.

Key Features:
- Apply rounding rules on invoices
- Support for sales order rounding
- Company-level configuration
- Seamless integration with Accounting

Use Cases:
- Retail businesses handling cash payments
- Countries with rounding requirements

Easy to configure and works out-of-the-box with Odoo Accounting.
""",
    'author': 'Webanix Solutions',
    'website': 'https://webanixsolutions.com',
    'maintainer': 'Webanix Solutions',
    'category': 'Accounting',
    'depends': ['account', 'sale', 'purchase', 'stock'],
    'data': [
        'views/res_company_views.xml',
        'views/account_move_views.xml',
        'views/purchase_order_views.xml',
        'views/stock_picking_views.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}