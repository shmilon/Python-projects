# server create
 
import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
 
server_socket.bind(("",12345))
server_socket.listen(5)
 
while True:
    connection_object, address = server_socket.accept()
    print("Client information = {}".format(address))
    
    msg = "Thank you for getting connected"
    connection_object.send(msg.encode())
    
    connection_object.close()
    break
 
 
#client create
 
import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12346
ip = "127.0.0.1"
 
client_socket.connect((ip,port))
msg2 = client_socket.recv(1024)
print("{}".format(msg2.decode()))
client_socket.close()
