# encoding:utf-8
import urllib
import urllib2
import cookielib
import re
import sys

output = sys.stdout
outputfile = open('test.txt', 'w')
sys.stdout = outputfile
for page in range(1,8):
# page = 1
    url = 'http://www.qiushibaike.com/hot/page/' + str(page)
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    headers = {'User-Agent': user_agent}
    try:
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request)
        content = response.read()#.decode('utf-8')
        pattern = re.compile('h2>(.*?)</h2.*?content">(.*?)</div>(.*?)<div class="stats">.*?number">(.*?)</',re.S)
        items = re.findall(pattern, content)
        for item in items:
            haveImg = re.search("img", item[2])
            if not haveImg:
                print>>outputfile,item[0],item[1].replace('<br/>','\n')#item[1]

    except urllib2.URLError, e:
        if hasatter(e, "code"):
            print e.code
        if hasatter(e, "reason"):
            print e.reason

outputfile.close()
sys.stdout = output
