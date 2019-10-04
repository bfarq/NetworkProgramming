import pygame
from gpiozero import Button

pygame.init()

def snareFunction():
    snare.play()
    print("Button 1 was pressed")

def chimeFunction():
    chime.play()
    print("Button 2 was pressed")

def pianoFunction():
    piano.play()
    print("Button 3 was pressed")

btn_snare = Button(17) 
btn_chime = Button(10) 
btn_piano = Button(11) 
    
snare = pygame.mixer.Sound('/home/pi/gpio-music-box/samples/drum_snare_soft.wav') 
chime = pygame.mixer.Sound('/home/pi/gpio-music-box/samples/elec_chime.wav')
piano = pygame.mixer.Sound('/home/pi/gpio-music-box/samples/ambi_piano.wav')


btn_snare.when_pressed = snareFunction 
btn_chime.when_pressed = chimeFunction
btn_piano.when_pressed = pianoFunction



    



