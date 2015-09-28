import requests  
import lxml.html  

# 第一版本为下载妹子的照片 
page = requests.get('http://tieba.baidu.com/p/2166231880').text  
doc = lxml.html.document_fromstring(page)  
for idx, el in enumerate(doc.cssselect('img.BDE_Image')):  
    with open(r'girl/'+'%03d.jpg' % idx, 'wb') as f:  
        f.write(requests.get(el.attrib['src']).content)  

# 赵丽颖zhaopian
# page = requests.get('http://tieba.baidu.com/p/3759513269').text  
# doc = lxml.html.document_fromstring(page)  
# for idx, el in enumerate(doc.cssselect('img.BDE_Image')):  
#     with open(r'girl/'+'%03d.jpg' % idx, 'wb') as f:  
#         f.write(requests.get(el.attrib['src']).content)  