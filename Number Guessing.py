# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 14:54:41 2021

@author: Pablo Bracciale
"""

import random
from pistas import comprobarPar, comprobarAltura, comprobarDecena, comprobarLongitud


opciones = range(1, 100)
numeroAleatorio=(random.choice(opciones))
numeroIngresado=int(input("Ingrese un numero del 0 al 100: "))
puntuacion=5

while numeroIngresado!=numeroAleatorio and puntuacion>0:
    puntuacion=puntuacion-1
    print ("Tu puntuacion se redujo a: {}".format(puntuacion)) 
    if puntuacion==4:
        comprobarPar(numeroAleatorio)
    if puntuacion==3:
        comprobarAltura(numeroAleatorio)
    if puntuacion==2:
        comprobarDecena(numeroAleatorio)
    if puntuacion==1:
        comprobarLongitud(numeroAleatorio)
    if puntuacion==0:
        print ("Perdiste")
        break
    numeroIngresado=int(input("Ingrese un numero del 0 al 100: "))
else:    
    print("Ganaste")

