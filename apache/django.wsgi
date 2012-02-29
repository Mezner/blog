import os, sys
sys.path.append('/home/mezner')
sys.path.append('/home/mezner/russellmyers')
sys.path.append('/home/mezner/russellmyers/templates')
os.environ['DJANGO_SETTINGS_MODULE'] = 'russellmyers.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
