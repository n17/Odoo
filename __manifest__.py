{
    'name': "partner_company_code",

    'summary': """
        Adds a "company_code" field to the "res.partner" data model.""",

    'description': """
         The purpose of this module is to add a new Char field called "company_code" –
meant for the company registration identification number – on the "res.partner" data model.
The field is also added to the customer / partner form.
    """,

    'author': "Oskars Zālītis",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/partner.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}
