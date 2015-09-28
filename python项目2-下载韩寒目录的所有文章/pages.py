girl# <a title="《论电影的七个元素》——关于我对电影的一些看法以及《后会无期》的一些消息" target="_blank" href="http://blog.sina.com.cn/s/blog_4701280b0102eo83.html">《论电影的七个元素》——关于我对电…</a>
#coding: utf-8
# 第一步得到文章的链接, given the html link, output local copy
import urllib.request

# str0='<a title="《论电影的七个元素》——关于我对电影的一些看法以及《后会无期》的一些消息" target="_blank" href="http://blog.sina.com.cn/s/blog_4701280b0102eo83.html">《论电影的七个元素》——关于我对电…</a>'
# title=str0.find(r'<a title')
# href=str0.find(r'href=')
# html=str0.find(r'.html')
# link=str0[href+6:html+5]
# print(link)
# content= urllib.request.urlopen(link).read().decode('utf8')
# print(content)
# file_name_index=link.find(r'blog_')
# file_name=link[file_name_index:]
# print(file_name)
# open(file_name, 'w').write(content)
# 以上就把韩寒博客的第一篇文章保存到本地文件夹

# 一下将博文目录的内容读下, 通过创建一个目录的list， 将每一页的关键页链接存进list里面， 用一个循环

pages_list=['']*10
first_page='http://blog.sina.com.cn/s/articlelist_1191258123_0_1.html'
pages_list[0]=first_page
key_pos=first_page.find(r'_0_')
i=0
for i in range(1, 10):
	new_page=first_page[:first_page.find(r'_0_')]+'_0_'+str(i)+'.html'
	pages_list[i]=new_page

print(pages_list)

urls=['']*500

# 对于每一个页面， 用一个小技巧使得可以持续的对不同页面的如第二页， 第五页的内容拿到
for page in range(len(pages_list)):
	con=urllib.request.urlopen(pages_list[page]).read().decode('utf8')

	# print(con)
	title=con.find(r'<a title')
	href=con.find(r'href=', title)
	html=con.find(r'.html', href)

	turns=50*page
	while title!=-1 and href!=-1 and html!=-1 and turns<50*(page+1):
		title=con.find(r'<a title', html)
		href=con.find(r'href=', title)
		html=con.find(r'.html', href)
		url=con[href+6:html+5]
		urls[turns]=url
		turns+=1
		print(url)
# if str.find() find nothing, then return -1
file_index=0
while file_index<500:
	if urls[file_index]=='':
		file_index+=1
	content=urllib.request.urlopen(urls[file_index]).read().decode('utf8')
	file_name_index=urls[file_index].find(r'blog_')
	file_name=urls[file_index][file_name_index:]
	open(r'hanhan/'+file_name,'w+').write(content)
	print('downloading '+file_name+'...')
	file_index+=1
