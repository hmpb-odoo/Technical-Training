# -*- coding: utf-8 -*-
{
    'name': 'Cooperative Volunteers',
    
    'sumary': 'App to manage a cooperative shop',
    
    'description': """
        Cooperative Volunteers app to manage a coperative shop:
        -Volunteers
        -Shop
    """,
    
    'author': 'hmpb',
    
    'category': 'Management',
    
    'version': '0.1',
    
    'depends': ['approvals'],
    
    'license' : 'OPL-1',
    'data': [
        'security/security_volunteers.xml',
        'security/ir.model.access.csv',
        'views/volenteers_menuitems.xml',
        'views/task_views.xml',
        'views/volunteer_views.xml',
        'views/aproval_request_inherith.xml',
        'wizards/task_wizard_view.xml',
    ],
    
   'demo': [
       'demo/volunteers.xml',
   ],
    
}