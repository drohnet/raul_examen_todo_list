# -*- coding: utf-8 -*-
from openerp import models, fields, api, _

STATES=[('draft','Draft'),
        ('confirmed','Confirmed'),
        ('cancel','Cancel'),]

class todo_list_task(models.Model):
	_name='todo.list.task'
	
	name = fields.Char(string='Task Name')
	employee_id = fields.Many2one('hr.employee', string = "Employee")
	#states = fields.Selection(STATES, string='state', required=False),
	task_date = fields.Datetime(string="Task date")
	subtask_ids = fields.One2many('sub.task.list', 'name', string='Sub task')
	
	
	
	
	def action_draft(self):
		self.state='draft'
	
	def action_cancel(self):
		self.state='cancel'

	def action_confirmed(self):
		self.state= 'confirmed'
