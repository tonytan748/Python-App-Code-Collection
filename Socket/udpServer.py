import socket

HOST='127.0.0.1'
PORT=50001
BUFFER=4096

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((HOST,PORT))

print 'udpServer listen at: %s:%s\n\r' % (HOST,PORT)

while True:
	recv,client_addr=sock.recvfrom(BUFFER)	
	if not recv:
		break
	print '[Client %s : %s said]: %s' % (client_addr[0],client_addr[1],recv)
	sock.sendto('udpServer has received your message.',client_addr)
cock.close()
