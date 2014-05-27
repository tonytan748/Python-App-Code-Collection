from socket

HOST='127.0.0.1'
PORT=50001
BUFFER=4096

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.connect((HOST,PORT))
sock.send('hello udpServer!')
recv=sock.recv(BUFFER)
print '[udpServer said]: %s' % recv
sock.close()
