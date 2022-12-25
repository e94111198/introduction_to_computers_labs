import matplotlib.pyplot as plt #匯入模組
import numpy as np #匯入模組

f = open('Temperature.txt', 'r') #讀檔
all=[] #list
f.readline() #讀一行
for line in f.readlines(): #一次讀一行
    line=line[5:] #前四個字不取
    line=line.replace("\n", "") #刪掉\n
    list=line.split(",") #用，分開
    tem=[] #list
    for t in list: #list裡面的元素
        tem.append(float(t)) #用浮點數的格式加到tem這個list裡
    all.append(tem) #tem再加到all list裡

fig = plt.figure(figsize=(15,6)) # 建立(15,6)大小圖表
plt.subplot(1,2,1) #子圖1
plt.subplots_adjust(wspace=0.12) #兩個子圖中間的空隙
month=np.array(range(1,13)) #month=1~12
plt.plot(month,all[0],label=2013) #2013年的折線圖和圖例
plt.plot(month,all[1],label=2014)
plt.plot(month,all[2],label=2015)
plt.plot(month,all[3],label=2016)
plt.plot(month,all[4],label=2017)
plt.plot(month,all[5],label=2018)
plt.plot(month,all[6],label=2019)
plt.plot(month,all[7],label=2020)
plt.plot(month,all[8],label=2021)
plt.title('Tainan Monthly Mean Temperature From 2013 To 2021',fontsize=10) #標題字及大小
plt.xlabel('Month') #x軸標籤
plt.ylabel('Temperature in Degree C')
plt.xticks(range(1,13,1)) #x軸刻度
plt.yticks(range(16,32,2))
plt.legend(loc=8,fontsize=9) #圖例位置大小
plt.savefig('lab13_01.png', bbox_inches='tight') #儲存圖片

average=[] #存每月平均的list
for j in range(12): #迴圈12次
    ave=[] #存不同年的同個月溫list
    for i in range(9): #迴圈9次
        ave.append(all[i][j]) #加進list
    tem=sum(ave)/9 #算平均
    average.append(round(tem,2)) #四捨五入到小數點第2位
mean=sum(average)/12 #平均
mean=round(mean,2) #四捨五入到小數點第2位
f.close() #關檔

plt.subplot(1,2,2) #子圖2
plt.subplots_adjust(wspace=0.12) #兩個子圖中間的空隙
month=np.array(range(1,13)) #month=1~12
plt.plot(month,average,'-o',markerfacecolor=(1,0,0,0.75),markeredgecolor=(1,0,0,0.75)) #折線圖、點(中間、邊框)、點顏色、透明度
plt.title('Tainan Monthly Mean Temperature Of 2013 To 2021',fontsize=10) #標題字及大小
plt.xlabel('Month') #x軸標籤
plt.ylabel('Temperature in Degree C')
plt.xticks(range(1,13,1)) #x軸刻度
plt.yticks(range(16,34,2))
for a,b in zip(month,average):
    plt.text(a,b+0.1,b,fontsize=9) #顯示數值標籤(x位置、Y位置、顯示y數值、大小)
plt.axhline(y=mean,color='r',linestyle="--",label='Mean of 9 Years') #水平線位置、顏色、樣式、圖例
plt.text(1,mean+0.1,mean,fontsize=9) #顯示數值標籤
plt.legend(loc=1,fontsize=7) #圖例位置大小
ax2 = plt.subplot(1,2,2) 
extent = ax2.get_window_extent().transformed(fig.dpi_scale_trans.inverted()) #擷取子圖二的位置
fig.savefig('lab13_02.png', bbox_inches=extent.expanded(1.2, 1.2)) #儲存子圖二圖片(位置擴張20%)

plt.savefig('lab13_03.png') #儲存圖片
plt.show() #顯示圖像