
import socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
local ='127.0.0.1'
print(host)
client.connect((host,1055)) 
msg = ' I connect！'  
client.send(msg.encode('utf-8'))  
data = client.recv(1024) 
print('recv:',data.decode()) 
client.close() 
