#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#%matplotlib inline
#%matplotlib notebook

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_aeronaves_envolvidas = pd.read_csv('/home/joao/Documents/lp/anv.csv', sep='~', header=0)
df_ocorrencias = pd.read_csv('/home/joao/Documents/lp/oco.csv', sep='~', header=0)
df_fatores_contribuintes = pd.read_csv('/home/joao/Documents/lp/ftc.csv', sep='~', header=0)

df_ocorrencias_sudeste = df_ocorrencias.loc[df_ocorrencias['ocorrencia_uf'].isin(['ES','MG','RJ','SP'])]

df_ocorrencias_aeronavesenv_sudeste = pd.merge(df_ocorrencias_sudeste, df_aeronaves_envolvidas, on='codigo_ocorrencia', how='inner')

df_ocorrencias_aeronavesenv_fatores_sudeste = pd.merge(df_ocorrencias_aeronavesenv_sudeste, df_fatores_contribuintes, on='codigo_ocorrencia', how='inner')

# df_graf_01 = df_ocorrencias_aeronavesenv_fatores_sudeste = df_ocorrencias_aeronavesenv_fatores_sudeste.loc[(df_ocorrencias_aeronavesenv_fatores_sudeste['ocorrencia_classificacao']\
#     .isin(['ACIDENTE'])) & (df_ocorrencias_aeronavesenv_fatores_sudeste['ocorrencia_tipo'].isin[('FALHA DO MOTOR EM VOO')])] 

df_graf_01 = df_ocorrencias_aeronavesenv_fatores_sudeste.loc[df_ocorrencias_aeronavesenv_fatores_sudeste['ocorrencia_classificacao']\
    .isin(['ACIDENTE'])]

# df_graf_01 = df_graf_01.loc[df_graf_01['ocorrencia_tipo']\
#     .isin(['PERDA DE CONTROLE EM VOO'])]

df_graf_01 = df_graf_01.loc[df_graf_01['fator_nome']\
    .isin(['CONDIÇÕES METEOROLÓGICAS ADVERSAS'])]

df_graf_01.aeronave_modelo.value_counts().head(5).plot(kind='bar', figsize=(10,5), grid=False, rot=0, color='blue')

plt.title('Os 5 modelos de aeronaves com mais acidentes ocasionados por condições meteorológicas na região sudeste do Brasil')
plt.xlabel('Modelos de Aeronaves')
plt.ylabel('Quantidade de Acidentes')
plt.xticks(fontsize=7, rotation=0)
plt.yticks(fontsize=7, rotation=0)
plt.show()
#-------------------------------------------------------------------

# df_graf_01 = df_ocorrencias_aeronavesenv_fatores_sudeste

# df_graf_01 = df_graf_01.loc[df_graf_01['ocorrencia_tipo']\
#     .isin(['PERDA DE CONTROLE EM VOO'])]

# df_graf_01 = df_graf_01.loc[df_graf_01['fator_nome']\
#     .isin(['CONDIÇÕES METEOROLÓGICAS ADVERSAS'])]

# df_graf_01.aeronave_fabricante.value_counts().head(5).plot(kind='bar', figsize=(10,5), grid=False, rot=0, color='red')

# plt.title('As 5 fabricantes de aeronaves com mais ocorrências ocasionadas por condições meteorológicas na região sudeste do Brasil')
# plt.xlabel('Fabricantes de Aeronaves')
# plt.ylabel('Quantidade de Ocorrências')
# plt.xticks(fontsize=7, rotation=0)
# plt.yticks(fontsize=7, rotation=0)
# plt.show()

#-------------------------------------------------------------------



# df_ocorrencias_sudeste = df_ocorrencias.loc[df_ocorrencias['ocorrencia_uf'].isin(['ES','MG','RJ','SP'])]

# df_ocorrencias_aeronavesenv_brasil = pd.merge(df_ocorrencias, df_aeronaves_envolvidas, on='codigo_ocorrencia', how='inner')

# df_ocorrencias_aeronavesenv_sudeste = pd.merge(df_ocorrencias_sudeste, df_aeronaves_envolvidas, on='codigo_ocorrencia', how='inner')

# df_ocorrencia_aeronavesenv_sudeste.aeronave_fabricante.value_counts().head(5).plot(kind='bar', figsize=(10,5), grid=True, rot=0, color='green')

# plt.title('As 5 fabricantes com mais ocorrências na região sudeste do Brasil')
# plt.xlabel('Fabricante')
# plt.ylabel('Quantidade de ocorrências')
# plt.xticks(fontsize=7, rotation=0)
# plt.yticks(fontsize=7, rotation=0)
# plt.show()

# df_ocorrencia_aeronavesenv_brasil.aeronave_fabricante.value_counts().head(5).plot(kind='bar', figsize=(10,5), grid=True, rot=0, color='blue')

# plt.title('As 5 fabricantes com mais ocorrências no Brasil')
# plt.xlabel('Fabricante')
# plt.ylabel('Quantidade de ocorrências')
# plt.xticks(fontsize=7, rotation=0)
# plt.yticks(fontsize=7, rotation=0)
# plt.show()

# df_ocorrencia_aeronavesenv_sudeste_cessna = df_ocorrencia_aeronavesenv_sudeste.loc[df_ocorrencia_aeronavesenv_sudeste['aeronave_fabricante'].isin(['CESSNA AIRCRAFT'])]

# df_ocorrencia_aeronavesenv_sudeste_cessna.ocorrencia_tipo_categoria.value_counts().head(5).plot(kind='bar', figsize=(10,5), grid=True, rot=0, color='red')
# plt.title('Os 5 tipos de ocorrências da fabricante CESSNA AIRCRAFT no sudeste do Brasil')
# plt.xlabel('Tipo de ocorrência')
# plt.ylabel('Quantidade do tipo de ocorrência')
# plt.xticks(fontsize=4, rotation=0)
# plt.yticks(fontsize=7, rotation=0)
# plt.show()

