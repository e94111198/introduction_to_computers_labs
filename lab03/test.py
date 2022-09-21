a =int(input("1.please input a number:"))#輸入數字並由字串轉為整數,給代號a
if a % 2 ==0:#若a除二餘0
   print ("this is even")#顯示字串
else:#否則
   print ("this is odd")#顯示另個字串
character = input("2.please input your student ID first character:")#輸入字串叫他character
b =int(input("3.please input your student ID last eight numbers:"))#輸入學號並由字串轉為整數 給代號b
if b % 2 == 0:#若b除2等於零
   print ("your student ID number is even")#顯示字串
else:#否則
   print ("your student ID number is odd")#顯示字串
print ("your student ID number is:"+ character + str(b))#顯示字串加上之前輸入的字串 其中數字要改為字串
