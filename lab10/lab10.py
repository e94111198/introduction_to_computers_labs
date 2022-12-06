from flask import Flask, request 
from flask_cors import CORS 
app = Flask(__name__) #開啟工具
CORS(app) #導入function
key=[] #建list
value=[] #建list
@app.route('/',methods=['GET']) #若有get request傳到/執行下面function
def root0(): #函數
    return 'ok' #傳回
@app.route('/set',methods=['POST'])
def root1():
    data = request.form.to_dict() #接收body資料 轉成dict
    print(data)
    x=data['key'] in key #key有在list裡
    if x == True: #如果他正確
       return 'key exist' #傳回
    else: #否則
       key.append(data['key']) #新增元素
       value.append(data['value']) #新增元素
       return 'set success' #傳回
@app.route('/key_list',methods=['GET'])
def root2():
    return str(key)
@app.route('/get_value/<key0>',methods=['GET'])
def root3(key0):
    if key0 in key: #若key0有在list裡
       return value[key.index(key0)] #傳回值
    else: #否則
       return 'key not found'
@app.route('/update_value',methods=['POST'])
def root4(): 
    data2 = request.form.to_dict()
    print(data2)
    if data2['key'] in key:
       data2.setdefault('key','value') #更改
       return 'update success'
    else:
       return 'key not found'
@app.route('/delete/<key1>',methods=['GET'])
def root5(key1):
    if key1 in key:
       key.remove(key1) #移除
       return 'delete success'
    else:
      return 'key not found'
app.run(host="0.0.0.0", port=3000 ,debug=True) #執行
