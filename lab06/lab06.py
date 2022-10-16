def gcd(a, b): #自訂函數
    if a ==0 or b ==0: #若其一條件成立
      print("0沒有GCD") #顯示
    else: #否則
      c = max(a,b) #c為a,b較大數
      d = min(a,b) #d為a,b中較小數
      r=c%d #r為c除以d餘數
      if r==1: #若
         print (str(a)+"和"+str(b)+"互質") #輸出
      else: #否則
         while(r!=0): #條件成立執行迴圈
          c=d 
          d=r 
          r=c%d
         print (str(a)+"和"+str(b)+"的gcd="+str(d)) #輸出
#return GCD
ans1 = gcd(80, 20)
ans2 = gcd(10, 0)
ans3 = gcd(19, 20)
