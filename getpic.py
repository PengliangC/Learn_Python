# coding=utf-8
import urllib.request
import re
url = 'http://desk.zol.com.cn/'
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
