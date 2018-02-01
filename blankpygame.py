#!/usr/bin/python

import pygame, sys
import serial
from pygame.locals import *

# port address
SERIAL_PORT = '/dev/ttyACM0'
# set baud rate
SERIAL_RATE = 9600

pygame.init()
DISPLAYSURF = pygame.display.set_mode((500, 500))
ser = serial.Serial(SERIAL_PORT, SERIAL_RATE)
pygame.display.set_caption('It\'s lit!')

while True:
    # read each line from the serial port
    r_value = ser.readline().decode('utf-8')
    g_value = ser.readline().decode('utf-8')
    b_value = ser.readline().decode('utf-8')
    red = int(r_value)
    green = int(g_value)
    blue = int(b_value)
    COLOR = (red,green,blue,255)
    DISPLAYSURF.fill(COLOR)
    for event in pygame.event.get(): 
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
