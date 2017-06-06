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
    
    for count in range(10):
    
        values = {'name': "PHP Lead %d" % (count),
                  'php_lead_id': count, 
                  'product_category_id':9,
                                
        }
                
        values_encoded = json.dumps(values, ensure_ascii=False)
        result = execute('crm.lead', 'create_from_web_service', values_encoded)
        
        if result:        
            print "#### La iniciativa creada es: >>>> ", result
        else:
            print "### No se puedo crear la iniciativa ###"
        
    #decoded = json.loads(encoded)
    #print "#### EL RESULTADO CODIFICADO >>>> ", encoded
    #print "#### EL RESULTADO DECODIFICADO >>>> ", decoded
