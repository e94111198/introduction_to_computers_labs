#大台南公車轉運站資訊
#https://data.gov.tw/dataset/53570

import pymysql #導入
import requests #導入

r = requests.get('https://data.tainan.gov.tw/dataset/63224a5d-8864-4440-b602-6dda51d39a5c/resource/d2f45fea-13f3-4c7a-87c6-baf02f392bfd/download/opendata.json')
#抓資料
list_of_dicts = r.json() 
db = pymysql.connect(host='localhost',port=3306,user='e94111198',password='0000',db='wordpress',charset='utf8mb4')
#數據連接
cursor = db.cursor() #創游標對象
for i in range(10): #迴圈
    a=list_of_dicts[i]['站名'] #找到"站名"對應的value
    b=list_of_dicts[i]['地址'] #找到"地址"對應的value
    c=list_of_dicts[i]['電話'] #找到"電話"對應的value
    d=list_of_dicts[i]['公車路線'] #找到"公車路線"對應的value
    sql="INSERT INTO 大台南公車轉運站資訊(站名,地址,電話,公車路線)VALUES(%s,%s,%s,%s)" #插入資料
    value = (a,b,c,d) 
    cursor.execute(sql,value)#執行
    db.commit() #導入
db.closed #關
