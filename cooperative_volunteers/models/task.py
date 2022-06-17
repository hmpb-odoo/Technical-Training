# -*- coding: utf-8 -*-

from unittest.loader import VALID_MODULE_NAME
from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

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

    state = fields.Selection(string="State",
                            selection=[
                                ('draft', 'Draft'),
                                ('ready', 'Ready'),
                                ('in progress', 'In progress'),
                                ('done', 'Done'),
                            ], default='draft')

    leader = fields.Many2one(comodel_name='volunteer.volunteer',
                                    string='leader')

    volunteer_ids = fields.Many2many(comodel_name='volunteer.volunteer',
                                    string='Volunteer')

    request_approvals_id = fields.One2many(comodel_name='approval.request',
                                    inverse_name='task_id',
                                    string='Request aprobals')
    


    @api.onchange('leader')
    def _onchanchange_leader(self):
        if(self.leader == ''):
            raise UserError('Leader is required')
        self.state = 'done'


