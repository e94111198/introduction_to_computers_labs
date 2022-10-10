dict0 = {"index":["國文","英文","數學","自然","社會"],"StuA":[50,60,70,80,90],"StuB":[57,86,73,82,43],"StuC":[97,96,86,97,83]}
#建立一個叫dict0的字典
print (dict0) #輸出字典
grade1 = dict0.get("StuA") #取StuA鍵的值
grade2 = dict0.get("StuB")
grade3 = dict0.get("StuC")
total=0 #令為0
for i in range(0,5): #循環五次
    total = total + grade1[i] #將成績加總
avg = total / 5 #取平均
print ("A學生平均成績:"+ str(avg)) #輸出字串
total1=0
for i in range(0,5):
    total1 = total1 + grade2[i]
avg1 = total1 / 5
print ("B學生平均成績:"+ str(avg1))
total2=0
for i in range(0,5):
    total2 = total2 + grade3[i]
avg2 = total2 / 5
print ("C學生平均成績:"+ str(avg2))
score=[] #建一個list
for i in range(0,5): #循環五次
    score.append((grade1[i]+grade2[i]+grade3[i])/3) #增加list元素(成績的平均值)
index1=list(dict0.get("index")) #以list轉換為串列
print (index1[0]+"平均成績"+str(score[0]))
print (index1[1]+"平均成績"+str(score[1]))
print (index1[2]+"平均成績"+str(score[2]))
print (index1[3]+"平均成績"+str(score[3]))
print (index1[4]+"平均成績"+str(score[4]))
