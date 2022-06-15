# -*- coding: utf-8 -*-

import string
from odoo import models, fields, api

class Volunteer(models.Model):
    _name = 'volunteer.volunteer'
    _description = 'Volunteer info'
    volunteer_id = fields.Many2one(comodel_name='res.partner', string='Volunteer')
    name = fields.Char(string='Volunteer_name', related='volunteer_id.name')