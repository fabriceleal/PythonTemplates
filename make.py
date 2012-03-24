#!/usr/bin/python


t = Template('${name}sadkasldkjasd')

d = {}
d['name'] = 'hello world!'

t.substitute(d)
