# print('hello')


# import urllib.request

# request=urllib.request.Request("http://www.baidu.com")
# response = urllib.request.urlopen(request)
# html=response.read()
# print (html)



# import urllib.request
# import http.cookiejar
# #声明一个CookieJar对象实例来保存cookie
# cookie = http.cookiejar.CookieJar()
# #利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
# handler=urllib.request.HTTPCookieProcessor(cookie)
# #通过handler来构建opener
# opener = urllib.request.build_opener(handler)
# #此处的open方法同urllib2的urlopen方法，也可以传入request
# response = opener.open('http://www.baidu.com')
# for item in cookie:
#     print ('Name = '+item.name)
#     print ('Value = '+item.value)

# import re

# pattern=re.compile(r'hello')

# res1=re.match(pattern,'hello')
# res2=re.match(pattern,'helloo aa')
# res3=re.match(pattern,'hello ss')

# if res1:
# 	print(res1.group())
# else:
# 	print('1fail')


# if res2:
# 	print(res2.group())
# else:
# 	print('2fail')

# if res3:
# 	print(res3.group())
# else:
# 	print('3fail')


import re
import urllib.request
import requests
import http.cookiejar

SAVE_DIR_PATH = 'E:/work/code/py/'
save = lambda url: open(SAVE_DIR_PATH + url[url.rfind('/')+1:], 'wb').write(requests.get(url).content)
zhihuurl="https://www.zhihu.com/question/25087008"


#设置保存cookie的文件，同级目录下的cookie.txt
filename = 'E:/work/code/py/cookie.txt'
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
# cookie = http.cookiejar.MozillaCookieJar(filename)
# #利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
# handler = urllib.request.HTTPCookieProcessor(cookie)
# #通过handler来构建opener
# opener = urllib.request.build_opener(handler)
# #创建一个请求，原理同urllib2的urlopen
# response = opener.open(zhihuurl)
# #保存cookie到文件
# cookie.save(ignore_discard=True, ignore_expires=True)



#创建MozillaCookieJar实例对象
cookielocal= http.cookiejar.MozillaCookieJar()
#从文件中读取cookie内容到变量
cookielocal.load(filename, ignore_discard=True, ignore_expires=True)

request=urllib.request.Request(zhihuurl)
opener1 = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookielocal))
response1 = opener1.open(request)
html=response1.read()
html=html.decode('utf-8')#python3
# print (html)

# request=urllib.request.Request(zhihuurl)
# response = urllib.request.urlopen(request)
# html=response.read()
# html=html.decode('utf-8')#python3
# print(html)
#
#
reg=r'src="(.+?\.jpg)"'
pattern = re.compile(reg)
allurl=re.findall(pattern,html)
for url in allurl:
	print ("imageurl=" + url)
	save(url)
