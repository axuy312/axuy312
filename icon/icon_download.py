#載入requests套件
import requests
#需要載入os套件，可處理文件和目錄
import os
#創建目錄
os.makedirs('./icon/',exist_ok=True)
url='https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/'

links = ["html","css","javascript","php","mysql","java","cpp","firebase","android","swift","python","git"]

for n in links:
    r=requests.get(url+"/"+n+"/"+n+".png")
    with open('./icon/'+n+".png",'wb') as f:
    #將圖片下載下來
        f.write(r.content)
