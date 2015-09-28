通过按enter使得出现下个笑话段子
知识点：
1、正则表达式的使用， 严格按照审查元素里面的网页内元素的格式来设计正则表达式， 
.*? 表示非贪婪查询下一个元素
(.*?) 表示用于返回那个地方的元素
按照审查元素里面的规律来找， 这个例子， 主要根据 author, content, thumb, stats的相对位置和其周围的元素对其定位。
使用方法是调用re的函数包， 其中有re.compile, pattern, sub
仔细总结关于正则表达式包函数的应用
2、面向对象的coding， 将函数功能改造成为面向对象的使用， getpage, loadpage等等
还有多练习
3、python3的request包， 其实就是代替了原有的urllib2， 于是都是用
urllib.request.urlopen(link).read().decode('utf8') 来读取html5的代码页
