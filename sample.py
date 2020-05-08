#!/usr/bin/python    
import ConfigParser
import os
import pycurl
from io import BytesIO 

config = ConfigParser.RawConfigParser()
config.read('ConfigFile.properties')

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

#https://stackabuse.com/using-curl-in-python-with-pycurl/

b_obj = BytesIO() 
crl = pycurl.Curl() 

# Set URL value
crl.setopt(crl.URL, 'https://github.com/harivemula/platform-automation-pks/blob/master/README.md') 
#'https://wiki.python.org/moin/BeginnersGuide')

# Write bytes that are utf-8 encoded
crl.setopt(crl.WRITEDATA, b_obj)

# Perform a file transfer 
crl.perform() 

# End curl session
crl.close()

# Get the content stored in the BytesIO object (in byte characters) 
get_body = b_obj.getvalue()

# Decode the bytes stored in get_body to HTML and print the result 
print('Output of GET request:\n%s' % get_body.decode('utf8')) 

#
