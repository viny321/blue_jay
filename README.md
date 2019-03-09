# blue_jay
Tool for Create WordCloud from CSV Files

这是一个Python 爬虫和数据分析练习项目  
系统的主要流程为:
1. 根据注册的matcher爬取网络内容，并保存到TXT文件中
2. 对TXT中的内容进行分词、统计、去除停用词，数据保存到CSV文件中
3. 根据CSV中的数据构造 直方图 和 词云图

###### 注意：（爬虫需要根据自己的需要重写Matcher（默认的对象构造包含在match.py文件中），并在运行前注册到程序中，代码中给出xstb.py作为例子）

![Image text](https://github.com/viny321/blue_jay/blob/master/image.png)
