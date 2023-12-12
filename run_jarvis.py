#! /usr/bin/env python3

import os
import sys
import argparse
from settings import get_config
import head

def parse_cmdline():
    parser = argparse.ArgumentParser(
         prog='jarvis.py',
         description='Runs the Jarvis control center')
    parser.add_argument('-c', '--conf', default='jarvis.conf', metavar='<conf>',
                        help="configuration file (default: %(default)s)")
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_cmdline()
    if os.access(args.conf, os.R_OK):
        try:
           conf = get_config(args.conf)
        except:
            print(f"Could not parse confguration file: {args.conf}")
    else:
        print(f"ERROR: Could not open configuration file: {args.conf}")
        sys.exit(1)

    