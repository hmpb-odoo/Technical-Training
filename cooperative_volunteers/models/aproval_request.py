# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AprovalRequest(models.Model):
    _inherit = 'approval.request'

    task_id = fields.Many2one(comodel_name='volunteer.task', 
                                string='Related task',
                                ondelete= 'set null')
                                
    leader_id = fields.Many2one(string="Leader task",
                                related="task_id.leader")

    volunteer_ids = fields.Many2many(string="Volunteers",
                                    related="task_id.volunteer_ids")
