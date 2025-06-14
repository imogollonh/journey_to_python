#1. Verificar si una palabra es palíndromo
#Una palabra que se lee igual al derecho y al revés.
#📥 Entrada: "radar"
#📤 Salida esperada: "La palabra es palíndromo"

def validar_palindromo():
    palabra = input('Ingrese la palabra a evaluar: ')
    palindromo = ""

    for p in range(len(palabra) - 1, -1 , -1):
        palindromo += palabra[p]
    
    if(palabra == palindromo):
        print(f"Es palindromo")
    else:
        print(f"No es palindromo")
        
#validar_palindromo()     

#2. Eliminar duplicados de una lista
#Pide una lista y elimina los elementos repetidos.
#📥 Entrada: "1,2,3,2,1,4"
#📤 Salida esperada: [1, 2, 3, 4]

def eliminar_duplicados():
    lista_numeros = input("Ingresa el listado de numeros separados por coma: ")
    numeros = [int(numero) for numero in lista_numeros.split(",")]
    
    sin_duplicar = list(set(numeros))
    
    print(f"Lista original: {numeros}")
    print(f"Lista sin duplicados: {sin_duplicar}")

#eliminar_duplicados()

#✅ 3. Convertir lista de temperaturas Celsius a Fahrenheit
#Recibe varias temperaturas, devuelve la lista convertida.
#📥 Entrada: "20,25,30"
#📤 Salida esperada: [68.0, 77.0, 86.0]

def convertir_fahrenheit(celsius):
    return (celsius * (9/5) ) + 32
    
def obtener_temperaturas():
    temperaturas = input("Ingresa el listado de temperaturas separados por coma: ")
    lista_temperaturas_celsius = [float(temp) for temp in temperaturas.split(",")]
    
    lista_fahrenheit = []
    
    for t in lista_temperaturas_celsius:
        lista_fahrenheit.append(convertir_fahrenheit(t))
        
    print(f"Lista de temperaturas celsius: {lista_temperaturas_celsius}")
    print(f"Lista de temperaturas fahrenheit: {lista_fahrenheit}")
    
#obtener_temperaturas()
        

#✅ 4. Registrar usuarios en un diccionario
#Pide nombre, edad, correo y guárdalos como diccionario. Permite agregar varios.
#📥 Entrada:
#Nombre: Ana  
#Edad: 25  
#Correo: ana@mail.com
#📤 Salida esperada:
#{'nombre': 'Ana', 'edad': 25, 'correo': 'ana@mail.com'}

def ingreso_usuarios():
    lista_usuarios = []
    flag_finalizar_ingreso = 's'
    
    while flag_finalizar_ingreso.lower() != 'n':
        usuario = dict()
        usuario["nombre"] = input("Ingresa el nombre del usuario: ")
        usuario["edad"] = input("Ingresa la edad del usuario: ")
        usuario["correo"] = input("Ingresa el correo del usuario: ")
        
        lista_usuarios.append(usuario)
        
        flag_finalizar_ingreso = input('Desea ingresar otro usuario? S/N: ')
    
    print(f"Su lista de usuarios ingresados: {lista_usuarios}")
    
#ingreso_usuarios()
        
        


#✅ 5. Calcular la frecuencia de palabras en una oración
#Pide una oración y cuenta cuántas veces aparece cada palabra.
#📥 Entrada: "hola hola mundo mundo mundo"
#📤 Salida esperada:
#{'hola': 2, 'mundo': 3}

from collections import Counter

def frecuencia_palabras():
    oracion = input('Ingrese una oracion para determinar la frecuencia de palabras: ')
    oracion_en_lista = oracion.split()
    
    conteo = Counter(oracion_en_lista)
    
    print(conteo)
    
frecuencia_palabras()
    

