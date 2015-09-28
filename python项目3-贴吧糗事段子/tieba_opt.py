# -*- coding:utf-8 -*-
import urllib
import urllib.request
import re
import time

class QSBK:
	def __init__(self):
		self.pageindex=1
		self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
		# 初始化headers
		self.headers = { 'User-Agent' : self.user_agent }
		# 存放段子的变量， 每一个元素是每一页的段子们
		self.stories=[]
		# 存放程序是否继续运行的变量
		self.enable=False

	def getpage(self, pageindex):
		try:
			url = 'http://www.qiushibaike.com/hot/page/' + str(pageindex)
			request = urllib.request.Request(url, headers = self.headers)
			response = urllib.request.urlopen(request)
			content=response.read().decode('utf8')
			return content
		except urllib.request.URLError as e:
			if hasattr(e, "code"):
				print("连接糗事百科失败， 错误代码", e.code)
			if hasattr(e, "reason"):
				print("连接糗事百科失败，错误原因", e.reason) 

	def getpageitem(self, pageindex):
		pagecode=self.getpage(pageindex)
		if not pagecode:
			print("页面加载失败。。。")
			return None
		pattern = re.compile('<div.*?class="author.*?>.*?<a.*?</a>.*?<a.*?>(.*?)</a>.*?<div.*?class="content">(.*?)</div>.*?<div class="(.*?)">.*?<span class="stats-vote.*?class="number">(.*?)</i>',re.S)
		# 修改之后的话， 有输出3处数据， 分别是1、作者；2、内容加标题；3、检查是照片thumb吗；4、赞数
		items = re.findall(pattern,pagecode)
		pageStories=[]
		for item in items:
		# haveImg=re.search("img", item[3])
		# if not haveImg:
		# 	print(item[0],item[1],item[2],item[4])
			if item[2]=='thumb': #如果这个帖子是有照片的话， 我就暂时先跳过
				pass
			else:
				pageStories.append([item[0].strip(), item[1].strip(), item[3].strip()])
				return pageStories

	def loadpage(self):
		if self.enable==True:
			if len(self.stories)<2:
				pageStories=self.getpageitem(self.pageindex)
				if pageStories:
					self.stories.append(pageStories)
					self.pageindex+=1

	def getOneStory(self, pageStories, page):
		for story in pageStories:
			input_content= input()
			self.loadpage()
			if input_content=="Q":
				self.enable=False
				return 
			print("第{page}页\t发布人：{people}\n发布内容：{content}\n赞：{praise}\n".format(page=page, people=story[0], content=story[1], praise=story[2]))

	def start(self):
		print("正在读取糗事百科， 按回车查看新段子， Q键退出")
		self.enable=True
		self.loadpage()
		nowpage=0
		while self.enable:
			if len(self.stories)>0:
				pageStories=self.stories[0]
				nowpage+=1
				del self.stories[0]
				self.getOneStory(pageStories, nowpage)


spider=QSBK()
spider.start()

