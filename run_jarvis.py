#! /usr/bin/env python3

import os
import sys
import argparse
import signal
import time
import simpleaudio
import random
import robothead

def parse_cmdline():
    parser = argparse.ArgumentParser(
         prog='jarvis.py',
         description='Runs the Jarvis control center')
    parser.add_argument('-c', '--conf', default='jarvis.conf', metavar='<conf>',
                        help="configuration file (default: %(default)s)")
    args = parser.parse_args()
    return args

def handler(signum, frame):
    msg = "Ctrl-C pressed, quitting..."
    print(msg)
    global stop
    stop = True

def callback_fn(channel):
    print("Callback called from channel %s" % channel)
    play_obj = wave_obj.play()
    while play_obj.is_playing():
        the_head.random_face()
        print(f'The current head status is: {the_head.get_face()}')
        time.sleep(random.randrange(100,500)/1000)
    the_head.neutral_face()

if __name__ == "__main__":
    args = parse_cmdline()
    if os.access(args.conf, os.R_OK):
        try:
           conf = robothead.get_config(args.conf)
        except:
            print(f"Could not parse confguration file: {args.conf}")
    else:
        print(f"ERROR: Could not open configuration file: {args.conf}")
        sys.exit(1)

    global stop
    stop = False

    the_head = robothead.head(conf)
    wave_obj = simpleaudio.WaveObject.from_wave_file(conf['audio']['file'])
    robothead.gpio.setup_gpio(conf, callback_fn)
    signal.signal(signal.SIGINT, handler)
    print("Ready! Press Crtl-C to exit")

    while not stop:
        time.sleep(1)

    robothead.gpio.cleanup_gpio()
