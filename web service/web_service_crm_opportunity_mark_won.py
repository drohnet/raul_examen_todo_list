from SimpleXMLRPCServer import SimpleXMLRPCServer
import xmlrpclib
import json

HOST='localhost' 
PORT=8069

DB='konectia_desarrollo_new_api' 
USER='admin'
PASS='odoo'
url = 'http://%s:%d/xmlrpc/' % (HOST,PORT)

common_proxy = xmlrpclib.ServerProxy(url+'common') 

object_proxy = xmlrpclib.ServerProxy(url+'object')

def execute(*args): 
    return object_proxy.execute(DB,uid,PASS,*args)

uid = common_proxy.login(DB,USER,PASS)
if not uid:
    print "No se pudo realizar el inicio de sesion"    
else:
    print "LogIn como  %s (uid:%d)" % (USER,uid)
    
    #self.env['crm.case.stage'].search(['|','&',('probability', '>', 0),('probability','<', 100),('sequence','=',1)])
    stage_ids = execute('crm.case.stage', 'search', ['|','&',('probability', '>', 0),('probability','<', 100),('sequence','=',1)])
    
    if stage_ids:
        #_logger.info('------------STAGE IDS------------')
        #_logger.info(stage_ids)
        
        #lead_ids = self.env['crm.lead'].search([('type','=','opportunity'), ('product_category_id', '!=', False),('stage_id','in', stage_ids)])
        lead_ids = execute('crm.lead', 'search', [('type','=','opportunity'), ('product_category_id', '!=', False),('stage_id','in', stage_ids)])
        
        result = execute('crm.lead','case_mark_won', lead_ids)
    
    if result:        
        print "#### El resultado de la operacion es: >>>> ", result
    else:
        print "### Hubo un error al convertir las iniciativas ###"
