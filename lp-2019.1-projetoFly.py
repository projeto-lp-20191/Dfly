#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')

ocorrencias = pd.read_csv('/home/brunolins/myprojectdir/Dados/oco.csv', sep='~')
ocorrencias_sudeste = ocorrencias.loc[ocorrencias['ocorrencia_uf'].isin(['ES','MG','RJ','SP'])]
recomendacoes = pd.read_csv('/home/brunolins/myprojectdir/Dados/rec.csv', sep='~')
fatores = pd.read_csv('/home/brunolins/myprojectdir/Dados/ftc.csv', sep='~')
aeronaves_envolvidas = pd.read_csv('/home/brunolins/myprojectdir/Dados/anv.csv', sep='~')

tabelao1 = pd.merge(ocorrencias_sudeste, aeronaves_envolvidas, on = 'codigo_ocorrencia', how='inner')
columns = ['ocorrencia_tipo_icao', 'ocorrencia_pais', 'investigacao_aeronave_liberada', 'divulgacao_relatorio_numero', 'divulgacao_relatorio_publicado', 'divulgacao_dia_publicacao', 'ocorrencia_dia_extracao', 'aeronave_pmd', 'aeronave_assentos', 'aeronave_registro_categoria', 'aeronave_fase_operacao_icao', 'aeronave_dia_extracao']
tabelao1.drop(columns, inplace=True, axis=1)

# clima = pd.read_csv('/home/brunolins/myprojectdir/sudeste.csv', sep=',')


# In[2]:


# tabelao1.to_csv('tabelao_inner.csv')
tabelao1


# In[3]:


# clima


# In[ ]:


get_ipython().run_line_magic('matplotlib', 'notebook')
tabelao1['ocorrencia_classificacao'].hist(bins=5)

