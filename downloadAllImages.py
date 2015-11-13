import re
import urllib.request
url = 'http://www.ivsky.com/bizhi/'
filename='C:\\projects\\PythonTest\\pic\\'
reg1 =r'src="(.+\.jpg)"'
reg2 = r'href="(.+?\.html+?)"'

def downloadimage(urlDownImage,address):
    conn = urllib.request.urlopen(urlDownImage) 
    f = open(address,'wb')  
    f.write(conn.read())  
    f.close()
	
def getData(reg,urlGet):
    data = urllib.request.urlopen(urlGet).read()
    data=data.decode('utf-8')
    r1 = re.compile(reg)
    c_t = r1.findall(data)
    return c_t


def downIt():
    urlData=getData(reg2,url)
    
    for urlNum in list(range(len(urlData))):
        urlNew=urlData[urlNum]
        print(urlNew)
        #urlImageData=getData(reg1,urlNew)		
        #for urlImageNum in list(range(len(urlImageData))):
            #urlImageNew=urlImageData[urlImageNum]
            #print(urlImageNew)
            #fn=filename+str(fileNum)+'.jpg'
            #downloadimage(urlImageNew,fn)
            #fileNum=fileNum+1



def downOnlyOneUrl():
    urlImageData=getData(reg1,url)
    for num in list(range(len(urlImageData))):
        #print(urlImageData[num])
        fn=filename+str(num)+'.jpg'
        
        downloadimage(urlImageData[num],fn)
        print('saved',num+1)
        num=num+1  
				  

downOnlyOneUrl()	
	
	
	