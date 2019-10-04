import socket
import sys
import pygame
from gpiozero import Button
  signal import pause

def sendButtons():
    while True:
        # Accept connection from client
        conn, addr = s.accept()
        print "Connected to client: ", addr
              
        pygame.init()        

        def snareFunction():
            snare.play()
            conn.send("Button 1 was pressed")
            

        def chimeFunction():
            chime.play()
            conn.send("Button 2 was pressed")
            

        def pianoFunction():
            piano.play()
            conn.send("Button 3 was pressed")
   
        snare = pygame.mixer.Sound('/home/pi/gpio-music-box/samples/drum_snare_soft.wav') 
        chime = pygame.mixer.Sound('/home/pi/gpio-music-box/samples/elec_chime.wav')
        piano = pygame.mixer.Sound('/home/pi/gpio-music-box/samples/ambi_piano.wav')


        btnSnare.when_pressed = snareFunction 
        btnChime.when_pressed = chimeFunction
        btnPiano.when_pressed = pianoFunction     
        

# Creates a socket
try:
    s = socket.socket(socket.AF_INET, socket. SOCK_STREAM)
    print "Socket has been created"
except socket.error as err:
    print "Socket error: %s" %(err)

# Reserving  a port
port = 10000

# Binds IP address and port number
try:
    s.bind(("",port))
    print "Socket has binded to port %s" %(port)
except socket.error as err:
    print "Binding error: %s" %(err)

# Listens for requests from clients
try:
    s.listen(4)
    print "Listening for requests..."
except socket.error as err:
    print "Listening error: %s" %(err)

btnSnare = Button(17) 
btnChime = Button(10)
btnPiano = Button(11)

# Transmits buttons to client
sendButtons()

# Close Connection
conn.close()
print "Connection closed"








        
        
    



        
        



