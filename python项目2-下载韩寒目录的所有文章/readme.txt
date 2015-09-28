爬虫来爬去韩寒博客里面各个页数的文章， 这里爬去的是前面的500篇
知识点：
1、通过对不同页码的稍微修改， 如最后一个数字的不同， 就可以跳转到下一个页面。
2、对于string的处理， 使用str.find(r'pattern')
来返回这个pattern在这个string里面第一次出现的index， 然后可以利用string的切片来获取想要的部分， 同时学习到的方法是， 利用python3里面自带的help(str.find())在看这个函数的接口
3、将收集到的内容保存到本地， 利用文件操作的函数open, write等等， 
open(r'hanhan/'+file_name, 'w+').write(content)
首先在当前目录下应该有hanhan这个文件夹， 然后写入这些内容，这些content会以html文件的形式存在文件夹里面。 希望只获取内容的话， 要利用正则表达式！也就是项目2里面所用到的知识。