import matplotlib.pyplot as plt
import numpy as np

f = open('Temperature.txt', 'r')
all=[]
f.readline()
for line in f.readlines():
    line=line[5:]
    line=line.replace("\n", "")
    list=line.split(",")
    tem=[]
    for t in list:
        tem.append(float(t))
    all.append(tem)

fig = plt.figure(figsize=(15,6))
plt.subplot(1,2,1)
plt.subplots_adjust(wspace=0.12)
month=np.array(range(1,13))
plt.plot(month,all[0],label=2013)
plt.plot(month,all[1],label=2014)
plt.plot(month,all[2],label=2015)
plt.plot(month,all[3],label=2016)
plt.plot(month,all[4],label=2017)
plt.plot(month,all[5],label=2018)
plt.plot(month,all[6],label=2019)
plt.plot(month,all[7],label=2020)
plt.plot(month,all[8],label=2021)
plt.title('Tainan Monthly Mean Temperature From 2013 To 2021',fontsize=10)
plt.xlabel('Month')
plt.ylabel('Temperature in Degree C')
plt.xticks(range(1,13,1))
plt.yticks(range(16,32,2))
plt.legend(loc=8,fontsize=9)
plt.savefig('lab13_01.png', bbox_inches='tight') #儲存圖片

average=[]
for j in range(12):
    ave=[]
    for i in range(9):
        ave.append(all[i][j])
    tem=sum(ave)/9
    average.append(round(tem,2))
mean=sum(average)/12
mean=round(mean,2)
f.close()

plt.subplot(1,2,2)
plt.subplots_adjust(wspace=0.12)
month=np.array(range(1,13))
plt.plot(month,average,'-o',markerfacecolor=(1,0,0,0.75),markeredgecolor=(1,0,0,0.75))
plt.title('Tainan Monthly Mean Temperature Of 2013 To 2021',fontsize=10)
plt.xlabel('Month')
plt.ylabel('Temperature in Degree C')
plt.xticks(range(1,13,1))
plt.yticks(range(16,34,2))
for a,b in zip(month,average):
    plt.text(a,b+0.1,b,fontsize=9)
plt.axhline(y=mean,color='r',linestyle="--",label='Mean of 9 Years')
plt.text(1,mean+0.1,mean,fontsize=9)
plt.legend(loc=1,fontsize=7)
ax2 = plt.subplot(1,2,2)
extent = ax2.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
fig.savefig('lab13_02.png', bbox_inches=extent.expanded(1.2, 1.2))

plt.savefig('lab13_03.png')
plt.show()
