import socket
import datetime

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0',9992))
sock.listen(5)
while True:
    print("lytter")
    conn,addr = sock.accept()
    print("Connection from " +str(addr))
    #conn.send("Hello World\n".encode('utf-8'))
    line = conn.recv(1024).decode("utf-8")    
    if line == 'hej':
        print(line + ' 1')
        conn.send("goddaw".encode('utf-8'))
    elif line == 'klokken':
        print(line + ' 2')
        klokken = datetime.now()
        conn.send("Klokken er "+klokken.encode('utf-8'))
    elif line == 'øl':
        print(line +' 3')
        conn.send("knap den op ".encode('utf-8'))
    elif line == 'farvel':
        print(line+' 4')
        conn.send('lukketid'.encode('utf-8'))
        break
    conn.close()

