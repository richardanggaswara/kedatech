{
    'name': "test_kedatech",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['account'],

    # always loaded
    'data': [
        "security/ir.model.access.csv",
        'views/material_views.xml',
        'views/tmp_materials_data.xml',
    ],
    "installable": True,
    "auto_install": False,
    "application": True,
    # only loaded in demonstration mode
    
}