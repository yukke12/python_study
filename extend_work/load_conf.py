# -*- coding: utf-8 -*-
import ConfigParser

inifile = ConfigParser.SafeConfigParser()
inifile.read("./conf.ini")

print inifile.get("system", "os")
print inifile.get("user", "name")
