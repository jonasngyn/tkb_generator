#!/usr/bin/env python3
import requests
import lxml.html as lh
import pandas as pd
from prettytable import PrettyTable

url='http://thpt-huynhmandat-kiengiang.edu.vn/TKB/tkb_class_14_0.html'
#request
page = requests.get(url)
#Download
doc = lh.fromstring(page.content)
#getAllDataOfPage



tr_elements = doc.xpath('//tr')

myList=[]
for t in range(1,6):
    (myList.append(str(tr_elements[t].text_content()).split("\n")))

    
t = PrettyTable() 
t.title = 'Thoi khoa bieu'
Table=['Thu 2','Thu 3','Thu 4','Thu 5','Thu 6','Thu 7']

Ngay=[[],[],[],[],[],[]]
for i in range(0,5):
    for j in range(2,8):
        #Ngay.append(str(" "))
        Ngay[j-2].append(myList[i][j]);
        
for i in range (0,6):
    t.add_column(Table[i],Ngay[i])

print(t);

