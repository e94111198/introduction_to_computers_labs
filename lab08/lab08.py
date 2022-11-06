import os
str1=os.getcwd()
str1=str1[1:]
print(str1.split("/"))
print(os.listdir('/home/E94111198'))

f=open('e94111198.txt','w')
str1=os.getcwd()
str1=str1[1:]
str1=str1.split("/")
for i in range(len(str1)):
    print (str1[i],file=f)
print (sep='/n',file=f)
a=os.listdir('/home/E94111198')
for i in range(len(a)):
    print (a[i],file=f)
f=open('e94111198.txt','r')
f.close()
