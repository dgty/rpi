#!/usr/bin/python

import datetime
import MySQLdb
import pycurl
import cStringIO

conn = MySQLdb.connect(host= "31.220.17.165",
user="dgtysoft_adm",
passwd="db1743",
db="dgtysoft_rpis")
x = conn.cursor()

name = "RPI3"
date = datetime.datetime.now()

response = cStringIO.StringIO()

c = pycurl.Curl()
c.setopt(c.URL, 'icanhazip.com')
c.setopt(c.WRITEFUNCTION, response.write)
c.perform()
c.close()

ip = response.getvalue()

sql = ("SELECT Name FROM IPAddresses")
result = x.execute(sql)
for row in x.fetchall() :
	print row

query = """INSERT INTO IPAddresses (Name,IP,Date) VALUES ('%s','%s','%s')""" % (name,ip,date)

print query

try:
	x.execute(query)
	conn.commit()
except:
	conn.rollback()
	
	print "didn't work"

conn.close()
