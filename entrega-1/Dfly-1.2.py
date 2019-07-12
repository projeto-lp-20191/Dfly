#!/usr/bin/env python
# coding: utf-8

# In[1]:


#%matplotlib inline
get_ipython().run_line_magic('matplotlib', 'notebook')


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import bokeh 
import seaborn as sns
import plotly.offline as py
import plotly.graph_objs as go
py.init_notebook_mode(connected=True)
from bokeh.io import output_notebook, show
output_notebook()
from matplotlib import interactive
interactive(True)

from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file
from bokeh.sampledata.stocks import AAPL, GOOG, IBM, MSFT

#get_ipython().run_line_magic('matplotlib', 'inline')

#%matplotlib inline

sns.set()


# In[2]:


df_anv = pd.read_csv('/home/joao/Documents/lp/anv.csv', sep='~', header=0)
df_oco = pd.read_csv('/home/joao/Documents/lp/oco.csv', sep='~', header=0)


# In[3]:


df_anv


# In[4]:


df_oco


# In[5]:


df_oco_sudeste = df_oco.loc[df_oco['ocorrencia_uf'].isin(['ES','MG','RJ','SP'])]


# In[6]:


df_oco_sudeste


# In[7]:


df_ocorrencia_aeronavesenv = pd.merge(df_oco_sudeste, df_anv, on='codigo_ocorrencia', how='inner')


# In[8]:


df_ocorrencia_aeronavesenv


# In[9]:


df_ocorrencia_aeronavesenv.plot.scatter(df_ocorrencia_aeronavesenv.ocorrencia_classificacao, df_ocorrencia_aeronavesenv.aeronave_fabricante, s=300)


# In[ ]:


df = pd.DataFrame([[5.1, 3.5, 0], [4.9, 3.0, 0], [7.0, 3.2, 1],
                      [6.4, 3.2, 1], [5.9, 3.0, 2]],
                      columns=['length', 'width', 'species'])


# In[ ]:


x=df_anv['aeronave_assentos']
y=(df_anv['aeronave_ano_fabricacao']> 2000)
plt.scatter(x, y)
plt.show()


# In[10]:


df_ocorrencia_aeronavesenv.head()


# In[11]:


df_ocorrencia_aeronavesenv.describe()


# In[12]:


df_ocorrencia_aeronavesenv.dtypes


# In[13]:


df_ocorrencia_aeronavesenv.ocorrencia_classificacao.value_counts().plot.scatter(figsize=(9, 3), align='center')


# In[14]:


df_ocorrencia_aeronavesenv.shape


# In[15]:


df_ocorrencia_aeronavesenv.aeronave_fabricante.value_counts()


# In[16]:


df_ocorrencia_aeronavesenv.aeronave_fabricante.value_counts().head(5).plot(kind='bar', figsize=(10,5), grid=True, rot=0, color='green')

plt.title('As 5 fabricantes com mais ocorrências na região sudeste do Brasil')
plt.xlabel('Fabricante')
plt.ylabel('Quantidade de ocorrências')
plt.xticks(fontsize=7, rotation=0)
plt.yticks(fontsize=7, rotation=0)

plt.show()

sns.set


# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
ax1 = df.plot.scatter(x='length',
                          y='width',
                          c='DarkBlue')


# In[ ]:


ax2 = df.plot.scatter(x='length',
                        y='width',
                        c='species',
                        colormap='viridis')


# In[ ]:


get_ipython().system('pip install bokeh')


# In[ ]:


import bokeh.sampledata
bokeh.sampledata.download()


# In[ ]:


import matplotlib.pyplot as plt
from bokeh.sampledata.iris import flowers as dados
plt.hist(dados['sepal_length'], bins=12)
plt.show()


# In[ ]:


from bokeh.io import output_notebook, show
output_notebook()


# In[ ]:


plt.hist(df_anv['aeronave_assentos'], bins=12)
plt.show()


# In[ ]:


hist = df_anv.plot.hist(data=df_anv["aeronave_assentos"], values="aeronave_assentos", color="aeronave_ano_fabricacao", legend="top_right", bins=12)
show(hist)


# In[ ]:


df_anv_hist = plt.hist(df_anv)
df_anv_hist = plt.hist(df_anv)


# 

# In[ ]:


x=df_anv['aeronave_assentos']
y=df_anv['aeronave_ano_fabricacao']
plt.hist(x, y)
plt.show()


# In[ ]:


get_ipython().system('pip install seaborn')


# In[ ]:


df.plot.scatter(x='length', y='width', c='DarkBlue')
plt.xlabel("Comprimento")
plt.ylabel("Largura")
plt.title("Teste")
plt.show()


# In[ ]:


get_ipython().system('pip install --upgrade matplotlib')


# In[ ]:


get_ipython().system('pip install plotly')


# In[ ]:


df.plot.scatter(x='length', y='width', c='DarkBlue')
plt.xlabel("Comprimento")
plt.ylabel("Largura")
plt.title("Teste")
plt.show()


# In[ ]:


trace = go.Scatter(x = df['length'], y = df["width"], mode = "markers")
data = [trace]
py.iplot(data)


# In[ ]:




