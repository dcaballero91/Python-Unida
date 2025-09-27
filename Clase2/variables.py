'''
# Tipos de datos y variables en Python
# Autor: Derlis A. Gonzalez
# Fecha: 2024-06-10   
# Descripción: Este script muestra ejemplos de tipos de datos y variables en Python.

Invoar de esta forma:
http://localhost:8000/Clase2/variables

Dato de entrada:
{
    input: "Ninguno"
}

Dato de salida:
{
    output: "Tipos de datos y variables impresos en consola"
}
'''

entero=10  # Variable de tipo entero
flotante=10.5 # Variable de tipo flotante
cadena="Hola"  # Variable de tipo cadena
booleano=True


print("Entero",entero)
print(type(entero))

print("Flotante",flotante) 
print(type(flotante))

print("Booleano",booleano)  
print(type(booleano))  

print("Cadena",cadena)
print(type(cadena))

numero1=10
numero2=20  
suma=numero1+numero2
print("Suma:",suma)


dato1="Hola"
print(dato1)
print(type(dato1))
dato1=100
print(dato1)        
print(type(dato1))
if dato1>50:
    print("Dato1 es mayor a 50")    