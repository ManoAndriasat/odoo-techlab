# -*- coding: utf-8 -*-
{
    'name': "hospital",

    'summary': "Main module for managing hospital operations",
    'application': True,
    'Installable': True,
    'version': '1.0',
    'sequence': 1,
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

    # any module necessary for this one to work correctly
    'depends': ['base','product'],

    # always loaded
    'data': [
        'data/groups.xml',
        'data/hospital_security.xml',
        'security/ir.model.access.csv',
        'views/hospital_consultation_views.xml',
        'views/hospital_disease_views.xml',
        'views/hospital_doctor_views.xml',
        'views/hospital_medication_views.xml',
        'views/hospital_nurse_views.xml',
        'views/hospital_patient_record_views.xml',
        'views/hospital_patient_views.xml',
        'views/menu_views.xml',
    ],
}

