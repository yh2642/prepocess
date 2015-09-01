__author__ = 'Administrator'


# coding=utf-8
import json
d = {'first': 'One', 'second':2}
json.dump(d, open('/tmp/result.txt', 'w'))


# coding=utf-8
import json
d = json.load(open('/tmp/result.txt','r'))
print d, type(d)

{u'second': 2, u'first': u'One'} <type 'dict'>