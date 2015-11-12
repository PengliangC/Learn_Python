# coding=gbk
#<a href="http://travel.163.com/food/#f=endnav">
import urllib.request
import re
url = 'http://tieba.baidu.com/p/2460150866'
file = 'd:/test.html'
reg = r'src="(.+?\.jpg)" pic_ext'
data = urllib.request.urlopen(url).read()
data=data.decode('utf-8')
r1 = re.compile(reg)
c_t = r1.findall(data)

print(c_t)