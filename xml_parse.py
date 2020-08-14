import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_899685.xml'
html = urllib.request.urlopen(url, context=ctx).read()
tree = ET.fromstring(html.decode())

print(sum([int(x.text) for x in tree.findall('comments/comment/count')]))
