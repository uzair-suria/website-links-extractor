import urllib.request, urllib.parse, urllib.error
import re
import ssl

# regex pattern:
pattern = b'href="(http[s]?://.+?)"'

# ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode  = ssl.CERT_NONE

url = input('Enter the URL: ')
html = urllib.request.urlopen(url, context=ctx).read()
links = re.findall(pattern, html)
print("Found Following Links: ")
for link in links:
    print(link.decode())
