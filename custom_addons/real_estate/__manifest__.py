# -*- coding: utf-8 -*-
{
    'name': "Real Estate",
    'installable': True,
    'application': True,
    'license': 'LGPL-3',

    'summary': "my first module",

    'description': """
Long description of module's purpose
    """,
    'author': "My Company",
    'website': "https://www.yourcompany.com",


'category': 'Sales',
    'version': '0.1',

    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_menus.xml'
    ],
    'demo': [
        'demo/demo.xml',
    ],
}