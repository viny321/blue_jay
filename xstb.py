#!coding:utf-8
    
import match
import re

class xstbMatcher(match.Matcher):
    #重写searchUrl 方法，使其返回下一页的URL 链接，格式为字符串
    def searchUrl(self):
        pattern = re.compile(r'l2" href="(.*?)">下')
        urls = pattern.findall(self.content)
        if len(urls)==0:
            return ""
        else:
            url = re.sub(r'amp;','',urls[0])
            return "url"+url
    
    #重写searchContent 方法，使其返回要爬取的网页主要内容，返回格式为字符串
    def searchContent(self):
        pattern = re.compile(r'<tr>(?s:(.*?))</tr>')
        results = pattern.findall(self.content)
        strx = ""
        for result in results:
            strx += result
        strx = re.sub(r'<td width(.*?)</td>|<td>\d{1,3}</td>|<td class="tbc">(?s:(.*?))</td>|<span class="title">|</span>|<td class="tbl">|<.{0,1}td>',"#",strx)
        strx = re.sub(r'\s|target="_blank"','',strx)
        strx = re.sub(r'#####','\n',strx)
        return strx

    #重写searchImage 方法，使其返回想要爬取的网页的图片链接， 返回格式为 list
    def serachImage(self):
        return ''