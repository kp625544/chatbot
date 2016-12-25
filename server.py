import aiml
import os
import socket

bot = aiml.Kernel();
bot.setBotPredicate('name', 'Pedro')
bot.setBotPredicate('master', 'Hydra')
bot.learn("std-startup.xml")
bot.respond("load aiml b")

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 4444                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.

c, addr = s.accept()     # Establish connection with client.



#print os.system("nc -l -p 4444")

while 1:
    print 'Got connection from', addr
    c.send('Thank you for connecting')
    data = s.recv(1024)
    print bot.respond(data)



c.close()                # Close the connection
