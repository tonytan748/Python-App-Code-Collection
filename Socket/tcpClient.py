import socket

HOST='127.0.0.1'
PORT=15339
BUFFER=4096

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect((HOST,PORT))
sock.send('hello, tcpServer')
recv=sock.recv(BUFFER)
print '[tcpServer said]: %s' % recv
sock.close()
