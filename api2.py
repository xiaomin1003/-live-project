import requests
import re
from bs4 import BeautifulSoup
def gethtml(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding='utf-8'
        return r.text
    except:
        return ""
def getcon(html):
    bsObj=BeautifulSoup(html)
    divlist=bsObj.find_all('div',{'class':'bk_show_info'})
    allbook=[]
    for divs in divlist:
        book_info=[]
        book_name=divs.h4['data-name']
        book_info.append(book_name)
        p_list=divs.find_all('p')
        for p_content in p_list:
            book_info.append(p_content.string)
        allbook.append(book_info)
    for book in allbook:
        print(book)
html=gethtml('http://www.bjjqe.com/')
getcon(html)
