
import socket
store=[]
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
client.connect(('www.google.com',80)) 
msg = ' I connect！'  
client.send(msg.encode('utf-8'))

while True:
    data = client.recv(1024) 
    if data:
        
        store.append(data)
        
        
    else:
        break
client.close()

print(store,'\n')

