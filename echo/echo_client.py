"""
echo client, usage:

 python echo_client.py <host> <port>

Both host and port are optional, defaults: localhost 50000
host must be present if you want to provide port
"""
import socket
import sys

def send_chat():
    s = socket.socket(socket.AF_INET,
                      socket.SOCK_STREAM)
    s.connect((host,port))
    s.send(chat)

    data = s.recv(size)
    s.close()
    print 'from (%s,%s) %s' % (host, port, data)


host = 'localhost' 
port = 50000 
size = 1024
chat = ''

nargs = len(sys.argv)
if nargs > 1:
    chat = sys.argv[1]
if nargs > 2:
    port = int(sys.argv[2])
if nargs > 3:
    host = sys.argv[3]

if (chat):
    send_chat()
else:
    print 'Please enter a message'
    chat = raw_input('--> ')
    send_chat()

