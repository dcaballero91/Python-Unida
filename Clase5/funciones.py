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