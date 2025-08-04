# -*- coding: utf-8 -*-
{
    'name': "Devansh Insurance Broking",

    'summary': 
    """Devansh Insurance Broking Internal Software""",

    'description': """
        Devansh Insurance Broking Internal Software
    """,

    'author': "Devansh Insurance Broking",
    "application": True,
    # 'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','contacts'],
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'icon': 'devansh_insurance/static/img/icon.png',
}
