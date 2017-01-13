#!/usr/bin/env python

import os
import urllib2
import json
import cStringIO
import datetime

metadata = urllib2.urlopen("http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US").read()

metadata = json.loads(metadata)

print metadata
print "metadata recieved"

image_url = "http://www.bing.com"+metadata[u'images'][0]['url']

file = cStringIO.StringIO(urllib2.urlopen(image_url).read())

now = datetime.datetime.now()

ctr = now.day

print "file created"

fd = open ('/home/arjun/open_source/bing-wallpaper-ubuntu/pics/file'+str(ctr)+'.jpg', 'w+')
# populate buf
fd.write (file.getvalue ())

# os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri file:///home/arjun/open_source/bing-wallpaper-ubuntu/pics/file"+str(ctr)+".jpg")

print "success"