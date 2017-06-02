# -*- coding: utf-8 -*-
{
    'name': "todo_list_raul",

    'summary': """ """,
        
    'description': """
        This module will be todo list
    """,

    'author': "Raul Abejon",
    'website': "none",
    'category': 'Sales',
    'version': '0.1',
    'depends': ['base','hr','hr_timesheet_sheet'],
    'data': [
		#'security/ir.model.access.csv',
		#'workflow/todo_list_workflow.xml',
		'views/todo_list_form_view.xml',
		'views/todo_list_tree_view.xml',
		'views/todo_list_task_employee_tree_views.xml',
		'views/todo_list_task_list_employee_form_view.xml',
        'views/todo_list_menu_view.xml',
    ],
}
