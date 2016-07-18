# encoding:utf-8
__author__ = 'my88899'
import urllib
import urllib2
import re

# 百度贴吧爬虫类
class BDTB(object):

    def __init__(self, baseUrl, seeLZ):
        self.baseURL = baseUrl
        self.seeLZ = '?see_lz=' + str(seeLZ)

    # 传入页码，获取该页帖子代码
    def getPage(self, pageNum):
        try:
            url = self.baseURL + self.seeLZ + '&pn=' + str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            print response.read()
            return response
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print u"fail to connect to BDTB, reason: ", e.reason

    def getTitle(self):
    	page=self.getPage(1)
    	pattern=re.compile(('<h3 class="core_title_txt .*?>(.*?)</h3>',re.S))
    	result=re.search(pattern,page)
    	if result:
    		print result.group(1)
    		return result.group(1)
    	else:
    		return None

baseUrl = 'http://tieba.baidu.com/p/3138733512'
bdtb = BDTB(baseUrl, 1)
bdtb.getPage(1)
