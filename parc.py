# -*- coding: utf-8 -*-
from openerp import models, fields


class user(models.Model):
    _name = 'parc.user'
    _rec_name = 'lastname'
    firstname = fields.Char('FirstName', required=True)
    lastname = fields.Char('LastName', required=True)
    machine_ids = fields.One2many('parc.machine', 'user_id', 'Machines')


class machine(models.Model):
    _name = 'parc.machine'
    title = fields.Char('Title', required=True)
    genre = fields.Char('Genre', required=True)
    user_id = fields.Many2one('parc.user', 'User', ondelete='cascade')