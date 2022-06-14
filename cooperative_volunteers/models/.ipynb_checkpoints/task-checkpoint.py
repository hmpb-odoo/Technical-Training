# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Task(models.Model):
    _name = 'volunteer.task'
    _description = 'Task info'
    
    name = fields.Char(string='Task', required=True)
    description = fields.Text(string='Description')
    
    start_date = fields.Datetime(string = 'Start date')
    end_date = fields.Datetime(string = 'End date')
    
    frecuency = fields.Selection(string="Frecuency",
                                selection=[
                                    ('never', 'Never'),
                                    ('daily', 'Daily'),
                                    ('once a week', 'Once a week'),
                                    ('twice a week', 'Twice a week'),
                                    ('once a month', 'Once a month'),
                                    ('twice a month', 'Twice a month'),
                                ])
    active = fields.Boolean(string = 'Active')