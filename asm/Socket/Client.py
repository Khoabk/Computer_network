from socket import *

import time


serverName = '192.168.1.69'
serverPort = 2001
clientPort = 40119

clientSocket =  socket(AF_INET, SOCK_DGRAM)

clientSocket.bind(('',clientPort))


# clientSocket.bind(('',clientPort))
#
#
# sth = clientSocket.connect((serverName,serverPort))
#
# print(sth)

#
# message = input('Input something: ')
#
#
# clientSocket.sendto(message.encode(),(serverName,serverPort))

clientSocket.settimeout(2)
start = time.time()

while True:

    if time.time() - start > 10:
        print(time.time() - start)
        break
#
# try:
#     clientSocket.recvfrom(256)
# except:
#     print(time.time() - start)
#     print("timeout")



#while True:

#    clientSocket.sendall(str.encode(message))



    # message = input('Input something: ')
    #
    # clientSocket.sendto(message.encode(),(serverName,serverPort))
    #
    # message, serverAddress = clientSocket.recvfrom(1024)
    #
    # print(message.decode())


    #
    # if message.decode() == "-1\n":
    #     break
    #
    # message = input('Input something: ')
#
# message = clientSocket.recv(1024)
#
# print(message.decode())
#
# clientSocket.close()
