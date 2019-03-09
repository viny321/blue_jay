#!coding:utf-8
    
import requests

Matchers={}

#run 方法，爬虫入口，site 为对应的网站，n 为指定爬取的页数（如果有下一页，下一页的链接由searchUrl 方法获取）
def run(site,n):
    if site not in Matchers.keys():   #Matchers 中没有site 指定的对象，返回
        return
    writeTXT(site)
    n -= 1
    if n==0:                        #指定页数爬取完成，返回
        print("----------------------------------------------\nn==0\n")
        return  
    if not updateMatcher(site):  #如果matcher 更新失败，返回
        print("update Matcher fail")
        return  
    return run(site,n)

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def runx(site):
    if site not in Matchers.keys():   #Matchers 中没有site 指定的对象，返回
        return
    writeTXT(site)
    if not updateMatcher(site):  #如果matcher 更新失败，返回
        print("update Matcher fail")
        return  
    return runx(site)

#把字符串strx 写入pathx 中指定的文件
def writeTXT(site):
    matcher = Matchers[site]
    pathx = site+".txt"
    with open(pathx,mode='a',encoding='utf-8') as f:
        f.write(matcher.searchContent())
        print(matcher.url,"文本内容爬取成功")
    return

#根据新的URL创建新的Matcher,put到Matchers 中
def updateMatcher(site):
    matcher = Matchers[site]
    url = matcher.searchUrl()
    if url == "":
        return False
    else:
        m1 = matcher.__class__(url)
        Matchers[site] = m1
        return True

#register 用于site 注册
def register(site,matcher):
    if site not in Matchers.keys():
        Matchers[site] = matcher
        print(site,"注册成功")
    else:
        print(site,"重复注册！")

#Matcher 对象，默认的爬虫方法，对下载的页面不做任何处理，直接返回
class Matcher(object):
    def __init__(self,url):
        self.url = url
        self.content = self.getHtmlByUrl(url)

    #根据URL 获取 HTML
    def getHtmlByUrl(self,url):
        headers={"Accept-Language":"zh-CN,zh;q=0.9"}
        r = requests.get(url,headers=headers)
        r.encoding = 'utf-8'
        return r.text

    def searchUrl(self):
        return ""

    def searchContent(self):
        return self.content
    
    def serachImage(self):
        return []
