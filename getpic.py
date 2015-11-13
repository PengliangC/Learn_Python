# coding=utf-8
import urllib.request
import re
#url = 'http://tieba.baidu.com/p/2460150866'
url='http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E7%99%BE%E5%BA%A6'
filename='C:\\projects\\PythonTest\\pic\\'
#reg = r'src="(.+?\.jpg)" pic_ext'
reg = r'src="(.+\.jpg)"'
data = urllib.request.urlopen(url).read()
data=data.decode('utf-8')
r1 = re.compile(reg)
c_t = r1.findall(data)
print("pic len：",len(c_t))

def downloadimage(url,address):
    conn = urllib.request.urlopen(url) 
    f = open(address,'wb')  
    f.write(conn.read())  
    f.close()

for num in list(range(len(c_t))):
    fn=filename+str(num)+'.jpg' 
    downloadimage(c_t[num],fn)
    print('saved',num+1)	
    num=num+1
#f.close()

print('Pic Saved!') 


#for name in c_t:
#    print(name)
