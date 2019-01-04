#STUDENT_NAME:KARTHIK SOMANAHALLI MURALIDHARA
#STUDENT_ID:1001520125

import socket
from threading import Thread 
from SocketServer import ThreadingMixIn 

# Multithreaded Python server : TCP Server Socket Thread Pool
class ClientThread(Thread): 
 
    def __init__(self,ip,port): #defining and initialising ip and port number
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port 
        
        print "[+] New server socket thread started for " + ip + ":" + str(port) 
 
    def run(self): 
        while True : 
            data = conn.recv(2048) #size of the amount of date 
            print "Server received data:", data
            print "using HTTP"
            print "client is the localhost"
            print "socket family is 01"
            MESSAGE = raw_input("Multithreaded Python server : Enter Response from Server/Enter exit:")
            if MESSAGE == 'exit':
                break
            conn.send(MESSAGE)  # echo 
            
        
# Multithreaded Python server : TCP Server Socket Program Stub
TCP_IP = '0.0.0.0' 
TCP_PORT = 2004 #initialising the port number
BUFFER_SIZE = 20  # Usually 1024, but we need quick response 

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #address family
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
tcpServer.bind((TCP_IP, TCP_PORT)) 
threads = [] 
 
while True: 
    tcpServer.listen(4) 
    print "Multithreaded Python server : Waiting for connections from TCP clients..." 
    (conn, (ip,port)) = tcpServer.accept() 
    newthread = ClientThread(ip,port) 
    newthread.start() #new thread being started
    threads.append(newthread) 
 
for t in threads: 
    t.join() 
