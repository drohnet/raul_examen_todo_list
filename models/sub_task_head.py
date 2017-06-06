# -*- coding: utf-8 -*-
from openerp import models, fields, api, _

class sub_task_head(models.Model):
    _name='sub.task.head'

    name = fields.Char(string=_('Sub task name'))
    sub_task_done = fields.Boolean(string=_('task done'))
    subtask_ids = fields.One2many('sub.task.list', 'name', string='Sub task')
    task_id = fields.Many2one('todo.list.task','name')
