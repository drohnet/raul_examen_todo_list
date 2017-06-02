# -*- coding: utf-8 -*-
from openerp import models, fields, api, _

EXECUTION_LEVELS=[('1','1'),
        ('2','2'),
        ('3','3'),]
        
class sub_task(models.Model):
	_inherit='hr.employee'

	execution_level = fields.Selection(EXECUTION_LEVELS, string='Level')

