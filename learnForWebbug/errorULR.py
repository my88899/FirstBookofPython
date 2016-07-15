# import urllib2

# requset = urllib2.Request('http://www.xxxxx.com')
# try:
#     urllib2.urlopen(requset)
# except urllib2.URLError, e:
#     print e.reason


import urllib2

req = urllib2.Request('http://blog.csdn.net/cqcre')
try:
    urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print e.code
    print e.reason
