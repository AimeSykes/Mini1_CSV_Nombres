# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 23:43:06 2022

@author: Equipo Rojo Baya (Cruz Anaya Aime Arely, Barrera Reyes Pablo Raziel)
"""
import csv
import random
        
def leerCSV(file):
    Pila=[]
    with open(file) as origencsv:
        origencsv.readline() 
        lectorCSV = csv.reader(origencsv, delimiter=',')
        for fila in lectorCSV:
             nombre, frec, edad_media=fila
             Pila.append(nombre)
    return(Pila)

def escribirCSV(destinocsv,nom,AP,AM):
        escritorDictCSV = csv.DictWriter(destinocsv, fieldnames=["nombre","AP","AM"], delimiter="|")
        print(nom,AP,AM)
        escritorDictCSV.writerow({"nombre":nom, "AP":AP, "AM":AM})
        
def menu():
    op = int(input('Programa que genera nombres completos\n'
                   'Elige una opción: \n'
                   '1.- Mujeres \n'
                   '2.- Hombres \n'
                   '3.- Mixto(hombres y mujeres) \n'))
    return (op)

def generaNombres(): 
    op = int(input('Cantidad de nombres a generar 1 a 1000 \n'))
    return (op)

def NombresHAleatorios():
    return NombresHombres[(random.randint(0, len(NombresHombres)-1))]

def NombresMAleatorios():
    return NombresMujeres[(random.randint(0, len(NombresMujeres)-1))]    

def NombresAleatorios():
    op = random.randint(1,2)
    
    if op == 1: 
        return NombresHombres[(random.randint(0, len(NombresHombres)-1))]
    else:
        return NombresMujeres[(random.randint(0, len(NombresMujeres)-1))]

def ApellidosAleatorios():
    return Apellidos[(random.randint(0, len(Apellidos)-1))]

def salida():
    op = menu()
    destinocsv = open("SalidaNombres.csv", 'w', newline="")
    
    if op == 1:
        for i in range(0, generaNombres(), 1):
            escribirCSV(destinocsv, NombresMAleatorios(), ApellidosAleatorios(), ApellidosAleatorios())
           
    elif op == 2:
        for i in range(0, generaNombres(), 1):
           escribirCSV(destinocsv, NombresHAleatorios(), ApellidosAleatorios(), ApellidosAleatorios())
          
    elif op == 3:
        for i in range(0, generaNombres(), 1):
            escribirCSV(destinocsv, NombresAleatorios(), ApellidosAleatorios(), ApellidosAleatorios())
     
NombresMujeres=leerCSV("mujeres.csv")
NombresHombres=leerCSV("hombres.csv")
Apellidos=leerCSV("apellidos.csv")
salida()