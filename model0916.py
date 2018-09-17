#!usr/bin/env python
import os
import sys
import time
word='yanjing'
os.system('rosrun object_recognition_core object_add.py -n "%s" -d "%s" --commit' % (word,word))
os.system('curl -X GET http://localhost:5984/object_recognition/_design/objects/_view/by_object_name/ >1.txt')
f = open('/home/victor/1.txt')
txt = f.read()
a=txt[44:76]
print a
os.system('rosrun object_recognition_core mesh_add.py %s /home/victor/stl/%s.stl --commit' % (a,word))
os.system('rosrun object_recognition_core training -c `rospack find object_recognition_linemod`/conf/training.ork')
