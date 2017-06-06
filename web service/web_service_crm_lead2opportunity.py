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
   
   
   
    lead_ids = execute('crm.lead', 'search', [('type', '=', 'lead'),('php_lead_id', '>', 0)])
    if lead_ids:
        result = execute('crm.lead', 'convert_opportunity', lead_ids, 7)
   
    if result:        
        print "#### El resultado de la operacion es: >>>> ", result
    else:
        print "### Hubo un error al convertir las iniciativas ###"

        
    #decoded = json.loads(encoded)
    #print "#### EL RESULTADO CODIFICADO >>>> ", encoded
    #print "#### EL RESULTADO DECODIFICADO >>>> ", decoded
