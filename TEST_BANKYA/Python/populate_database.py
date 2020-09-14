#!/usr/bin/env python
# coding: utf-8

# In[33]:


from sqlalchemy import create_engine
import names
import yaml
from random import randint
import datetime
from datetime import date


# In[34]:


with open("db.yml", "r") as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)


# In[35]:


user = cfg['mysql']['user']
pss = cfg['mysql']['passwd']
host = cfg['mysql']['host']
port = cfg['mysql']['port']
db = cfg['mysql']['db']


# In[36]:


en = create_engine(f'mysql+pymysql://{user}:{pss}@{host}:{port}/{db}')


# In[37]:


def fecha():
    año = str(randint(1980, 2002))
    mes = str(randint(1,12))
    if mes == "2":
        dia = str(randint(1,28))
    else:
        dia = str(randint(1,30))
    return año + '-' + mes + '-' + dia


# In[38]:


def calcular_edad(f_nac):
    hoy = date.today()
    try:
        cumple = f_nac.replace(year=hoy.year)
    except ValueError:
        cumple = f_nac.replace(year=hoy.year, day=f_nac.day - 1) 
    if cumple > hoy:
        return hoy.year - f_nac.year - 1
    else:
        return hoy.year - f_nac.year


# In[39]:


def direccion():
    calles = ['av. del Parque', 'Pirámide de la Luna', 'Retorno 48', 'Calzad de la Virgen', "Retorno 1"]
    return calles[randint(0,4)] + ' ' +'#' + str(randint(1,100))


# In[40]:


def municipio():
    muns = ['Coyoacán', 'Alvaro Obregón', 'Azcapotzalco', 'Miguel Hidalgo', 'Tlalpan', 'Benito Juárez']
    return muns[randint(0, 5)]


# In[41]:


def cod_postal():
    cps = ['04460', '14506', '90210', '15023', '04571', '23429', '12345']
    return cps[randint(0, 6)]


# In[42]:


for i in range(100):
    nombre = names.get_first_name()
    apellidos = names.get_last_name() + ' ' + names.get_last_name()
    f_nac = fecha()
    dia, mes, anio = [int(v) for v in f_nac.split("-")]
    edad = calcular_edad(date(dia, mes, anio))
    direc = direccion()
    cp = cod_postal()
    mun = municipio()
    estado = "CDMX"
    tel = '55' + str(randint(10000000, 99999999))
    cad = f'INSERT INTO CLIENTES VALUES ({i+1},"{nombre}","{apellidos}",\'{f_nac}\',{edad},"{direc}","{cp}","{mun}","{estado}","{tel}")'
    conn = en.connect()
    conn.execute(cad)
    conn.close()


# In[44]:


import dateutil.relativedelta


# In[45]:


plazos = [1, 3, 6, 9, 12, 15, 18, 20, 24, 36, 48, 60, 72]
f = [15, 30]
for i in range(150):
    p = randint(0,11)
    f_1 = randint(0,1)
    cliente = randint(1,50)
    monto_inicial = randint(1000, 300000)
    fecha_i = str(date.today())
    fecha_aux = datetime.datetime.strptime(fecha_i, "%Y-%m-%d")
    fecha_f = str(fecha_aux + dateutil.relativedelta.relativedelta(months=plazos[p]))[:10]
    monto_total = monto_inicial
    freq = f[f_1]
    monto_pagos = monto_total/plazos[p]
    cad = f'INSERT INTO PRESTAMOS VALUES ({i+1},{cliente},\'{fecha_i}\', \'{fecha_f}\' ,{monto_total},{freq},{monto_pagos})'
    conn = en.connect()
    conn.execute(cad)
    conn.close()


# In[46]:


import pandas as pd


# In[47]:


df = pd.read_csv('..\\prestamos.csv', sep = ',', encoding = 'utf8')


# In[48]:


df.head()


# In[49]:


df.shape


# In[50]:


df.dtypes


# In[51]:


for i , fila in df.iterrows():
    ci = int(df['CUSTOMERID'].iloc[i])
    f = int(df['FREQ_PAGOS'].iloc[i])
    m = df['MONTO_PAGOS'].iloc[i]
    c = int(df['CONTRACTID'].iloc[i])
    fecha = df['FECHA_INI'].iloc[i]
    fecha_aux = fecha.split('/')
    dia = fecha_aux[0]
    mes = fecha_aux[1]
    anio = fecha_aux[2]
    fecha_aux_1 =  str(anio+ '-' +mes+ '-' +dia)
    fecha_aux = datetime.datetime.strptime(fecha_aux_1, "%Y-%m-%d")
    fecha_f = str(fecha_aux + dateutil.relativedelta.relativedelta(days=f))[:10]
    cad = f'INSERT INTO PAGOS VALUES({i+1},{c},{ci},\'{fecha_f}\',{m}, {m},\'{fecha_f}\')'
    conn = en.connect()
    conn.execute(cad)
    conn.close()


# In[ ]:





# In[ ]:





# In[ ]:




