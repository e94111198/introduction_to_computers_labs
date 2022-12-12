import json
def Perm(arrs): #函式
   if (len(arrs))==1: #如果長度為1
      return [arrs] #返回
   result = []  #給一個list儲存所有結果
   for j in range(len(arrs)): #迴圈
      rest_arrs = arrs[:j]+arrs[j+1:] #取得i之外的  
      rest_lists = Perm(rest_arrs)  #其他繼續排
      lists = [] #list
      for term in rest_lists:
         lists.append(arrs[j:j+1]+term) #找出組合
      result += lists #把這個組合加到所有可能組合的list
   return result

def BF(input): #函式
   N = len(input) #幾份工作/人
   who=[] #list
   a=0
   for i in range(N): #迴圈幾次
      who.append(a)  
      a+=1 #用0.1.2.3...數字當人的代號
   result=Perm(who) #帶入函式找出人的排列組合

   time = [] #list    
   for per in result: # 對每個排列組合
      temp_cost = 0 #總和先設為0
      for i in range(len(per)): # 對每個組合中的人
         current_job=i # 取得工作
         current_people = per[i]  # 取得人        
         current_cost=input[current_job][current_people]  # 取得某人做某事的cost
         temp_cost += current_cost #每個人時間加總
      time.append(temp_cost) #列出全部組合時間
   cost = min(time) #找出最小時間
   assignment = result[time.index(min(time))] #找出式哪個組合
   return assignment, cost

# main
with open('input.json', 'r') as inputFile: #打開檔案
   data = json.load(inputFile) # load data
   for key in data:
      input = data[key] # load each input
      
      # show input data and number of the Tasks
      # print(input)

      # Brute Force Algorithm
      assignment, cost = BF(input) 
      print('Question: ' + str(key)) #輸出
      print('Assignment:', assignment) #輸出
      print('Cost:', cost) #輸出
      print()