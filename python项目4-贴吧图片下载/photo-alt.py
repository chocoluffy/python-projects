#! /usr/bin/env python  
#coding:utf-8  
  
import urllib,re
import urllib.request  
  
def get_html(url):  
    page = urllib.request.urlopen(url)  
    html = page.read().decode('utf-8')
    return html  
  
def get_img(html):  
    reg = r'src="(.*?\.jpg)" bdwater='  
    imgre = re.compile(reg)  
    imglist = re.findall(imgre, html)  
    i = 0  
    for imgurl in imglist:  
        urllib.request.urlretrieve(imgurl, '%s.jpg'%i)  
        i+=1  
html = get_html('http://tieba.baidu.com/p/2166231880')  
# print (get_img(html))
open(r'girl-alt/'+'%03d.jpg', 'wb').write(get_img(html))