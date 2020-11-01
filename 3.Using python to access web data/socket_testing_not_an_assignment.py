import socket                                                   #import library

mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)         #create socket
mysock.connect(('data.pr4e.org',80))                            #establishing connection with server and port
cmd='GET http://pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()   #turns out server does not exist
mysock.send(cmd)                                                #calling method on socket object

while True:                                                     #loop to run until EOF
  data=mysock.recv(512)
  if(len(data)<1):  break                                       #break if file is empty
  print(data.decode())                                          #decode file and print it
mysock.close()                                                  #close the socket because it takes up resources
