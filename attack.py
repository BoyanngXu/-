import io
import os
import re
from bs4 import BeautifulSoup
import urllib.request
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding = 'utf8')
url = "https://movie.douban.com/top250?start=0&filter="

def askURL(url):    #得到某一网页内容
    head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}
    #编辑头文件，伪装
    req = urllib.request.Request(url,headers=head)#发出请求
    res = urllib.request.urlopen(req)#打开url，从而得到html
    html = res.read().decode("utf-8") #html的byte转str

    f = open('D:\douban.txt','a',encoding='utf-8')
    f.write(html + '\n\n\n\n')
    f.close()
    return html

def getdata(url):   #爬取网页
    datalist = []
    for i in range (0,10):
        url = "https://movie.douban.com/top250?start=" + str(i*25) + "&filter="
        html = askURL(url)

        #逐一解析数据
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class_='item'):
            # print(item)
            data = [] #保存一部电影里的信息
            item = str(item)

            link = re.findall(fdlk,item)[0] #re库正则表达式寻找
            data.append(link)
            img = re.findall(fdimg,item)[0]
            data.append(img)

            tit = re.findall(fdtit,item)  #多个元素没有[0]
            if len(tit) == 2:
                ctit = tit[0]
                data.append(ctit)
                ftit = tit[1]
                data.append(ftit)
            else:
                data.append(tit)
                data.append(" ")

            dir = re.findall(fddir, item)[0]
            data.append(dir)
            rat = re.findall(fdrat, item)[0]
            data.append(rat)
            juN = re.findall(fdjuN, item)[0]
            data.append(juN)

            inq = re.findall(fdinq, item)
            if len(inq) != 0:
                data.append(inq)
            else:
                data.append(" ")

            datalist.append(data)

    print(datalist)
    return datalist



fdlk = re.compile(r'<a href="(.*?)">')
fdimg = re.compile(r'<img.*src="(.*?)" ',re.S)  #re.S省略换行符
fdtit = re.compile(r'<span class="title">(.*)</span>')
fddir = re.compile(r'<p class="">(.*)</p>',re.S)
fdrat = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
fdjuN = re.compile(r'<span>(\d*)人评价</span>')
fdinq = re.compile(r'<span class="inq">(.*)</span>')

os.remove('D:\douban.txt')
datalist = getdata(url)

# (r''): 忽视引用中所有特殊符号