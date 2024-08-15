# __manifest__.py

{
    'name': 'AB Test Module',
    'version': '1.0',
    'category': 'Uncategorized',
    'summary': 'A module to demonstrate a simple test in Odoo',
    'description': """
        This is a test module to demonstrate how to create a simple test in Odoo.
    """,
    'author': 'Your Name',
    'depends': ['base'],
    'data': [
            'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': False,
}
