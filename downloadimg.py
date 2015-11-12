# -*- coding:utf-8 -*-  
import urllib.request  
path = "D:\\Download"  
url = "http://pic2.sc.chinaz.com/files/pic/pic9/201309/apic520.jpg"  
name ="C:\\projects\\PythonTest\\1.jpg"  
#保存文件时候注意类型要匹配，如要保存的图片为jpg，则打开的文件的名称必须是jpg格式，否则会产生无效图片  
conn = urllib.request.urlopen(url)  
f = open(name,'wb')  
f.write(conn.read())  
f.close()  
print('Pic Saved!') 