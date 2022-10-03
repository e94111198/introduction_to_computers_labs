grade1 = []
print ("開始輸入A學生的成積，請依照 國文、英文、數學、自然、社會 的順序輸入:")
for i in range(5):
    grade1.append(input())
print ("A學生的成績")
print ("國文:"+grade1[0]+"、英文:"+grade1[1]+"、數學:"+grade1[2]+"、自然:"+grade1[3]+"、社會:"+grade1[4])
print ("")
grade2 = []
print ("開始輸入B學生的成積，請依照 國文、英文、數學、自然、社會 的順序輸入:")
for i in range(5):
    grade2.append(input())
print ("B學生的成績")
print ("國文:"+grade2[0]+"、英文:"+grade2[1]+"、數學:"+grade2[2]+"、自然:"+grade2[3]+"、社會:"+grade2[4])
print ("")
grade3 = []
print ("開始輸入C學生的成積，請依照 國文、英文、數學、自然、社會 的順序輸入:")
for i in range(5):
    grade3.append(input())
print ("C學生的成績")
print ("國文:"+grade3[0]+"、英文:"+grade3[1]+"、數學:"+grade3[2]+"、自然:"+grade3[3]+"、社會:"+grade3[4])
print ("")
total =0
for i in range(0,5):
    total = total + eval(grade1[i])
avg = total / 5
print ("A學生平均成績:{}".format(avg))
total2 =0
for i in range(0,5):
    total2 = total2 + eval(grade2[i])
avg = total2 / 5
print ("B學生平均成績:{}".format(avg))
total3 =0
for i in range(0,5):
    total3 = total3 + eval(grade3[i])
avg = total3 / 5
print ("C學生平均成績:{}".format(avg))
c_sum = int(grade1[0])+int(grade2[0])+int(grade3[0])
e_sum = int(grade1[1])+int(grade2[1])+int(grade3[1])
m_sum = int(grade1[2])+int(grade2[2])+int(grade3[2])
sc_sum = int(grade1[3])+int(grade2[3])+int(grade3[3])
so_sum = int(grade1[4])+int(grade2[4])+int(grade3[4])
print ("國文平均成績:",c_sum/3)
print ("英文平均成績:",e_sum/3)
print ("數學平均成績:",m_sum/3)
print ("自然平均成績:",sc_sum/3)
print ("社會平均成績:",so_sum/3)
