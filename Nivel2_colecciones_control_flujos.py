#1. Verificar si un número es divisible entre 2 y 3
#Descripción: Pide un número al usuario y di si es divisible entre 2, entre 3, entre ambos o ninguno.

def numero_divisible():
    numero = int(input('Ingrese un numero: '))
    if numero % 2 == 0 and numero % 3 == 0:
        print(f"El numero es divisible entre 2 y 3")
    elif numero % 2 == 0:
        print(f"El numero es divisible entre 2")
    elif numero % 3 == 0:
        print(f"El numero es divisible entre 3")
    else:
        print(f"El numero no es divisible entre 2 y 3")

#numero_divisible()
        
#2. Buscar un nombre en una lista
#Descripción: Pide un nombre y verifica si existe en una lista predefinida de nombres.

def validar_nombre():
    lista_nombres = ['Juan', 'Alberto', 'Carlos', 'Ivan', 'Andrea']
    
    nombre = input('Ingresa el nombre a buscar: ')
    
    for nombres_en_lista in lista_nombres:
        if nombre.lower() == nombres_en_lista.lower():
            print(f"El nombre {nombre} esta en la lista")
            return
    print(f"El nombre {nombre} no esta en la lista")

#validar_nombre()

#3. Calcular el promedio de una lista de notas
#Descripción: Dada una lista de números, calcula el promedio. Usa sum() y len().

def calcular_promedio():
    entrada = input("Ingresa las notas separadas por coma: ")
    notas = [float(nota) for nota in entrada.split(",")]
    promedio = sum(notas) / len(notas)
    print(f"Promedio: {promedio}")

#calcular_promedio()


#4. Contar cuántos números pares e impares hay en una lista
#Descripción: Dada una lista de números, indica cuántos son pares y cuántos impares.

def contador_numeros():
    entrada = input("Ingresa el listado de numeros separados por coma: ")
    numeros = [int(numero) for numero in entrada.split(",")]
    contador_pares = 0
    contador_impares = 0
    
    for numero in numeros:
        if numero % 2 == 0:
            contador_pares += 1
        else:
            contador_impares += 1
    
    print(f"Hay: {contador_pares} y {contador_impares} impares" )
    
#contador_numeros()

#5. Simular inicio de sesión con intentos limitados
#Descripción: Pide usuario y contraseña, y permite 3 intentos. Si son correctos, da acceso.

def login():
    intentos = 1
    
    while intentos < 4:
        user = input('Ingresa tu usuario: ')
        password = input('Ingresa tu contrasena: ')
        #Se simula que es case sensitive
        if user == 'admin' and password == '123':
            print(f"Bienvenido {user}")
            return
        else:
            print(f"Credenciales incorrectas. Intentos {intentos}")
            intentos += 1
    print("Cuenta bloqueada")
    
login()

