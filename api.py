import requests
from bs4 import BeautifulSoup
import re
import json
def getkeyword(keyword):
    url='http://www.baidu.com/s?wd='+keyword
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding='UTF-8'
        return r.text
    except:
        return ""
def parserlinks(html):
    soup=BeautifulSoup(html,"html.parser")
    links=[]
    for div in soup.find_all('div',{'data-tools':re.compile('title')}):
        data=div.attrs['data-tools']
        d=json.loads(data)
        links.append(d['title'])
    return links
def main():
    html=getkeyword('福州最佳美食餐厅搜索')
    ls=parserlinks(html)
    count=1
    with open('15.txt','w')as fd:
        for i in ls:
            fd.write('[')
            fd.write(str(count))
            fd.write(']')
            fd.write(i)
            fd.write('\n')
            count+=1
        print('写入文件成功！')
main()