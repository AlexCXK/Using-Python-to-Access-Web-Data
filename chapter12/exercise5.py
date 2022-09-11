# Exercise 5: (Advanced) Change the socket program so that it only shows
# data after the headers and a blank line have been received. Remember
# that recv receives characters (newlines and all), not lines.

import socket

try:
    #url = input('Enter a URL: ').lower()
    url = 'http://data.pr4e.org/romeo.txt'
    domain = url.split("/")[2]
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((domain, 80))
    cmd = ('GET ' + url + ' HTTP/1.0\r\n\r\n').encode()
    mysock.send(cmd)
    bData = b''
    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        bData += data
    mysock.close()
    content = (bData.split(b'\r\n\r\n')[1]).decode()
    print(content)

except:
    print("an improperly formatted or non-existent URL")
