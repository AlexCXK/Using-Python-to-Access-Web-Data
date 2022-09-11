# Exercise 2: Change your socket program so that it counts the number
# of characters it has received and stops displaying any text after it has
# shown 3000 characters. The program should retrieve the entire docu-
# ment and count the total number of characters and display the count
# of the number of characters at the end of the document.
# http://data.pr4e.org/mbox-short.txt for test


import socket

try:
    url = input('Enter a URL: ').lower()
    domain = url.split("/")[2]
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((domain, 80))
    cmd = ('GET ' + url + ' HTTP/1.0\r\n\r\n').encode()
    mysock.send(cmd)
    dataTotal = ''
    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break

        dataTotal += data.decode()
    mysock.close()

    print(dataTotal[:3000])
    print(len(dataTotal[:3000]))
except:
    print("an improperly formatted or non-existent URL")
