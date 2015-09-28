# -*- coding:utf-8 -*-
import urllib
import urllib.request
import re
 
page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
	request = urllib.request.Request(url,headers = headers)
	response = urllib.request.urlopen(request)
# print(response.read().decode('utf8'))

# 我们可以看到，每一个段子都是<div class=”article block untagged mb15″ id=”…”>…</div>包裹的内容。

# 现在我们想获取发布人，发布日期，段子内容，以及点赞的个数。不过另外注意的是，段子有些是带图片的，如果我们想在控制台显示图片是不现实的，所以我们直接把带有图片的段子给它剔除掉，只保存仅含文本的段子。

# 所以我们加入如下正则表达式来匹配一下，用到的方法是 re.findall 是找寻所有匹配的内容。方法的用法详情可以看前面说的正则表达式的介绍。

	content=response.read().decode('utf8')
	# pattern = re.compile('<div.*?class="author.*?>.*?<a.*?</a>.*?<a.*?>(.*?)</a>.*?<div.*?class="content".*?title="(.*?)">(.*?)</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
	pattern = re.compile('<div.*?class="author.*?>.*?<a.*?</a>.*?<a.*?>(.*?)</a>.*?<div.*?class="content">(.*?)</div>.*?<div class="(.*?)">.*?<span class="stats-vote.*?class="number">(.*?)</i>',re.S)
	# 修改之后的话， 有输出3处数据， 分别是1、作者；2、内容加标题；3、检查是照片thumb吗；4、赞数
	items = re.findall(pattern,content)
	for item in items:
		# haveImg=re.search("img", item[3])
		# if not haveImg:
		# 	print(item[0],item[1],item[2],item[4])
		if item[2]=='thumb': #如果这个帖子是有照片的话， 我就暂时先跳过
			pass
		else:
			print(item[0], item[1], item[3])
except urllib.request.URLError as e:
	if hasattr(e, "code"):
		print(e.code)
	if hasattr(e, "reason"):
		print(e.reason) 


# 现在正则表达式在这里稍作说明

# 1）.*? 是一个固定的搭配，.和*代表可以匹配任意无限多个字符，加上？表示使用非贪婪模式进行匹配，也就是我们会尽可能短地做匹配，以后我们还会大量用到 .*? 的搭配。

# 2）(.*?)代表一个分组，在这个正则表达式中我们匹配了五个分组，在后面的遍历item中，item[0]就代表第一个(.*?)所指代的内容，item[1]就代表第二个(.*?)所指代的内容，以此类推。

# 3）re.S 标志代表在匹配时为点任意匹配模式，点 . 也可以代表换行符。

# 关键点是，由于糗事百科的构架已经有改动， 于是正则表达式需要重新写！