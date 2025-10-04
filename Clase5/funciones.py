'''
Ejemplo de funciones
'''

def sumar(a,b):
    r=a+b
    print(f"Sumando dentro de la funcion: {a} + {b}={r}")
    return r

a=5
b=3
resultado=sumar(a,b)
print("-----Fuera de la funcion----"   )
print(f"El resultado de la suma es: {resultado}")
if resultado>5:
    print("El resultado es mayor a 5")
else:
    print("El resultado es menor o igual a 5")