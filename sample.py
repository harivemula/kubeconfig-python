#!/usr/bin/python    
import ConfigParser
import os
import pycurl
from io import BytesIO 
import sys


config = ConfigParser.RawConfigParser()
config.read('/var/ConfigFile.properties')

print "dbname:[" + config.get('DatabaseSection', 'database.dbname')+"]";

# Set environment variables
#os.environ['API_USER'] = 'username'
#os.environ['API_PASSWORD'] = 'secret'

# Get environment variables
#USER = os.getenv('API_USER')
#PASSWORD = os.environ.get('API_PASSWORD')
print "API_USER:["+os.getenv('API_USER','None')+"]"
print "API_PASSWORD:["+os.getenv('API_PASSWORD','None')+"]"
print "HTTP_PROXY:["+os.getenv('HTTP_PROXY','None')+"]"
print "HTTPS_PROXY:["+os.getenv('HTTPS_PROXY','None')+"]"
print "NO_PROXY:["+os.getenv('NO_PROXY','None')+"]"


PY3 = sys.version_info[0] > 2


class Test:
    def __init__(self):
        self.contents = ''
        if PY3:
            self.contents = self.contents.encode('ascii')

    def body_callback(self, buf):
        self.contents = self.contents + buf


sys.stderr.write("Testing %s\n" % pycurl.version)

t = Test()
c = pycurl.Curl()
c.setopt(c.URL, 'https://file-examples.com/wp-content/uploads/2017/02/file_example_JSON_1kb.json')
c.setopt(c.WRITEFUNCTION, t.body_callback)
c.perform()
c.close()

print(t.contents)
#
