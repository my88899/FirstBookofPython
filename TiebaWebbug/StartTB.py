# encoding:utf-8
__author__ = 'my88899'
import urllib
import urllib2
import re

# 处理页面标签类


class Tool():
    # 去除img标签,7位长空格
    removeImg = re.compile('<img.*?>| {7}|')
    # 删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    # 把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    # 将表格制表<td>替换为\t
    replaceTD = re.compile('<td>')
    # 把段落开头换为\n加空两格
    replacePara = re.compile('<p.*?>')
    # 将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    # 将其余标签剔除
    removeExtraTag = re.compile('<.*?>')

    def replace(self, x):
        x = re.sub(self.removeImg, "", x)
        x = re.sub(self.removeAddr, "", x)
        x = re.sub(self.replaceLine, "\n", x)
        x = re.sub(self.replaceTD, "\t", x)
        x = re.sub(self.replacePara, "\n    ", x)
        x = re.sub(self.replaceBR, "\n", x)
        x = re.sub(self.removeExtraTag, "", x)
        # strip()将前后多余内容删除
        return x.strip()


# 百度贴吧爬虫类


class BDTB(object):

    def __init__(self, baseUrl, seeLZ):
        self.baseURL = baseUrl
        self.seeLZ = '?see_lz=' + str(seeLZ)
        self.tool = Tool()


    # 传入页码，获取该页帖子代码
    def getPage(self, pageNum):
        try:
            url = self.baseURL + self.seeLZ + '&pn=' + str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            # print response.read()
            return response.read().decode('utf-8')
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print u"fail to connect to BDTB, reason: ", e.reason
                return None

    def getTitle(self):
        page = self.getPage(1)
        pattern = re.compile(
            ('<h3 class="core_title_txt .*?>(.*?)</h3>', re.S))
        result = re.search(pattern, page)
        if result:
            # print result.group(1)
            return result.group(1).strip()
        else:
            return None

    def getPageNum(self):
        page = self.getPage(1)
        pattern = re.compile(
            '<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>', re.S)
        result = re.search(page, pattern)
        if result:
            # print result.group(1)
            return result.group(1).strip()
        else:
            return None

# 获取每一层楼的内容,传入页面内容
    def getContect(self, page):
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>')
        items = re.findall(pattern, page)
        floor = 1
        # for item in items:
        #     print item
        for item in items:
            print u"Floor:", floor, u"------------------------------------------------------------------------------------------------------------------------------------\n"
            print self.tool.replace(items[1])
            floor += 1

baseUrl = 'http://tieba.baidu.com/p/3138733512'
bdtb = BDTB(baseUrl, 1)
bdtb.getContect(bdtb.getPage(1))
