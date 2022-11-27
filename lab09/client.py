import socket #導入

HOST = '10.3.141.1' #IP位置
PORT = 8000 #分機

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #指定參數位址家族和協議
s.connect((HOST, PORT)) #指定要串接的HOST,PORT

print('connected to %s:%s'%(HOST, PORT)) #輸出
while True: #迴圈
      outdata = input('Send: ') #輸入
      s.send(outdata.encode()) #傳送資料過去
    
      indata = s.recv(1024) #最大長度1024
      if outdata=='EXIT': #若輸入EXIT
          s.close() #close
          print('Closed connection.') #輸出
          break
      print('Echo: '+indata.decode()) #輸出
