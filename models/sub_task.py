# -*- coding: utf-8 -*-
from openerp import models, fields, api, _

class sub_task(models.Model):
    _name='sub.task.list'

    name = fields.Char(string=_('Sub task name'))
    description = fields.Text(string = _("Description"))
    sub_task_date = fields.Datetime(string=_("Task start date"))
    hour_start = fields.Float(string=_("From"), digits=(4,2))
    hour_end = fields.Float(string=_("To"), digits=(4,2))
    total_time = fields.Char(string=_("Total time"))
    consumed_hours = fields.Float(string=_("Dedicated hours"),
                                    digits=(4,2),
                                    readonly=1,
                                    compute="check_hours_dif")
    sub_task_date = fields.Datetime(string= 'Start day',
				    default = fields.Datetime.now())
    sub_task_id = fields.Many2one('todo.list.task','name')
    done = fields.Boolean(string="Done")
                        
    @api.multi
    @api.constrains("hour_start", "hour_end" )
    def _check_coherence_date(self):
        if self.hour_start > self.hour_end:
            raise exceptions.ValidationError(
                    _("Wrong hour !! Try to enter a valid hour."))
            return
    
    @api.multi
    @api.onchange('hour_start','hour_end')
    def check_hours_dif(self):
	for s in self:
	    diff = s.hour_end - s.hour_start
	    s.consumed_hours = diff


