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
    
    task_id = execute('todo.list.task', 'search', ())
    for task in task_id:
        print task
    
        
        
    #~ decoded = json.loads(encoded)
    #~ print "#### EL RESULTADO CODIFICADO >>>> ", encoded
    #~ print "#### EL RESULTADO DECODIFICADO >>>> ", decoded
