#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from pandas import Series
import datetime as dt
import matplotlib.pyplot as plt


# In[ ]:


df_oco = pd.read_csv('oco.csv', encoding="utf-8", sep='"~"', engine='python')
df_oco


# In[ ]:


df_rec = pd.read_csv('rec.csv', encoding="utf-8", sep='"~"', engine='python')
df_rec


# In[ ]:


df_ftc = pd.read_csv('ftc.csv', encoding="utf-8", sep='"~"', engine='python')
df_ftc


# In[ ]:


df_anv = pd.read_csv('anv.csv', encoding="utf-8", sep='"~"', engine='python')
df_anv


# In[ ]:


df_oco_rec = pd.merge(df_oco, df_rec, how='outer', on='"codigo_ocorrencia')
#df_oco_rec.to_csv("df_oco_rec.csv", sep=',', encoding='utf-8')
df_oco_rec


# In[ ]:


df_oco_rec_ftc = pd.merge(df_oco_rec, df_ftc, how='outer', on='"codigo_ocorrencia')
df_oco_rec_ftc


# In[ ]:


df_oco_rec_ftc_anv = pd.merge(df_oco_rec_ftc, df_anv, how='outer', on='"codigo_ocorrencia')
df_oco_rec_ftc_anv.to_csv("df_oco_rec_ftc_anv.csv", sep=',', encoding='utf-8')
df_oco_rec_ftc_anv


# In[ ]:


df.columns


# In[ ]:


df.dtypes


# In[ ]:


df['ocorrencia_dia'] = pd.to_datetime(df['ocorrencia_dia'])
df['ocorrencia_dia'].dtype


# In[ ]:


s = df['ocorrencia_dia'].str.split('-').apply(Series, 1).stack()


# In[ ]:


print(s)


# In[ ]:


df = df.str.replace(""", "")


# In[ ]:


s = df[df['ocorrencia_dia'] == '2013-05-05']


# In[ ]:


s


# In[ ]:


df


# In[ ]:


df.loc[:,((df['ocorrencia_dia']) < '2009-01-01') & ((df['ocorrencia_dia']) > '2006-01-01')]


# In[ ]:


start = dt.datetime.strptime('2010-01-02', '%Y-%m-%d')
end = dt.datetime.strptime('2011-01-02', '%Y-%m-%d')
sdf = (df.ocorrencia_dia > start) & (df.ocorrencia_dia < end)
df.loc[sdf,'Apagar'] = False
df

