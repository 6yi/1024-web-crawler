import requests
import re
import os
from lxml import etree
try:
    flag=1
    while flag<=270:
        base_url='https://t66y.com/'
        page_url='https://t66y.com/thread0806.php?fid=16&search=&page='+str(flag)
        get=requests.get(page_url)
        article_url=re.findall(r'<h3><a href="(.*)" target="_blank" id="">(?!<.*>).*</a></h3>',str(get.content,'gbk',errors='ignore'))
        for url in article_url:
            tittle=['default']
            getpage=requests.get(str(base_url)+str(url))
            tittle=re.findall(r'<h4>(.*)</h4>',str(getpage.content,'gbk',errors='ignore'))
            file=tittle[0]
            if  os.path.exists(file)==False:
                os.makedirs(file)
                tree=etree.HTML(str(getpage.content,'gbk',errors='ignore'))
                img_url=tree.xpath('//input/@data-src')
                filename=1
                for download_url in img_url:
                    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36Name','Referer':'https://t66y.com'}
                    req=requests.get(url=download_url,headers=headers)
                    file_path='./'+file+"/"+str(filename)+'.jpg'
                    with open(file_path,'wb') as f:
                        print('开始下载：'+file+"----第"+str(filename)+"张图片")
                        f.write(req.content)
                        filename+=1
        print(file+"--下载完成")
except:
    print("崩了，兄弟")


