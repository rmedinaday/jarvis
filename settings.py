#! /bin/env/python3

import sys
import yaml

def get_config(config):
    try:
        f = open(config, 'r')
    except (IOError, FileNotFoundError) as e:
        raise
    try:
        config_dict = yaml.load(f, Loader=yaml.SafeLoader)
    except yaml.YAMLError as e:
        print(f'Error in configuration file: {e}')
        if hasattr(e, 'problem_mark'):
            mark = e.problem_mark
            print("Error position: (%s:%s)" % (mark.line+1, mark.column+1))
        raise
    return config_dict