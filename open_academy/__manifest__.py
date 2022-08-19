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
        'security/ir.model.access.csv',
        'views/open_academy_views.xml',
        'views/session_views.xml',
        'views/course_views.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
