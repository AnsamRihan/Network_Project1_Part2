from socket import *

print('--------------------------------------------------------------\n'
      '\t\t\t\t\tClient Side configuraion\n--------------------------------------------------------------')
serverName = '192.168.1.6' #IP changes to the one on ur device with ur internet connection
serverPort = 9955 #identifying the server port to send packets to
clientSocket = socket(AF_INET, SOCK_STREAM) #TCP connection
clientSocket.connect((serverName,serverPort)) #connection made
sentence = input('Input student ID:')  #get id
clientSocket.send(sentence.encode()) #send to server
ResponseSentence = clientSocket.recv(1024) #if the connection is still valid and there is a response then get it
print(ResponseSentence.decode()) # print the response
clientSocket.close() #end connection
