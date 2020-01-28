# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 22:55:26 2019

@author: 97654
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
from IPython.display import display

mpl.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['savefig.dpi'] =100#像素
plt.rcParams['figure.dpi'] = 100#分辨率

data1=pd.read_csv('zhenxing2017.csv')
data2=pd.read_csv('zhenxing2018a.csv')
data3=pd.read_csv('zhenxing2018b.csv')
data1.info
display(data1.head(2))
data4=data1.append(data2,ignore_index=True)
data=data4.append(data3,ignore_index=True)
x=list(data)
data1=data.drop([x[0],x[1]],axis=1)
data=data[[x[0],x[1],x[2],x[3],x[8],x[9],x[10],x[12],x[21],x[22],x[23],x[24],x[25],x[26],x[27],x[32]]]
data.to_csv('zhengxing.csv/xlsx')#读出csv/xlsx文件

x=list(data)
y1=data[x[1]]
y2=data[x[2]]

data=data.drop('column name', axis=1)#删除一列

data=pd.read_csv('zhenxing.csv')
data=data.drop('Unnamed: 0', axis=1)
data.rename(columns={'Unnamed: 0':'总价'},inplace = True)
x=list(data)
data[x[1]]=pd.to_datetime(data[x[1]])
data1=data[[x[1],x[14]]]
data1=data1.set_index(x[1])
data2=data1.resample('M').sum().to_period('M')
data3=data2.reset_index()

for i in range(len(data)):
    if data[x[12]][i]!=data[x[15]][i]:
       data[x[14]][i]=data[x[11]][i]*data[x[15]][i]
    else:
       continue
for i in range(len(data)):
    if data[x[3]][i]!='销售订单':
        data[x[14]][i]=0
    else:
        continue
    
f,ax1=plt.subplots(1,1,figsize=(20,15))
sns.barplot(x='订单日期', y='总价', palette="Blues_d",data=data3,ax=ax1)
ax1.set_title('每月有效销售额统计',fontsize=15)
ax1.set_xlabel('月份')
ax1.set_ylabel('销售额')

data=pd.read_csv('zhenxing.csv')
data=data.drop('Unnamed: 0', axis=1)
data1=data[[x[2],x[14]]]
data2=data1[x[14]].groupby(data1[x[2]]).sum()
data3=pd.DataFrame(data2)
data3=data3.reset_index()

f,ax1=plt.subplots(1,1,figsize=(20,15))
sns.barplot(x='省区', y='总价', palette="Blues_d",data=data3,ax=ax1)
plt.xticks(rotation=45)
ax1.set_title('省区有效销售额统计',fontsize=15)
ax1.set_xlabel('省区')
ax1.set_ylabel('销售额')


data=pd.read_csv('zhenxing.csv')
data=data.drop('Unnamed: 0', axis=1)
data1=data[[x[2],x[14]]]
data2=data1[x[14]].groupby(data1[x[2]]).sum()
data3=pd.DataFrame(data2)
data3=data3.reset_index()
data4=data3.sort_index(axis = 0,ascending = False,by = x[14])
data4.reset_index(drop=True, inplace=True)

mpl.rcParams['font.size']=3
f,ax1=plt.subplots(1,1,figsize=(20,15))
g=sns.barplot(x='类型', y='数量', palette="Blues_d",data=data6,ax=ax1)
plt.xticks(rotation=30)
ax1.set_title('各类型产品数量统计',fontsize=15)
ax1.set_xlabel('类型')
ax1.set_ylabel('数量')


for index,row in data6.iterrows():
    g.text(row.name,row.tip,round(row.total_bill,2),color="black",ha="center")

fig = plt.figure()
plt.pie(data5[x[12]],labels=data5[x[10]],autopct='%1.2f%%')

data5=data4.copy()
data5['销售占比']=''
sum=data5[x[14]].sum()
for i in range(len(data5)):
    data5['销售占比'][i]=data5[x[14]][i]/sum
f1 = lambda x :'%.4f%%' %(x*100)
data5[['销售占比']]= data5[['销售占比']].applymap(f1)

mpl.rcParams['font.size']=3
f,ax1=plt.subplots(1,1,figsize=(70,50))
sns.barplot(x='经销商编号', y='总价', palette="Blues_d",data=data4,ax=ax1)
plt.xticks(rotation=30)
ax1.set_title('各经销商的销售额统计',fontsize=15)
ax1.set_xlabel('经销商编号')
ax1.set_ylabel('销售额')

 for index,row in grouped_values.iterrows():
     

fig = plt.figure(figsize=(70,50))
plt.pie(data4[x[14]],labels=data4[x[2]],autopct='%1.2f%%')


fig = plt.figure()
g=plt.pie(data4[x[14]],autopct='%1.2f%%')








#删除所有非销售订单的行
for i in range(len(data)):
    if data[x[3]][i]!='销售订单':
        data.drop([i],inplace=True)
        i+=1
    else:
        continue
    
    

idx = np.arange(len(data4))
color = cm.jet(np.array(x)/max(x))
plt.barh(data4[x[10]], data4[x[12]])
plt.yticks(idx,data4[x[10]])


sum=0
for i in range(10,len(data4)):
    sum+=data4[x[14]][i]
data4[x[14]][9]=data4[x[14]][9]+sum

for i in range(10,len(data4)):
        data4.drop([i],inplace=True)
    































































































