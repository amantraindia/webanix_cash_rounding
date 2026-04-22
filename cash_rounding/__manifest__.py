{
    'name': 'Cash Rounding Odoo',
    'version': '19.0.1.0.0',
    'summary': 'Cash Rounding Odoo',
    'description': 'Cash Rounding Odoo in sales and invoices',
    'author': 'Webanix Solutions',
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