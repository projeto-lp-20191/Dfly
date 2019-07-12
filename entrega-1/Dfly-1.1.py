import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import radians, cos, sin, asin, sqrt


# df_sudeste = pd.read_csv('/home/joao/Documentos/lp/sudeste.csv', sep=',', header=0, usecols=["elvt"])
# print(df_sudeste.head(5))

# def test_intertuples(df):
#     for i in df.itertuples():
#         elevation = i.elvt
#         print(elevation)

# test_intertuples(df_sudeste)

df_ocorrencias = pd.read_csv('/home/joao/Documentos/lp/oco.csv', sep='~', header=0,\
         usecols=['codigo_ocorrencia','ocorrencia_classificacao', 'ocorrencia_tipo', 'ocorrencia_uf',\
                 'ocorrencia_latitude', 'ocorrencia_longitude', 'ocorrencia_horario', 'ocorrencia_dia'])

#print(df_ocorrencias.head(5))
#print(df_ocorrencias.shape)

df_ocorrencias_sudeste = df_ocorrencias.loc[df_ocorrencias['ocorrencia_uf'].isin(['ES','MG','RJ','SP'])]

df_fatores_contribuintes = pd.read_csv('/home/joao/Documentos/lp/ftc.csv', sep='~', header=0,\
        usecols=['codigo_ocorrencia', 'fator_nome'])

#print(df_fatores_contribuintes.head(5))
#print(df_fatores_contribuintes.shape)

df_aeronaves_envolvidas = pd.read_csv('/home/joao/Documentos/lp/anv.csv', sep='~', header=0,\
        usecols=['codigo_ocorrencia', 'aeronave_tipo_veiculo', 'aeronave_fabricante',\
                'aeronave_modelo', 'aeronave_motor_tipo', 'aeronave_motor_quantidade',\
                        'aeronave_ano_fabricacao', 'aeronave_tipo_operacao', 'total_fatalidades'])

#print(df_aeronaves_envolvidas.head(5))
#print(df_aeronaves_envolvidas.shape)

df_ocorrencias_fatores_sudeste = pd.merge(df_ocorrencias_sudeste, df_fatores_contribuintes, on='codigo_ocorrencia', how='inner')

df_ocorrencias_cond_met_sudeste = df_ocorrencias_fatores_sudeste.loc[df_ocorrencias_fatores_sudeste['fator_nome'].isin(['CONDIÇÕES METEOROLÓGICAS ADVERSAS'])]

#print(df_ocorrencias_cond_met_sudeste.head(5))
#print(df_ocorrencias_fatores_sudeste.describe())
#print(df_ocorrencias_cond_met_sudeste.shape)

df_ocorrencias_cond_met_aeronaves_sudeste = pd.merge(df_ocorrencias_cond_met_sudeste, df_aeronaves_envolvidas, on='codigo_ocorrencia', how='inner')

#print(df_ocorrencias_cond_met_aeronaves_sudeste.head(5))
#print(df_ocorrencias_fatores_sudeste.describe())
#print(df_ocorrencias_cond_met_aeronaves_sudeste.shape)

df_ocorrencias_cond_met_aeronaves_sudeste['estacao'] = None

df_ocorrencias_cond_met_aeronaves_sudeste.to_csv ('/home/joao/Documentos/lp/ocorrencias_cond_met_aeronaves_sudeste.csv', index = None, header=True)


#==============================================================================================

df_met_sudeste = pd.read_csv('/home/joao/Documentos/lp/sudeste.csv', sep=',', header=0,\
         usecols=['wsid','wsnm', 'elvt', 'lat', 'lon', 'city', 'prov', 'mdct', 'date',
         'yr', 'mo', 'da', 'hr', 'stp', 'gbrd', 'temp', 'hmdy', 'wdsp', 'wdct', 'gust'])

#print(df_met_sudeste.head(5))
#print(df_ocorrencias_fatores_sudeste.describe())
#print(df_met_sudeste.shape)

#===============================================================================================

# def relacionar_localizacao(df1, df1_col1, df1_col2, df2, df2_col1, df2_col_2):
#     df1_localizacao = []
#     for i in df1.itertuples():
#         latitude = i.df1_col1
#         longitude = i.df1_col2
#         df1_localizacao[0] = latitude
#         df1_localizacao[1] = longitude
#         print(df1_localizacao)


def criar_dicionario_localizacao_ocorrencias(df1):
        df1_localizacao_geral = {}
        for i in df1.itertuples():
                df1_localizacao = []
                latitude = i.ocorrencia_latitude
                longitude = i.ocorrencia_longitude
                hora = i.ocorrencia_horario
                data = i.ocorrencia_dia
                df1_localizacao.append(latitude)
                df1_localizacao.append(longitude)
                df1_localizacao.append(hora)
                df1_localizacao.append(data)
                df1_localizacao_geral[i.codigo_ocorrencia] = df1_localizacao
                #print(df1_localizacao)

        #print(df1_localizacao_geral)

        return df1_localizacao_geral

dic_ocorrencias = criar_dicionario_localizacao_ocorrencias(df_ocorrencias_cond_met_aeronaves_sudeste)


def criar_dicionario_localizacao_estacoes(df1):
        df1_localizacao_geral = {}
        for i in df1.itertuples():
                df1_localizacao = []
                latitude = i.lat
                longitude = i.lon
                data_hora = i.mdct
                df1_localizacao.append(latitude)
                df1_localizacao.append(longitude)
                df1_localizacao.append(data_hora)
                df1_localizacao_geral[i.wsid] = df1_localizacao
                #print(df1_localizacao)

        #print(df1_localizacao_geral)

        return df1_localizacao_geral

dic_estacoes = criar_dicionario_localizacao_estacoes(df_met_sudeste)

#================================================================================================

# Formula de Haversine
def haversine( a, b ):
        # Raio da Terra em Km
        r = 6371
        relacao_ocorrencia_estacao_12km = {}
        for k1, v1 in a.items():
                for k2, v2 in b.items():        
                        # Converte coordenadas de graus para radianos
                        lat1, lon1, lat2, lon2 = map(radians, [ v1[0], v2[1], v2[0], v2[1] ] )

                        # Formula de Haversine
                        dlon = lon2 - lon1
                        dlat = lat2 - lat1
                        hav = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
                        d = 2 * r * asin( sqrt(hav) )
                        #print(d)
                        if (d <= 12):
                                relacao_ocorrencia_estacao_12km[k1] = k2


        return relacao_ocorrencia_estacao_12km

dic_haversine = haversine(dic_ocorrencias, dic_estacoes)

#print((haversine(dic_ocorrencias, dic_estacoes)).keys())

#print(len((haversine(dic_ocorrencias, dic_estacoes)).keys()))

#===============================================================================================

def preencher_estacao(dic_haversine, df):
        print(df.head(5))
        idx = 0
        for k,v in dic_haversine.items():
                if (df['codigo_ocorrencia'] == k).item():
                        df.insert(idx,'estacao', v)
                        idx += 1
        return df

df_ocorrencias_com_id_estacao = preencher_estacao(dic_haversine, df_ocorrencias_cond_met_aeronaves_sudeste)

print(df_ocorrencias_com_id_estacao.head())