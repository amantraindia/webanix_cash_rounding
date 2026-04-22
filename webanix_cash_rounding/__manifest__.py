{
    'name': 'Cash Rounding Odoo',
    'version': '19.0.1.0.0',
    'summary': 'Cash Rounding Odoo',
    'description': 'Cash Rounding Odoo in sales and invoices',
    'author': 'Webanix Solutions',
    'category': 'Accounting',
    'depends': ['account', 'sale'],
    'data': [
        'data/ir_model_fields.xml',
        'views/res_company_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}