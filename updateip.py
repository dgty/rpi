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
ip = ip.rstrip()

sql = ("SELECT Name FROM IPAddresses")
result = x.execute(sql)
for row in x.fetchall() :
	print row

query = """UPDATE IPAddresses SET IP='%s',Date='%s' WHERE Name='%s' """ % (ip,date, name)

print query

try:
	x.execute(query)
	conn.commit()
except:
	conn.rollback()
	
	print "didn't work"

conn.close()

log = "IP Update at: " + str(date) + " With IP: " + ip + " \n"
with open("Scripts/Logs/ipupdate_log.txt", "a") as logfile:
	logfile.write(log)
