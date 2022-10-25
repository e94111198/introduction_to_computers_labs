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
      self.weight = weight
      self.mood = mood
    def feed(self,n_feed): #定義方法 裡面有n_feed參數
      f=[n_feed*0.2, n_feed] #建立陣列
      return f #回傳
    def walk(self,n_walk):
      w=[-n_walk*0.2,n_walk*2]
      return w
    def bath(self,n_bath):
      b=[n_bath*0,-n_bath*2]
      return b
    dogsweight=0
    dogsmood=0
    def printf(self, n_feed, n_walk, n_bath):
      f=self.feed(n_feed) #把值叫出來
      w=self.walk(n_walk)
      b=self.bath(n_bath)
      dogsweight=self.weight+f[0]+w[0]+b[0] #初始值和後來加總
      dogsmood=self.mood+f[1]+w[1]+b[1]
      print("狗狗現在的體重="+str(dogsweight)+"kg,心情"+str(dogsmood)) #輸出
class Cats(Animal):
    def __init__(self, weight, mood):
      self.weight = weight
      self.mood = mood
    def feed(self,n_feed):
      f=[n_feed*0.1, n_feed]
      return f
    def walk(self,n_walk):
      w=[-n_walk*0.1,-n_walk*1]
      return w
    def bath(self,n_bath):
      b=[n_bath*0,-n_bath*2]
      return b
    catsweight=0
    catsmood=0
    def printf(self, n_feed, n_walk, n_bath):
      f=self.feed(n_feed)
      w=self.walk(n_walk)
      b=self.bath(n_bath)
      catsweight=self.weight+f[0]+w[0]+b[0]
      catsmood=self.mood+f[1]+w[1]+b[1]
      print("貓貓現在的體重="+str(catsweight)+"kg,心情"+str(catsmood))

dog = Dogs(4.8, 65) #傳入參數
dog.printf(18, 10, 4)

cat = Cats(8.2, 60)
cat.printf(40, 7, 1)

