#! /usr/bin/env python  
#coding:utf-8  
  
import urllib,re
import urllib.request  
  
def get_html(url):  
    page = urllib.request.urlopen(url)
    data=page.read()
    data[872] = data[872].decode('latin-1')  
    html = data.decode('utf-8')
    return html  
  
def get_img(html):  
    # reg = r'src="(.*?\.jpg)" bdwater='  
    # reg=r'src="(.*?\.jpg)">.*?</a>'
    reg=r'<img alt=.*?src="(.*?)">'
    imgre = re.compile(reg)
    print(imgre)  
    imglist = re.findall(imgre, html)
    print(imglist)
    i = 0  
    for imgurl in imglist:  
        # urllib.request.urlretrieve(imgurl, '%s.jpg'%i, callbackfunc)
        urllib.request.urlretrieve(imgurl, './lofter/{0}.jpg'.format(i), callbackfunc)
        i+=1  
html = get_html('http://blog.163.com/jonas_hwang/blog/static/20480323020153124528637/')
print(get_img(html))
# print (get_img(html))


def callbackfunc(blocknum, blocksize, totalsize):
    '''回调函数
    @blocknum: 已经下载的数据块
    @blocksize: 数据块的大小
    @totalsize: 远程文件的大小
    '''
    percent = 100.0 * blocknum * blocksize / totalsize
    if percent > 100:
        percent = 100
    print ("%.2f%%"% percent)