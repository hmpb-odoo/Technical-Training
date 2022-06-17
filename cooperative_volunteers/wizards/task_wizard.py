# -*- coding: utf-8 -*- 
from odoo import models, fields, api
class TaskWizard(models.TransientModel):
    _name = 'volunteer.wizard'
    _description = 'Wizard: Quick add task for volunteer'

    volunteers_ids = fields.Many2one(comodel_name='volunteer.volunteer', string='Volunteers', required=True)

    volunteers_tasks_id = fields.Many2many(comodel_name='volunteer.task', string='Tasks', related='volunteers_ids.tasks_ids')

    tasks_id = fields.Many2many(comodel_name='volunteer.task', string='Tasks abiables')


    def add_volunteer_tasks(self):
        for volunteer in self.volunteers_ids:
            volunteer.tasks_ids |= self.tasks_id
        return True





    