from socket import *
import subprocess
import time
import platform

def get_os(): #function to get the software OS platform
    return platform.system()

serverPort = 9955 #server port to recieve data/packets on
serverSocket = socket(AF_INET, SOCK_STREAM) #TCP connection
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('--------------------------------------------------------------\n'
      '\t\t\t\t\tServer Side configuraion\n--------------------------------------------------------------')

nameList = ['1200749', '1200206'] #The list of valid IDs from client
isValid = 0 #flag used to know if the ID is valid or not

while True: #always check for connection from clients to accept
    connectionSocket, addr = serverSocket.accept()  # if found connection, accept it
    print('Sever is now listening to data from', addr)
    sentence = connectionSocket.recv(1024).decode()
    print(sentence)

    for i in range(len(nameList)): #check list if IDs
        if(sentence == nameList[i]): #if the sent message have an ID from the list
            lockscreen = 'Be aware!, The server OS screen will lock in 10 seconds.'
            connectionSocket.send(lockscreen.encode()) #send to client about lock screen
            print(lockscreen) #print lock screen msg on server side
            isValid = 1 #flag the ID as valid

            time.sleep(10) #wait 10s

            os_name = get_os() #get the name of OS
            if (os_name == 'Darwin'): #lock screen depending on OS type
                subprocess.run(["open", "-a", "ScreenSaverEngine"])
            elif (os_name == 'Windows'):
                subprocess.run(["rundll32.exe", "user32.dll,LockWorkStation"])
            elif (os_name == 'Linux'):
                subprocess.run(["gnome-screensaver-command", "-l"])

    if(isValid == 0): #if not from the list of IDs print the error msg on server
        print('This student ID is NOT VALID!\n')

    isValid = 0 #put validation back to false
    connectionSocket.close() #end connection

