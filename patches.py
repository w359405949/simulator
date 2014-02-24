import os
import sys
import codecs
import ConfigParser

def patch_prototype():
    config = ConfigParser.ConfigParser()
    config.readfp(codecs.open('config.ini', 'r', 'utf-8-sig'))
    prototype_file = config.get('Global', 'prototype', 'prototype')
    os.system("cd %s;svn up;find . -name '*.proto' |xargs protoc --python_out=." % prototype_file)
    open('%s/__init__.py' % prototype_file, 'w').close()
    sys.modules['prototype'] = __import__(prototype_file)
