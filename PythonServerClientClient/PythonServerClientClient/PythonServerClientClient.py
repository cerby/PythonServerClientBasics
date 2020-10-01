import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost',9992)
print('connecting to '+str(server_address))
sock.connect(server_address)

while True:
    print('skriv besked ')
    message = sys.stdin.readline()
    sock.sendall(message.encode('utf-8'))
    data = sock.recv(1024)
    print('Received '+data.decode('utf-8'))