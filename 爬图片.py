import requests
from bs4 import BeautifulSoup
import os
import time
import random
from urllib import request,parse
import urllib.request
def denglu(url):
    date={
        'Host': 'max-l.mediav.com',
        'cookie': 'Hm_lvt_cb7f29be3c304cd3bb0c65a4faa96c30=1593671101,1593672512; Hm_lpvt_cb7f29be3c304cd3bb0c65a4faa96c30=1593673214',
        'user - agent': random.choice(meizi_headers),
    }
    html=requests.post(url,headers=date)
    # print(html.text)
    return html.text
def fenxi(a):
    html_lxml=BeautifulSoup(html,'lxml')
    html_ul=html_lxml.find('ul',id='pins')
    html_li=html_ul.find_all('li')
    for tag in html_li:
        tag_name=tag.find('span').a
        print(tag_name.get_text())
        print(tag_name['href'])
        tag_href=tag_name['href']
        path="F:/图片/"+tag_name.get_text()
        os.mkdir(path)
        tupian(tag_href,path)

def tupian(a,path):
    html2=denglu(a)
    html_lxml2 = BeautifulSoup(html2, 'lxml')
    html_page=html_lxml2.find('div',class_='pagenavi')
    html_total=html_page.find_all('a')[-2].span.get_text()
    print(html_total)
    for i in range (1,int(html_total)):
        page=str(a+'/'+str(i))
        page2=denglu(page)
        page_lxml=BeautifulSoup(page2,'lxml')
        page_jpg=page_lxml.find('div',class_='main-image').p.a.img['src']
        print("正在下载----"+path+"下的图片"+str(i))
        print(page_jpg)
        download(page_jpg,path,i)
def download(page_jpg,path,i):
    date = {
        'Referer': page_jpg,
        'User-Agent': random.choice(meizi_headers),
    }
    #延时
    time.sleep(random.randint(1, 3))
    r=requests.get(page_jpg,headers=date)
    path2=path+'/'+str(i)+'.jpg'
    with open(path2,'wb') as img:
        img.write(r.content)
        print("----------------------下载完成第"+str(i)+"张照片------------------")
if __name__=="__main__":
    url = "https://www.mzitu.com/"
    meizi_headers=[
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
        "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
        'Opera/9.25 (Windows NT 5.1; U; en)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
        'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
        'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
        'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
        "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
        "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0",
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
    ]
    html=denglu(url)
    fenxi(html)



