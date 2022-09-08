from socket import *

serverIP = '192.168.1.69'

serverPort = 2001

serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('', serverPort))
#
# serverSocket.listen()
#
# conn, addr = serverSocket.accept()
#
# print("Connection established\n")
#
# print("Client information\n")
#
# print(addr)


while True:
    message, clientAddress = serverSocket.recvfrom(1024)

    # if data.decode() == "-1":
    #     message = "-1\n"
    #     conn.sendall(str.encode(message))
    #     conn.sendall(b"Close connection\n")
    #     break

    serverSocket.sendto(message,clientAddress)

    print(message.decode())





#
#
#
#
# #print ("The server is ready to receive")
# while 1:
#     message, clientAddress = serverSocket.recvfrom(2048)
#
#     print(clientAddress)
#
#     print(message.decode())
#
#     modifiedMessage = message.upper()
#
#     serverSocket.sendto(modifiedMessage, clientAddress)
#
#     end = input("End program?")
#
#     if end == "end":
#         message = "Server has shut down\n"
#         serverSocket.sendto(str.encode(message), clientAddress)
#         break
