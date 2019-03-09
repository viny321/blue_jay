#!coding:utf-8
    
import csv
import drawpic
import jieba
from collections import Counter

#根据TXT分词、生成条形图和词云图
def drawpicByTxt(site1):
    txtPath = site1+".txt"
    destImgName = site1+'.png'
    descImageName = site1+'.jpg'
    srcImagePath = "d:/html/source/xxx.jpg"    #词云图背景图
    #根据txt 的内容分词、去停用词 构建CSV 文件
    #duan_words = getDuanWord(readTxt(txtPath))
    c = getDuanWord(readTxt(txtPath))
    csvPath = txtToCSV(txtPath,c)
    #根据CSV 文件 生成条形图 和 词云图
    drawpic.bar_plot(csvPath,destImgName)
    drawpic.drawpic(csvPath,imagePath,descImageName)

#
def readTxt(txtPath):
    with open(txtPath,mode='r',encoding='utf-8') as txt:
        text = txt.read()
    return text

#
def txtToCSV(txtPath,c):
    csvPath = txtPath.replace('.txt','.csv')
    with open(csvPath,'w',encoding='UTF-8',newline='') as output_csv_file:
        filewriter = csv.writer(output_csv_file)
        filewriter.writerow(['words','frequency'])
        for i,tup in enumerate(c):
            if i==0:
                print('==>',tup[0],tup[1])
                continue
            elif i==101:
                break
            else:
                filewriter.writerow([tup[0],tup[1]])
    return csvPath

#去停用词
def getDuanWord(text):
    stop_word_list = []
    with open('d:/html/source/stop_word.txt',mode='r',encoding='utf-8') as swt:
        for line in swt.readlines():
            line = line.strip()
            if not len(line):
                continue
            stop_word_list.append(line)
    duan_words = []
    c = Counter(jieba.cut(text)).most_common(500) #在分词的结果中取500个
    for word in c:
        if word[0] not in stop_word_list:
            duan_words.append(word)
    return duan_words