{
    'name': "open_academy",

    'summary': "Module objective is to create test courses",

    'description': "This is a test module for an Open Academy Courses",

    'author': "Odoo Community Association (OCA)",
    'website': "http://www.yourcompany.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/course_view_form.xml',
        'views/course_view_search.xml',
        'views/course_action.xml',
        'views/sessions_action.xml',
        'views/course_menu.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
