# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 11:08:01 2020

@author: jesusa7x
"""
###############################--Busqueda por Pais
def busquedaPais(pais):  
    linea = 0
    total = 0
    
    for line in fh:
        line.rstrip()
        words = line.split(',')
        if len(words) > 2:
            total += 1
            if(pais in words[3]):
                linea += 1
                print(words[4], words[2])

    print(linea,' out of ', total)
    
#####################################################--Busqueda por continente
def busquedaContinente(contienente):
    linea = 0
    total = 0
    
    for line in fh:
        line.rstrip()
        words = line.split(',')
        if len(words) > 2:
            total += 1
            if(contienente in words[11]):
                linea += 1
                print(words[4], words[11])
                
    print(linea,' out of ', total)
    
#################################################################################------Main
fname = "Aeropuertos2.txt"
try:
        fh = open(fname)
except:
        print('File not found')
        quit()

print('Elija una opcion de busqueda:')
print('1.-Busqueda por Pais')
print('2.-Busqueda por Continente')
opcion = int(input('Opcion: '))

if opcion == 1:
    pais = input('Escriba el Pais: ')
    busquedaPais(pais)
if opcion == 2:
    cont = input("Escriba el continente:")
    busquedaContinente(cont)