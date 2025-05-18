# -*- coding: utf-8 -*-
{
    'name': "Byc Web Widgets",

    'summary': """
       """,

    'description': """

    """,

    'author': "Bytecode Bolivia",
    'website': "http://www.bytecodebo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Web',
    'version': '16.0.1.0.1',
    'license': 'LGPL-3',
    # any module necessary for this one to work correctly
    'depends': [

        'web_tree_dynamic_colored_field',
        'web_tree_many2one_clickable',
        'web_action_conditionable',
        'web_chatter_position',
        'web_domain_field',
        'web_environment_ribbon',
        'web_listview_range_select',
        'web_notify',
        'web_refresher',
        'web_field_numeric_formatting',

        # 'base_float_dynamic_field',
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
       #  'security/ir.model.access.csv',
       #  'views/model_test_base_views.xml',
       #  'views/model_test_views.xml',
       #  'views/menu_items.xml'
    ],
    'assets': {
        # 'web.assets_frontend': [
        #     'byc_web_settings/static/src/scss/login.scss',
        # ],
        'web.assets_backend': [
            ##     'byc_web_settings/static/src/scss/primary_variables.scss',
            #'byc_web_widget_fullscreen/static/src/css/fullscreen.css',
            #'byc_web_widget_fullscreen/static/src/js/fullscreen-widget.js',
        ],
        'web.assets_qweb': [
            ##    ('remove', 'web/static/src/legacy/**/*.xml'),
            ##    'web/static/src/legacy/xml/base.xml',
            #'byc_web_widget_fullscreen/static/src/xml/fullscreen_widget.xml',
        ],
        'web._assets_common_scripts': [
            ## 'web/static/lib/underscore/underscore.js',
            ##'byc_web_widget_fullscreen/static/lib/fullscreen-widget/fullscreen-jquery.js',
            #'byc_web_widget_fullscreen/static/lib/jquery-fullscreen/jquery.fullscreen.js',
        ]
    },
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
