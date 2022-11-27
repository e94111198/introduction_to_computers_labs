import socket #導入

HOST = '10.3.141.1' #IP位置
PORT = 8000 #分機

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #指定參數位址家族和協議
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #服務器socket被關閉後馬上釋放服務器端口
s.bind((HOST, PORT)) #綁定socket
s.listen(5) #監聽

print('Server started at: %s:%s' % (HOST, PORT)) #輸出
print('Waiting for connection...') #輸出

while True:  #迴圈
    conn, addr = s.accept() #接受客戶端連接 返回conn及客戶端IP位置
    print('Connected by ' + str(addr)) #輸出

    while True: #迴圈
        indata = conn.recv(1024) #1024:一次接收訊息的最大長度
        if len(indata) == 0: # connection closed
            conn.close()
            print('(%s:%s) closed connection' % (HOST, PORT)) #輸出
            print('Waiting for connection…') #輸出
            break
        print('(%s:%s):' % (HOST, PORT) + indata.decode()) #輸出

        outdata = indata.decode() #解碼
        conn.send(outdata.encode()) #編碼
