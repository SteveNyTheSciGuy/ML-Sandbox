# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 16:28:07 2020

@author: Steven
"""

import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.dates as mdates
import numpy as np
import os
import pandas as pd
style.use('ggplot')
plt.xkcd()


### DATA USED FOR PLOTTING ###

### NYC Population data based on sex and race ###
# https://www.health.ny.gov/statistics/vital_statistics/2010/table01.htm
#NYCPop=pd.read_csv('NYC_Population_Age_Sex_Cond.csv')
NYCPop=pd.read_csv('NYC_Population_Age_Sex.csv')
ages=NYCPop['Age']
num_ppl=NYCPop['Total']
num_male=NYCPop['Male']
num_female=NYCPop['Female']

### STOCK PRICES ###
stk_tsla= pd.read_csv('tsla.txt',parse_dates=True,index_col=0)
#stinfo['100ma']=stinfo['Adj Close'].rolling(window=100,min_periods=0).mean()
#stinfo.dropna(inplace=True)
stk_appl= pd.read_csv('AAPL.csv',parse_dates=True,index_col=0)
stk_mmm= pd.read_csv('MMM.csv',parse_dates=True,index_col=0)


def scatter_template():
    style.use('ggplot')
    
    x=stk_appl['Adj Close']
    y=stk_mmm['Adj Close']
    dates=stk_appl.index
    
    plt.scatter(y,x,s=2,c=dates,edgecolor='#000000',
                linewidth=.1,alpha=1)
    
    print(np.max(dates))
    
    cbar=plt.colorbar(ticks=[],orientation='horizontal')
    cbar.set_label('Jan  2000      -     Date     -      Dec  2016')
    plt.tight_layout()
    
    plt.xlabel('Apple Stock Value / $')
    plt.ylabel('3M Stock Value / $')
    plt.title('Stock Corrolations')
    plt.legend()
    plt.show()

def bar_template():
    style.use('fivethirtyeight')

    x=ages
    y=num_male
    y1=num_female
    plt.bar(x+1,y,label='Males',color='#6ca0dc',width=2)
    plt.bar(x-1,y1,label='Females',color='#f8b9d4',width=2)
    
    plt.xticks(np.arange(0,85,10))
    plt.tight_layout()
    plt.xlabel('Ages')
    plt.ylabel('Number of People')
    plt.title('NYC Demographics')
    plt.legend()
    plt.show()

def pie_template():
    plt.xkcd()

    slices=num_ppl
    labels=['Age\n0-19','Age\n20-39','Age\n40-59','Age\n60-79','Age\n80+']
    colors=['#348abd','#e24a33','#988ed5','#fbc15e','#777777']
    explode=[0,0.07,0,0,0]            
    
    plt.pie(slices,labels=labels,
            wedgeprops={'edgecolor':'#111111'},colors=colors,explode=explode,
                        shadow=True,startangle=90,autopct='%1.f%%')

    plt.tight_layout()
    plt.title('Age Distributions')
    plt.show()

def line_template_stock():
    style.use('ggplot')
    
    x=stk_tsla.index
    y=stk_tsla['Adj Close']

    x1=stk_appl.index
    y1=stk_appl['Adj Close']

    x2=stk_appl.index
    y2=stk_mmm['Adj Close']
   
    plt.plot(x,y,color='#222222',linestyle='-',linewidth=1,
             label='Tesla Stock')
    plt.plot(x1,y1,color='#888888',linestyle='-',
             linewidth=1,label='Apple Stock')    
    plt.plot(x2,y2,color='#cb410b',linestyle='-',
             linewidth=1,label='3M')    
    
    plt.tight_layout()
    plt.title('Stock Prices')
    plt.xlabel('Date')
    plt.ylabel('Stock $')
    plt.legend()
    plt.show()

def line_template_pop():
    plt.xkcd()

    plt.plot(ages,num_ppl,color='#222222',linestyle='--',linewidth=2,label='Tot Pop')
    plt.plot(ages,num_male,color='#6ca0dc',linestyle='-',linewidth=3,label='Male')
    plt.plot(ages,num_female,color='#f8b9d4',linestyle='-',linewidth=3,label='Female')

    med_tot=sum(num_ppl*(ages+2.5))/sum(num_ppl)
    med_male=sum(num_male*(ages+2.5))/sum(num_male)
    med_female=sum(num_female*(ages+2.5))/sum(num_female)
            
    plt.vlines(med_tot,80000,800000,color='#222222',linestyle='-',linewidth=1.5)
    plt.vlines(med_male,80000,800000,color='#6ca0dc',linestyle='-',linewidth=1.5)
    plt.vlines(med_female,80000,800000,color='#f8b9d4',linestyle='-',linewidth=1.5)

    plt.annotate('Median Ages',(40,750000))
    plt.ticklabel_format(axis='y',style='scientific',scilimits=(0,4))

    plt.xlabel('Ages')
    plt.ylabel('Number of People')
    plt.title('NYC Demographics')
    plt.legend()
    plt.show()
    


line_template_stock()    
line_template_pop()    
#pie_template()
bar_template()
scatter_template()    
    
    
    
    
    
    
    
    
    
    
    