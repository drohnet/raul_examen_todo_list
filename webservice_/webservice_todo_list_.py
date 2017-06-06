from SimpleXMLRPCServer import SimpleXMLRPCServer
import xmlrpclib
import json

HOST='localhost' 
PORT=8069

DB='adivet_test_v1' 
USER='admin'
PASS='hiphop35'
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
    
    for count in range(1):
    
        values = {'name': "PHP Tarea %d" % (count),
                  'task_lvl': '1',
                  'state':'draft',
        }
        values_encoded = json.dumps(values, ensure_ascii=False)
        result = execute('todo.list.task', 'create_from_web_service', values_encoded)
        #task_id = execute('todo.list.task', 'search', ())
        #~ if result:
            #~ print "#### La tarea creada es: >>>> ", result
        
        for count_2 in range(3):
            values_sub = {
                          'name': "PHP SubTarea %d" % (count_2),
            }
            
            values_encoded_sub = json.dumps(values_sub, ensure_ascii=False)
            result_sub = execute('sub.task.head', 'create_from_web_service', values_encoded_sub)
        
            if result_sub:        
                print "#### La subtarea creada es: >>>> ", result_sub
            else:
                print "### No se puedo crear la subtarea ###"
    
        #~ else:
            #~ print "### No se puedo crear la tarea ###"
        
        
    #decoded = json.loads(encoded)
    #print "#### EL RESULTADO CODIFICADO >>>> ", encoded
    #print "#### EL RESULTADO DECODIFICADO >>>> ", decoded
