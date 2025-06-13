from datetime import datetime
## 1. Programa que pida nombre y edad, y diga en qué año cumplirás 100 años.

def pronostico_edad():
    nombre = input('Ingresa tu nombre: ')
    edad = int(input('Ingresa tu edad: '))
    
    anio = (100 - edad) + int(datetime.now().year)
    
    print(f"Hola {nombre} en el anio {anio} cumpliras 100 anios")
    
#pronostico_edad()

## 2. Función que reciba dos números y devuelva el mayor.

def numero_mayor():
    n1 = int(input('Ingresa el primer numero: '))
    n2 = int(input('Ingresa el segundo numero: '))
    
    if n1 > n2:
        print(f"{n1} es mayor a {n2}")
    if n2 > n1:
        print(f"{n2} es mayor a {n1}")
    else:
        print(f"Ambos numeros son iguales")
    

#numero_mayor()

## 3. Tabla de multiplicar del número que el usuario ingrese.

def tabla_multiplicar():
    numero = int(input('Ingresa el numero para la tabla: '))
    
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

#tabla_multiplicar()

## 4. Contar cuántas vocales tiene una cadena.

def contador_vocales():
    vocales = 'aeiou'
    cadena = input('Ingrese una cadena: ')
    contador = 0

    for letra in cadena.lower():
        if letra in vocales:
            contador += 1

    print(f"La cadena: {cadena}, tiene {contador} vocales")

                
 
#contador_vocales()   

## 5. Convertir grados Celsius a Fahrenheit.

def convertir_fahrenheit():
    celsius  = float(input('Ingrese los grados celsius: '))
    fahrenheit = (celsius * (9/5) ) + 32
    
    print(f"Grados celsius {celsius}, grados fahrenheit {fahrenheit}")

#convertir_fahrenheit()