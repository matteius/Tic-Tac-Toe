#!/usr/bin/env python
import sys, os

# Add custom Python paths
sys.path.insert(0, "/home2/geekshac/django_projects/")
sys.path.insert(0, "/home2/geekshac/django_projects/tictactoe/")

# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ['DJANGO_SETTINGS_MODULE'] = "tictactoe.settings"

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")