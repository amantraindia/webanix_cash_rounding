{
    'name': 'Cash Rounding Odoo',
    'version': '19.0.1.0.0',
    'summary': 'Default cash rounding in sales and invoices',
    'description': 'Automatically applies cash rounding in orders and invoices.',
    'author': 'Your Company',
    'category': 'Accounting',
    'depends': ['account', 'sale'],
    'data': [
        'views/res_company_views.xml',
        'data/ir_model_fields.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}