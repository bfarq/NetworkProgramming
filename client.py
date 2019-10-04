import socket

# Create a socket
s = socket.socket(socket.AF_INET, socket. SOCK_STREAM)

host = '127.0.0.1'
port = 10000

# Connect to server
s.connect((host, port))
print "Connected to server"

# Receive and print message from server
print s.recv(1024)

# Close connection
s.close()
print "Connection closed"
