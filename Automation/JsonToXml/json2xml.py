#!/usr/bin/env python2.7

import json
import urllib
import dicttoxml

page = urllib.urlopen('https://jsonplaceholder.typicode.com/todos/1')

content = page.read()
obj = json.loads(content)

print(obj)

print("--------------------")

xml = dicttoxml.dicttoxml(obj)
print(xml)
