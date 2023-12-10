#! /usr/bin/env python3

import time
import Jetson.GPIO as GPIO
import Adafruit_PCA9685
import signal
import random

PIN=7
BUS=0
PCA9685_ADDRESS=0x40
SERVO_ID = 0
SERVO_MIN = 150  # Min pulse length out of 4096
SERVO_MAX = 600  # Max pulse length out of 4096

global stop
stop = False
counter = 0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.IN)

def handler(signum, frame):
    msg = "Ctrl-C pressed, quitting..."
    print(msg)
    global stop
    stop = True

def callback_fn(channel):
    print("Callback called from channel %s" % channel)
    pulse = random.randrange(SERVO_MIN, SERVO_MAX)
    pwm.set_pwm(SERVO_ID, 0, pulse)

pwm = Adafruit_PCA9685.PCA9685(address=PCA9685_ADDRESS, busnum=BUS)

# Configure min and max servo pulse lengths
pwm.set_pwm_freq(60)

signal.signal(signal.SIGINT, handler)
GPIO.add_event_detect(PIN, GPIO.FALLING, callback=callback_fn)
print("Ready! Press Crtl-C to exit")

while not stop:
    time.sleep(1)

GPIO.cleanup()
