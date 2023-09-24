import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
 
server_socket.bind(("",80))
server_socket.listen(5)
 
while True:
    connection_object, address = server_socket.accept()
    print("Client information = {}".format(address))
    
    msg = "Thank you for getting connected"
    connection_object.send(msg.encode())
    
    connection_object.close()
    break
 