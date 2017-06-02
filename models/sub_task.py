# -*- coding: utf-8 -*-
from openerp import models, fields, api, _

class sub_task(models.Model):
	_name='sub.task.list'
	
	name = fields.Char(string='Task Name')
	description = fields.Text(string = "Description")
	sub_task_done = fields.Boolean(string='task done')
	task_date = fields.Datetime(string="Task date")
	do_it = fields.Boolean(string="Done ?")

