class Animal(): #建立類別
    def __init__(self, weight, mood): #定義建構式
      self.weight = weight
      self.mood = mood
    def feed(self): #定義方法
        pass #建立空白方法
    def walk(self):
        pass
    def bath(self):
        pass
class Dogs(Animal): #建立子類別
    def __init__(self, weight, mood):
      super().__init__(weight,mood)
    def feed(self,n_feed): #定義方法 裡面有n_feed參數
      super().feed(n_feed)
    def walk(self,n_walk):
      w=[-n_walk*0.2,n_walk*2]
      return w
    def bath(self,n_bath):
      b=[0,-n_bath*2]
      return b
    def printf(self, n_feed, n_walk, n_bath):
      w=self.walk(n_walk)
class Shiba(Dogs):
    def __init__(self, weight, mood):
      super().__init__(weight,mood)
    def feed(self,n_feed): #定義方法 裡面有n_feed參數
      f=[n_feed*0.3, n_feed*5] #立陣列
      return f #回傳
    def printf(self, n_feed, n_walk, n_bath):
      f=self.feed(n_feed) #把值叫出來
      w=self.walk(n_walk)
      b=self.bath(n_bath)
      self.weight=self.weight+f[0]+w[0] #初始值和後來加總
      self.mood=self.mood+f[1]+w[1]+b[1]
      def mood_constraint(self, constraint):
        self.constr = constr
      if self.mood  > 90:
         print ("柴犬現在的體重=",str(self.weight),"kg,心情",str(self.mood))  
         print ("所以,柴犬現在的心情90")
      print ("mood最高只能為=90")
shiba= Shiba(5,70)
shiba.printf(20,10,3)
