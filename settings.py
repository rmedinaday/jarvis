#! /bin/env/python3

import sys
import yaml

def getconfig(config):
    try:
        f = open(config, 'r')
    except IOError:
        print(f'Configuration file {config} not found. Quitting.')
        sys.exit(1)
    try:
        config_dict = yaml.load(f, Loader=yaml.SafeLoader)
    except yaml.YAMLError, exc:
        print(f'Error in configuration file: {exc}')
        if hasattr(exc, 'problem_mark'):
            mark = exc.problem_mark
            print("Error position: (%s:%s)" % (mark.line+1, mark.column+1))
        sys.exit(1)
    return config_dict
