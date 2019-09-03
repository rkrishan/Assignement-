#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 21:40:47 2019

@author: Ram
"""

import pandas as pd
import numpy as np
#import datetime
#from datetime import datetime as dt

data = pd.read_csv('./data.csv')

data.shape
data.info()
data.dtypes

obj_col_list = list(data.select_dtypes(include=['object']).columns)

#now we will convert all the object variables into category type this will help in reducing
#memory usage
for col in obj_col_list:
    data[col]= data[col].astype('category')

data.info(null_counts=True)

#data.describe()

data['current_period_started_at'] = pd.to_datetime(data['current_period_started_at'], errors="ignore")
data['current_period_ends_at'] = pd.to_datetime(data['current_period_ends_at'], errors="ignore")
data['current_period_started_at'] = data['current_period_started_at'].dt.normalize()
data['current_period_ends_at'] = data['current_period_ends_at'].dt.normalize()
#data['current_period_started_at'] = data['current_period_started_at'].dt.year
#df['Month-str'] = df['Date'].dt.strftime('%b')
data['current_period_started_at'] = data['current_period_started_at'].apply(lambda x: x.strftime('%Y-%m'))
data['current_period_ends_at'] = data['current_period_ends_at'].dt.strftime('%Y-%m')
#df['month'] = df['ArrivalDate'].dt.month
## First part
df = data.groupby(['current_period_started_at','account_state'])['business_id'].count().reset_index()
#df = data.groupby(['current_period_started_at','account_state'])['business_id'].agg(['count']).reset_index()
df.to_excel('data_mom_active_closed.xlsx')

## Second part
#df = data.groupby(['current_period_started_at','account_state'])['count','avg_monthly_rating'].apply(list)
df=data.groupby(['current_period_started_at','account_state'])['count','avg_monthly_rating'].agg(lambda x: list(x))
df.to_excel('data_mom_count_avgmonthlyrating_distribution_active_closed.xlsx')
