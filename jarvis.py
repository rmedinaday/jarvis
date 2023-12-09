#! /usr/bin/python3


import Jetson.GPIO as GPIO
import simpleaudio as sa
import time
import signal

global stop
stop = False
pin = 7
counter = 0
filename = 'newgrange.wav'
wave_obj = sa.WaveObject.from_wave_file(filename)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.IN)

#while counter <10:
#  value = GPIO.input(pin)
#  print("Pin %d input value %d" % (pin, value))
#  counter += 1
#  time.sleep(1)

def handler(signum, frame):
    msg = "Ctrl-C pressed, quitting..."
    print(msg)
    global stop
    stop = True

def callback_fn(channel):
    print("Callback called from channel %s" % channel)
    play_obj = wave_obj.play()
    play_obj.wait_done()

signal.signal(signal.SIGINT, handler)

GPIO.add_event_detect(pin, GPIO.FALLING, callback=callback_fn)
print("Ready! Press Crtl-C to exit")

while not stop:
    time.sleep(1)
GPIO.cleanup()


