# -*- coding: utf-8 -*-
{
    'name': "ward room",
    'summary': "room for hospital",
    'application': True,
    'license': 'LGPL-3',


    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base','hospital'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/room_patient_views.xml',
        'views/room_round_views.xml',
        'views/menu_views.xml',
    ],
}

