import sys
py_script='''
import socket	
import json	
import sys	

port = 8888
filename = "'''
py_script += sys.argv[1]
py_script += '''"


s = socket.socket()

type_dict = {'str': str, 'int': int, 'float': float}

def main():
    f = open(filename)
    data = json.load(f)
    for i in data['remote_procedures']:
        py_script = f"""
    def {i['procedure_name']}(self, *args):
        arg_list = []
        for i in range(len(args)):
            arg_list.append(args[i])
        return self.execute("{i['procedure_name']}", arg_list)
        """
        file = open('rpc_client.py','a')
        file.write(py_script)
        file.close()

if __name__ == "__main__":
    main()
    
class clientRPC:

    def __init__(self):
        
        s.connect(('127.0.0.1', port))

    def execute(self, name, arg_list):

        quit_flag=0
        f = open(filename)
        data = json.load(f)
        for i in data['remote_procedures']:
            out_str = ""
            if i['procedure_name'] == name:
                out_str += i['procedure_name'] + "$"
                
                for j in range(len(arg_list)):
                    out_str += str(arg_list[j]) + "$"
                    try:
                        if type(arg_list[j]) is type_dict[i['parameters'][j]['data_type']]:
                            out_str += i['parameters'][j]['data_type'] + "$"
                        else:
                            quit_flag=1
                    except:
                        break
        
                if quit_flag==1:
                    out_str = "DISCONNECT"
                    s.sendall(out_str.encode())
                    return s.recv(1024).decode()
                    sys.exit()
                    
                out_str = out_str[0:len(out_str)-1]
                s.sendall(out_str.encode())
                return s.recv(1024).decode()
                
        f.close()
        
    
        
'''
file = open('rpc_client.py','w')
file.write(py_script)
file.close()

exec(open('rpc_client.py').read())