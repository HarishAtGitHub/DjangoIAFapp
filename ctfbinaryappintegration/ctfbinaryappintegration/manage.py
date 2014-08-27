#!/usr/bin/env python
import os
import sys
from os.path import abspath, dirname

if __name__ == "__main__":
    sys.path.insert(0, dirname(dirname(abspath(__file__))))
    sys.path.append(dirname(abspath(__file__)) + '/iaf_endpoint/webservice/rest/lib/python2.6/site-packages')
    sys.path.append(dirname(abspath(__file__)) + '/iaf_endpoint/webservice/rest/lib/python2.6/site-packages/SOAPpy-0.12.5-py2.6.egg')
    sys.path.append(dirname(abspath(__file__)) + '/iaf_endpoint/webservice/rest/lib/python2.6/site-packages/fpconst-0.7.2-py2.6.egg')
    sys.path.append(dirname(abspath(__file__)) + '/iaf_endpoint/webservice/rest/lib/python2.6/site-packages/wstools-0.4-py2.6.egg')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)