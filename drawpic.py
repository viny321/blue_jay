#!coding:utf-8

import csv
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
from os import path
from wordcloud import WordCloud, STOPWORDS ,ImageColorGenerator

#根据传入的map<str:float> 按给定的 float 的大小生成词云，写到当前文件夹下的destImgName 中，背景图为 sourImgPath
def drawpic(csvPath,sourImgPath,destImgName):
    dictx = csvToDict(csvPath)
    backgroud_Image = plt.imread(sourImgPath)  #根据给定的源地址加载背景图片 
    print("图片加载成功")
    #设置词云样式
    wc = WordCloud(
        width=845,
        height=845,
        background_color='white',
        mask=backgroud_Image,
        font_path='d:/html/source/xxx.ttf',#设置字体，这里为字体路径
        max_words=105,
        relative_scaling=0.6,
        stopwords=STOPWORDS,
        max_font_size=90,
        random_state=20
    )
    wc.generate_from_frequencies(dictx,max_font_size=None)
    print("开始加载词组")
    img_colors = ImageColorGenerator(backgroud_Image,default_color=(0,0,0))
    wc.recolor(random_state=20,color_func=img_colors)
    plt.imshow(wc)
    plt.axis('off')
    #plt.show()
    wc.to_file(destImgName)
    print("词云生成成功！")
    return

#生成条形图
def bar_plot(csvPath,destImgName):
    #配置中文字体和修改字体大小
    matplotlib.rcParams['font.family'] = 'SimHei'
    matplotlib.rcParams['font.size'] = 12

    data_frame = pd.read_csv(csvPath,sep=',',nrows=10)
    words = data_frame['words']
    words_index = range(len(words))
    frequency = data_frame['frequency']

    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
    ax1.bar(words_index,frequency,align = 'center',color = 'blue')
    plt.xticks(words_index,words,rotation=0)
    plt.xlabel('word')
    plt.ylabel('frequency')
    plt.title('热点词')

    plt.savefig(destImgName,dpi=400,bbox_inches='tight')
    #plt.show()
    print("热点词统计条形图生成成功")
    return

#读取CSV文件构造dict
def csvToDict(csvPath):
    dictx = {}
    with open(csvPath,'r',encoding='utf-8') as csvFile:
        dictReader = csv.DictReader(csvFile)
        for item in dictReader:
            dictx[item['words']] = float(item['frequency'])
    return dictx