# -*- coding: utf-8 -*-
{
    'name': "Doc Consulting",
    'version': '0.1',
    
    'application': True,
    'installable': True,
    'license': 'AGPL-3',

    'summary': "Short (1 phrase/line) summary of the module's purpose",

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
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/doc_consulting_patient.xml',
        'views/doc_consulting_drug.xml',
        'views/doc_consulting_doctor.xml',
        'views/doc_consulting_consultation.xml',
        'views/doc_consulting_menus.xml',
        'report/doc_consulting_reports.xml',
        'report/doc_consulting_templates.xml',              
    ],
}

