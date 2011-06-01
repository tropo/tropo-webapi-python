#!/usr/bin/python

# Hello, World CGI script.
# Addresses gh-5.
# Steps:
# 1. edit Apache httpd.conf file
#  Alias /tropo/ "/path/to/examples/"
# <Directory "/path/to/examples">
#    Options +ExecCGI
#    SetHandler cgi-script
#    Allow from all
#    AllowOverride All
# </Directory>
#   2. Create Web API app in Tropo and assign it the url 
#        http://my_webserver.com/tropo/g-5.hello_cgi.py
#   3. Place this file in examples folder and chmod it executable
#   4. Dial up Tropo app, and hear "Hello, World ..."

import cgi
from tropo import Tropo

def hello():
    t = Tropo()
    t.say(['hello world! I am a C G I script.'])
    json = t.RenderJson()
    print json
    return json



print "Content-type: text/json"
print
print 

hello()

