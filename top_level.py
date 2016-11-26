#!/usr/bin/python

# http://stackoverflow.com/questions/1260792/python-import-a-file-from-a-subdirectory
# libs/__init__.py  # file must exist, even if empty
# from libs import lower_level
import libs.lower_level as lower_level  # otherwise default: libs.lower_level

print lower_level.inner_call("Hello World")

