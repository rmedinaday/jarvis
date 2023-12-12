#! /usr/bin/python3

import sys
import Jetson.GPIO as GPIO
import simpleaudio as sa
import time
import signal
import Adafruit_PCA9685
import random
from settings import get_config

global stop
stop = False
pin = 7
counter = 0
filename = 'oobleck.wav'
wave_obj = sa.WaveObject.from_wave_file(filename)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.IN)

BUS=0
PCA9685_ADDRESS=0x40

EYE_H=0
EYE_H_MAX=500
EYE_H_MIN=300
EYE_H_REST=400

EYE_V=2
EYE_V_MAX=430
EYE_V_MIN=310
EYE_V_REST=370

JAW=4
JAW_MIN=250
JAW_MAX=390

HEAD=6
HEAD_MIN=340
HEAD_MAX=390

pwm = Adafruit_PCA9685.PCA9685(address=PCA9685_ADDRESS, busnum=BUS)
pwm.set_pwm_freq(60)

def generateExpression():
    global eye_h_pulse
    global eye_v_pulse
    global jaw_pulse
    eye_h_pulse = random.randrange(EYE_H_MIN, EYE_H_MAX)
    eye_v_pulse = random.randrange(EYE_V_MIN, EYE_V_MAX)
    jaw_pulse = random.randrange(JAW_MIN, JAW_MAX)

def resetExpression():
    pwm.set_pwm(JAW, 0, JAW_MIN)
    pwm.set_pwm(EYE_H, 0, EYE_H_REST)
    pwm.set_pwm(EYE_V, 0, EYE_V_REST)

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
    global jaw_pulse
    global eye_h_pulse
    global eye_v_pulse
    print("Callback called from channel %s" % channel)
    play_obj = wave_obj.play()
    while play_obj.is_playing():
        generateExpression()
        pwm.set_pwm(JAW, 0, jaw_pulse)
        pwm.set_pwm(EYE_H, 0, eye_h_pulse)
        pwm.set_pwm(EYE_V, 0, eye_v_pulse)
        time.sleep(random.randrange(100,500)/1000)
    resetExpression()

signal.signal(signal.SIGINT, handler)

GPIO.add_event_detect(pin, GPIO.FALLING, callback=callback_fn)

print("Ready! Press Crtl-C to exit")

while not stop:
    time.sleep(1)
GPIO.cleanup()


