# © <{{cookiecutter.year}}> <{{cookiecutter.author}}>
{
    'name': '{{cookiecutter.module_verbose_name}}',
    'version': '{{cookiecutter.odoo_version}}.0.0.1',

    'summary': '{{cookiecutter.module_verbose_name}}',

    'category': '{{cookiecutter.category}}',
    'website': '{{cookiecutter.website}}',
    'author': '{{cookiecutter.author}}, iCode',
    'auto_install': False,
    'installable': True,

    'depends': [
        # Odoo standard modules
        'base',

        # third party modules
        # 'oca_timesheet',

        # our modules
        # 'tms_modifications_icode',
    ],
    'data': [
        # security
        # 'security/security.xml',
        # 'security/ir.model.access.csv',

        # data
        # 'data/ir_sequence_data.xml',

        # reports

        # config
        # 'views/res_config_settings_views.xml',

        # assets
        # 'views/assets.xml',

        # views
        # 'views/account_move_views.xml',

        # wizard

        # menus
        # 'views/menus.xml',

    ],
    'demo': [

    ],
    'qweb': [

    ],
    'external_dependencies': {
        'python': [

        ],
    }

}
