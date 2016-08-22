import pycurl
import cStringIO

response = cStringIO.StringIO()

c = pycurl.Curl()
c.setopt(c.URL, 'icanhazip.com')
c.setopt(c.WRITEFUNCTION, response.write)
c.perform()
c.close()

print response.getvalue()
