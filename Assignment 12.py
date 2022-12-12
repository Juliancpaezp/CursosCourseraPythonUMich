# Exploring the HyperText Transport Protocol

# You are to retrieve the following document using the HTTP protocol in a way
# that you can examine the HTTP Response headers.

# http://data.pr4e.org/intro-short.txt

# There are three ways that you might retrieve this web page and look at the
# response headers:

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()