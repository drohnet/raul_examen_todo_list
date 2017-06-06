# -*- coding: utf-8 -*-
from datetime import timedelta
from openerp import models, fields, api, _, exceptions
import json

def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError, e:
        return False            
    return True

class todo_list_task(models.Model):
    _name='todo.list.task'
    
    name = fields.Char(string='Task Name', required=True)
    
    state = fields.Selection([('draft', 'Draft'),
                            ('in_process', 'in process'),
                            ('done', 'Done')],
                            default='draft')
    subtask_head_ids = fields.One2many('sub.task.head', 'name', string='Sub task')
    task_lvl = fields.Selection([('1', '1'),
                                ('2', '2'),
                                ('3', '3'),])
    employee_id = fields.Many2one('hr.employee', string = "Employee")
    start_datetime=fields.Datetime(string= 'Start day',
                                    default = fields.Datetime.now())
    end_datetime = fields.Datetime(string = 'End day',)
    total_days = fields.Char(string= 'Total days',
                                readonly=1,
                                compute="check_dates_dif")

    @api.multi
    def action_draft(self):
        self.state='draft'
    @api.multi
    def action_cancel(self):
        self.state='cancel'
    @api.multi
    def action_in_process(self):
        print "><"
        self.state= 'in_process'
    @api.multi
    def action_done(self):
        self.state='done'
	
    @api.multi
    @api.constrains("start_datetime", "end_datetime" )
    def _check_coherence_date(self):
	if self.start_datetime and self.end_datetime:
	    if self.start_datetime > self.end_datetime:
		raise exceptions.ValidationError(
			_("Wrong date !! Try to enter a valid date."))
		return
	
    @api.multi
    @api.onchange('start_datetime','end_datetime')
    def check_dates_dif(self):
	self.ensure_one()
	if self.start_datetime and self.end_datetime:
	    date_end = fields.Datetime.from_string(self.end_datetime)
	    date_start = fields.Datetime.from_string(self.start_datetime)
	    diff = date_end - date_start
	    if date_end >= date_start:
		self.total_days = str(diff.days)
	    return
        
    @api.model
    def create_from_web_service(self,vals):
        res = {}
        if vals and is_json(vals): 
                       
            vals_decode = json.loads(vals)
                                    
            if vals_decode.get('name', False):
                res = self.create(vals_decode)
        return res
