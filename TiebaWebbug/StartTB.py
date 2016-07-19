# -*- coding:utf-8 -*-
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

    def __init__(self, baseUrl, seeLZ, floorTag):
        self.baseURL = baseUrl
        self.seeLZ = '?see_lz=' + str(seeLZ)
        self.tool = Tool()
        # 全局file变量，文件写入操作对象
        self.file = None
        # 楼层标号，初始为1
        self.floor = 1
        # 默认的标题，如果没有成功获取到标题的话则会用这个标题
        self.defaultTitle = u"百度贴吧"
        # 是否写入楼分隔符的标记
        self.floorTag = floorTag

    # 传入页码，获取该页帖子代码
    def getPage(self, pageNum):
        try:
            url = self.baseURL + self.seeLZ + '&pn=' + str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            # print response.read()
            return response.read().decode('utf-8')
        except urllib2.URLError as e:
            if hasattr(e, "reason"):
                print u"fail to connect to BDTB, reason: ", e.reason
                return None

    def getTitle(self, page):
        #得到标题的正则表达式
        pattern = re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>',re.S)
        # pattern = re.compile(('<h3 class="core_title_txt .*?>(.*?)</h3>', re.S))
        result = re.search(pattern, page)
        if result:
            return result.group(1).strip()
        else:
            return None

    def getPageNum(self, page):
        page = self.getPage(1)
        pattern = re.compile(
            '<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>', re.S)
        result = re.search(pattern, page)
        if result:
            return result.group(1).strip()
        else:
            return None

# 获取每一层楼的内容,传入页面内容
    def getContect(self, page):
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
        items = re.findall(pattern, page)
        contents = []
        # floor = 1
        # for item in items:
        #     print item
        for item in items:
            # 将文本进行去除标签处理，同时在前后加入换行符
            content = "\n" + self.tool.replace(item) + "\n"
            # contents.extend(content.encode('utf-8'))
            contents.append(content.encode('utf-8'))
        return contents
            # print content
            # print u"Floor:", floor, u"------------------------------------------------------------------------------------------------------------------------------------\n"
            # print self.tool.replace(items[1])
            # floor += 1

    def setFileTitle(self,title):
        #如果标题不是为None，即成功获取到标题
        if title is not None:
            self.file = open(title + ".txt","w+")
        else:
            self.file = open(self.defaultTitle + ".txt","w+")
        pass

    def writeData(self,contents):
        #向文件写入每一楼的信息
        for item in contents:
            if self.floorTag == '1':
                #楼之间的分隔符
                floorLine = "\n" + str(self.floor) + u"-----------------------------------------------------------------------------------------\n"
                self.file.write(floorLine)
            self.file.write(item)
            self.floor += 1

    def start(self):
        indexPage = self.getPage(1)
        pageNum = self.getPageNum(indexPage)
        title = self.getTitle(indexPage)
        self.setFileTitle(title)
        if pageNum == None:
            print "URL was lost, please try again..."
            return
        try:
            print "Total pages number is: " + str(pageNum)
            for i in range(1,int(pageNum)+1):
                print "Writing page number is: " + str(i)
                page = self.getPage(i)
                print "getPage complete"
                contents = self.getContect(page)
                print "getContect complete"
                # print contents
                self.writeData(contents)
                print "writeData complete"
        #出现写入异常
        except IOError,e:
            print "writing error, reason: " + e.message
        finally:
            print "loading complete"

print u"input the number of TZ"
baseURL = 'http://tieba.baidu.com/p/'+str(raw_input(u'http://tieba.baidu.com/p/'))
seeLZ = raw_input("input 1 to get the hosts only, input 0 for all\n")
floorTag = raw_input("wheather to get the detail of the host, 1 for yes, 0 for no\n")
bdtb = BDTB(baseURL, seeLZ, floorTag)
bdtb.start()


# baseUrl = 'http://tieba.baidu.com/p/3138733512'
# bdtb = BDTB(baseUrl, 1)
# bdtb.getContect(bdtb.getPage(1))
