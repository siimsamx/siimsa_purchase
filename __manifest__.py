# -*- coding: utf-8 -*-
{
    'name': "Requisición de compra",

    'summary': """
        SIIMSA S.A. de C.V.""",

    'description': """
        Requisición de compra, SIIMSA S.A. de C.V.
    """,

    'author': "Alan Cortés",
    'website': "http://www.siimsa.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Compras',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'board', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
		'views/partner.xml',
		'views/list_activity.xml',
		'report/list_activity.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}