#!/usr/bin/env python
import os
import sys
from os.path import abspath, dirname

if __name__ == "__main__":
    sys.path.insert(0, dirname(dirname(abspath(__file__))))
    sys.path.append(dirname(abspath(__file__)) + '/lib/python2.6/site-packages')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)