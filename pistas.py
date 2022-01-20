# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 16:52:02 2021

@author: Pablo Bracciale
"""

def comprobarPar (numero):
    if numero % 2 == 0:
        print ("Pista: El numero es par.")
    else:
        print ("Pista: El numero es impar.")
        
def comprobarAltura (numero):
    if numero>50:
        print ("Pista: El numero es mayor a cincuenta")
    else:
        print ("Pista: El numero es menor a cincuenta")

def comprobarDecena(numero):
    decenas={
            "Primera decena": range (1,11),
            "Segunda decena":range (11,21),
            "Tercera decena":range (21,31),
            "Cuarta decena":range (31,41),
            "Quinta decena": range (41,51),
            "Sexta decena": range (51,61),
            "Septima decena":range (61,71),
            "Octava decena":range (71,81),
            "Novena decena": range (81,91),
            "Decima decena": range (91,100),
            }
    for clave, valor in decenas.items():
        for valores in valor:
            if numero==valores:
                print ("El numero esta en la {}".format(clave))
                
def comprobarLongitud(numero):
    if len(str(numero))==1:
        print ("Tiene un solo digito! Por eso esta en la primera decena :)")
    if len(str(numero))==2:
        if str(numero)[0]<str(numero)[1]:
            print("El segundo digito es mayor al primero")
        elif str(numero)[0]==str(numero)[1]:
            print ("Ambos digitos son iguales")
        else:
            print("El primer digito es mas alto que el segundo")

        