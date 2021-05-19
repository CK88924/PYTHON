import sys
import socket
# 建立server
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
print(host)
server.bind((host,1025)) #绑定ip port
server.listen(5) 
while True:
    conn,addr = server.accept() 
    print("客戶端ip:",addr)
    data = conn.recv(1024)  #接收
    print('recive:',data.decode()) 
    conn.send(str.encode('server is ok')) #發送
    conn.close()
