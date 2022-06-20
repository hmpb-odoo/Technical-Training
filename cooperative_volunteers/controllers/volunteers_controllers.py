# -*- coding: utf-8 -*-

from odoo import http

class Cooperative(http.Controller):
    @http.route('/cooperative/', auth='public', website=True)
    def index(self, **kw):
        return "hello, world"

    @http.route('/cooperative/volunteers/', auth='public', website=True)
    def volunteers(self, **kw):
        volunteers = http.request.env['volunteer.volunteer'].search([])
        return http.request.render('cooperative_volunteers.volunteers_website', {
            'volunteers': volunteers,
        })

    @http.route('/cooperative/<model("volunteer.task"):tasks>/', auth='public', website=True)
    def tasks(self, tasks):
        return http.request.render('cooperative_volunteers.task_website', {
            'task': tasks,
        })