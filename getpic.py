# coding=utf-8
#<a href="http://travel.163.com/food/#f=endnav">
import urllib.request
import re
url = 'http://tieba.baidu.com/p/2460150866'
filename='C:\\projects\\PythonTest\\pic\\'
reg = r'src="(.+?\.jpg)" pic_ext'
data = urllib.request.urlopen(url).read()
data=data.decode('utf-8')
r1 = re.compile(reg)
c_t = r1.findall(data)
print("pic len：",len(c_t))

for num in list(range(len(c_t))):
    fn=filename+str(num)+'.jpg'
    
    conn = urllib.request.urlopen(c_t[num]) 
    f = open(fn,'wb')  
    f.write(conn.read())  
    f.close() 
    print('saved',num+1)	
    num=num+1
print('Pic Saved!') 
	
#for name in c_t:
#    print(name)
