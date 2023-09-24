#client create
 
import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 80
ip = "127.0.0.1"
 
client_socket.connect((ip,port))
msg2 = client_socket.recv(1024)
print("{}".format(msg2.decode()))
client_socket.close()