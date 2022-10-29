py_script='''
import socket	
import sys
import server_procedures as sp
from inspect import signature
		
s = socket.socket()		
port = 8888			
s.bind(('', port))		
s.listen(5)		

while True:
    c, addr = s.accept()	
    receive_str = c.recv(1024).decode()
    if(receive_str == "DISCONNECT"):
        response = "Type of argument not matching"
        c.sendall(response.encode())

    else:
        receive_list = receive_str.split('$')

        try: 
            response = ""
            length = ""

            code = 'length = len(signature(sp.' + receive_list[0] + ').parameters)'
            exec(code)

            if length == (len(receive_list)-1)/2:
            
                code = 'response = sp.' + receive_list[0] + '('
                
                for i in range(1, len(receive_list)-1, 2):
                    if receive_list[i+1] == "string":
                        code += '"' + receive_list[i] + '"' + ','
                    else:
                        code += receive_list[i] + ',' 
                code = code[0:len(code)-1]
                code += ')'
                exec(code)
                response = str(response)
                
            else:
                response = "Arguments not matched!"

        except AttributeError:
            response = "No such function exists"

        c.sendall(response.encode())
    c.close()
    
'''
file = open('rpc_server.py','w')
file.write(py_script)
file.close()