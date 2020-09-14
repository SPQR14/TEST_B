#!/usr/bin/env python
# coding: utf-8

from sqlalchemy import create_engine
import names
import yaml
from random import randint
from datetime import date

with open("db.yml", "r") as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

user = cfg['mysql']['user']
pss = cfg['mysql']['passwd']
host = cfg['mysql']['host']
port = cfg['mysql']['port']
db = cfg['mysql']['db']

en = create_engine(f'mysql+pymysql://{user}:{pss}@{host}:{port}/{db}')

"""
    COSTUMERID INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY, 
    NOMBRE VARCHAR(35) NOT NULL,
    APELLIDOS VARCHAR(35) NOT NULL,
    F_NACIMIENTO DATE NOT NULL,
    EDAD SMALLINT,
    CALLE_Y_NUMERO VARCHAR(60) NOT NULL,
    CP VARCHAR(5) NOT NULL,
    MUNICIPIO VARCHAR(50) NOT NULL,
    ESTADO VARCHAR(4) NOT NULL,
    TELEFONO VARCHAR(10)
"""
def fecha():
    año = str(randint(1985, 2002))
    
    mes = str(randint(1,12))
    if mes == "2":
        dia = str(randint(1,28))
    else:
        dia = str(randint(1,30))
    return año + '-' + mes + '-' + dia

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

def direccion():
    calles = ['av. del Parque', 'Pirámide de la Luna', 'Retorno 48', 'Calzad de la Virgen', "Retorno 1"]
    return calles[randint(0,4)] + ' ' +'#' + str(randint(1,100))

def municipio():
    muns = ['Coyoacán', 'Alvaro Obregón', 'Azcapotzalco', 'Miguel Hidalgo', 'Tlalpan', 'Benito Juárez']
    return muns[randint(0, 5)]

for i in range(50):
    nombre = names.get_first_name()
    apellidos = names.get_last_name() + ' ' + names.get_last_name()
    f_nac = fecha()
    dia, mes, anio = [int(v) for v in f_nac.split("-")]
    edad = calcular_edad(date(dia, mes, anio))
    direc = direccion()
    cp = str(randint(10000, 99999))
    mun = municipio()
    estado = "CDMX"
    tel = '55' + str(randint(10000000, 99999999))
    cad = f'INSERT INTO CLIENTES VALUES ({i+1},"{nombre}","{apellidos}",\'{f_nac}\',{edad},"{direc}","{cp}","{mun}","{estado}","{tel}")'
    conn = en.connect()
    conn.execute(cad)
    conn.close()

en.dispose()

