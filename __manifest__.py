# -*- coding: utf-8 -*-
{
    'name': "Export Sales Data",

    'summary': """
        Export Data from Sales addons and POS    
    """,

    'description': """
        Export all information of Sales and POS addons
    """,

    'author': "YnievesDotNet",
    'website': "https://ynievesdotnet.github.io",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales/Point Of Sale',
    'version': '13.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'point_of_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'wizards/export_sales_data.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
}
