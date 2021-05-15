
import socket
global port
global host
host="192.168.100.32"
port=9999

s=socket.socket()

s.connect((host,port))

while True:
    i=str.encode("Hellow")
    s.send(i)
    data=s.recv(900000)
    print(data)
s.close()