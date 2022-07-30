import os
from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
#Mendefinisikan Tombol
#Tombol ON
GPIO.setup(2, GPIO.IN)

#Tombol OFF
GPIO.setup(3, GPIO.IN)
GPIO.setwarnings(False)
#Mendefinisikan Lampu LED
GPIO.setup(4,GPIO.OUT)
#Me non aktifkan lampunya dulu (LOW) kalau (HIGH) menyalakan lampu
GPIO.output(4,GPIO.LOW)

while True:
on = GPIO.input(2)
off = GPIO.input(3)
if on == True:
print "Lampu ON"
GPIO.output(4, GPIO.HIGH)
sleep(0.2)
elif off == True:
print "Lampu OFF"
GPIO.output(4, GPIO.LOW)
sleep(0.2)