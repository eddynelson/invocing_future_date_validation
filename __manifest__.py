# -*- coding: utf-8 -*-
{
    'name': "invocing_future_date_validation",

    'summary': """validate future date in invocing""",

    'description': """validate future date in invocing""",

    'author': "eddynelson02@gmail.com",
    'website': "http://www.invocing.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account', 'account_invoicing'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
