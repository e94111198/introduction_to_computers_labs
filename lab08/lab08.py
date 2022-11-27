import os #導入模組
str1=os.getcwd() #取得資料夾路徑
str1=str1[1:] #不要第一條斜線
print(str1.split("/")) #用斜線分隔印出list
print(os.listdir('/home/E94111198')) #列出指定路徑資料夾內所有內容

f=open('e94111198.txt','w') #寫檔
str1=os.getcwd()
str1=str1[1:]
str1=str1.split("/")
for i in range(len(str1)): #重複
    print (str1[i],file=f) #寫入
print (sep='/n',file=f) #用換行分隔
a=os.listdir('/home/E94111198') 
for i in range(len(a)):
    print (a[i],file=f)
f=open('e94111198.txt','r') #讀檔
f.close() #結束
