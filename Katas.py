
# 1) Escribe una función que reciba una cadena de texto como parámetro y 
# devuelva un diccionario con las frecuencias de cada letra en la cadena. 
# Los espacios no deben ser considerados.

def frecuencias_letras(cadena):
    '''
    Esta función recibe una cadena de texto y devuelve un diccionario con 
    la frecuencia de cada letra en la cadena.    
    
    Parámetros:
        -cadena (str): La cadena de texto en la que se contarán las letras.

    Return:
        -dict: Un diccionario con las letras como claves y los valores 
               son sus frecuencias en la cadena.
    '''
    
    cadena = cadena.replace(" ", "") # Eliminamos los espacios
    frecuencias = {}  # Creamos un diccionario vacío para almacenar las frecuencias
    for letra in cadena: # Iteramos sobre cada letra en la cadena
        # Si la letra ya está en el diccionario, incrementamos su contador. Si no, la añadimos con un contador de 1.
        if letra in frecuencias:  
            frecuencias[letra] += 1
        else:
            frecuencias[letra] = 1
    return frecuencias

# Ejemplo de uso de la función
texto = "Hola mundo"
resultado = frecuencias_letras(texto)
print(resultado)

# 2) Dada una lista de números, obtén una nueva lista con el doble de cada valor. 
# Usa la función map()
def doblar_valor(numeros):
    '''
    Esta función recibe una lista de números y devuelve una nueva lista 
    con el doble de cada valor.
    
    Parámetros:
        -numeros (list): Lista de números a procesar.
    
    Return:
        -list: Nueva lista con el doble de cada número.
    '''
# Aplicamos un función lambda a cada elemento de la lista. Como el resultado de la función 
# map() es un objeto, lo convertimos a una lista para que nos muestre un resultado legible.  
    return list(map(lambda x: x * 2, numeros)) 
# Ejemplo de uso de la función
numeros = [1, 2, 3, 4, 5]
resultado = doblar_valor(numeros)
print(resultado)


# 3) Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe 
# devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

def filtro_palabras(palabra, palabra_objetivo):                      
    '''
    Función recibe una lista de palabras y una palabra objetivo, 
    y devuelve una lista con todas las palabras que contienen la palabra objetivo.
    
    Parámetros:
        -palabra (list): Lista de palabras a filtrar.
        -palabra_objetivo (str): Palabra que se busca en la lista.
    
    Return:
        -list: Lista de palabras que contienen la palabra objetivo.
    '''
    #creo una variable con una List Comprehension para crear una lista nueva a partir de la lista inicial
    lista_palabras_obejetivo = [palabra for palabra in palabra if palabra_objetivo in palabra]
    return print (lista_palabras_obejetivo)

#caso de uso:
lista_ejemplo = ['mamut', 'elefante', 'cocodrilo', 'mamut', 'serpiente', 'león', 'mamut']
filtro_palabras(lista_ejemplo, 'mamut')  # Salida: ['mamut', 'mamut', 'mamut']


# 4) Genera una función que calcule la diferencia entre los valores de dos listas.
# Usa la función  map()

def diferencia_listas(lista1, lista2):
    '''
    La función recibe dos listas de números y devuelve una lista con la 
    diferencia entre los valores correspondientes de ambas listas.
    
    Parámetros:
        -lista1 (list): Primera lista de números.
        -lista2 (list): Segunda lista de números.
    
    Return:
        -list: Lista con las diferencias entre los valores de las dos listas.
    '''
    #Englobo la funcióm map() en list, ya que el ouput de map() es un objeto iterable, y quiero una lista como resultado.
    lista_diferencia_valores = list(map(lambda x, y: x - y, lista1, lista2))

    return print(f'La lista con la diferencia entre los valores de las dos listas es: {lista_diferencia_valores}')

#caso de uso:
lista1 = [10, 20, 30, 40]
lista2 = [1, 2, 3, 4]
calculo_diferencias = diferencia_listas(lista1, lista2)  
print(calculo_diferencias)


# 5) Ecribe una función que tome una lista de números como parámetro y un valor opcional 
# nota_aprobado, que por defecto es 5. La función debe calcular la media de los números 
# en la lista y determinar si la media es mayor o igual que nota aprobado. Si es así, 
# el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver 
# una tupla que contenga la media y el estado.
def calculo_aprobado(lista_numeros, nota_aprobado=5):
    '''
    La función recibe una lista de números y un valor con valor por defecto igual a 5, 
    calcula la media de los números en la lista y determina si la media es mayor o 
    igual que nota_aprobado. Devuelve una tupla con la media y el estado (aprobado/suspenso).
    
    Parámetros:
        -lista_numeros (list): Lista de números a procesar.
        -nota_aprobado (float): Valor opcional para determinar el estado de aprobado/suspenso.
    
    Return:
        -tuple: Tupla con la media y el estado.
    '''
    if not lista_numeros:  # Verifico si la lista está vacía
        return print("La lista está vacía, no se puede calcular la media ni la calificación.")
    
    media = sum(lista_numeros) / len(lista_numeros)  # Calculo de la media
    estado = "aprobado" if media >= nota_aprobado else "suspenso"  # Fijamos el estado según los datos
    
    return (media, estado)

# Caso de uso:
lista_numeros = [6, 7, 8, 9, 10]
calificación = calculo_aprobado(lista_numeros) 
print(calificación) 


# 6) Escribe una función que calcule el factorial de un número de manera recursiva.

def factorial_recursivo(x):
    '''
    La función calcula el factorial de un número de manera recursiva.
    
    Parámetros:
        -x (int): Número del cual se desea calcular el factorial.
    
    Return:
        -int: El factorial del número n.
    '''    
    if x < 0:
        return 'Número no permitido. Indica un número positivo'
    elif x == 0 or x == 1:
        return 1
    else:
        return x * factorial_recursivo(x - 1) # Llamada recursiva
    
# Caso de uso:
numero = 5
resultado = (factorial_recursivo(numero))
print(f'El factorial de {numero} es: {resultado}')  


# 7) Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función  map()

def tuplas_to_strings(lista_tuplas):
    '''
    La función recibe una lista de tuplas y convierte cada tupla en un string.
    
    Parámetros:
        -lista_tuplas (list): Lista de tuplas a convertir.
    
    Return:
        -list: Lista de strings resultante de la conversión de las tuplas.
    '''
    return list(map(lambda tupla: str(tupla), lista_tuplas))  # Convierte cada tupla a string
    #a lo que despues podríamos aplicar un join() si quisiéramos unir los elementos de cada tupla en un solo string o o que veamos conveniente.

# Caso de uso:
lista_tuplas = [(1, 2), (3, 4), (5, 6)]
resultado = tuplas_to_strings(lista_tuplas) 
print(f'La lista de strings resultante es: {resultado}') 

# 8) Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico 
# o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje 
# indicando si la división fue exitosa o no.

def dividir_numeros():
    '''
    La función recibe solicita dos números e intenta dividirlos. Manejamos excepciones 
    para valores no numéricos y división por cero.
    
    Parámetros:
        -num1 (float): Primer número.
        -num2 (float): Segundo número.
    
    Return:
        -str: Mensaje indicando si la división fue exitosa o no.
    '''
    # Solicito los números al usuario convietiendolos a float para poder hacer la división 
    # y los envuelvo en un try-except-else para manejar excepciones
    try:
        print(f'Ingresa dos números y te daremos el resultado de la división')
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        resultado = num1 / num2
    except ValueError:
        return print(f'Error: Entrada no válida, por favor ingresa números.')
    except ZeroDivisionError:
        return print(f'Error: No se puede dividir por cero.')
    else:
        return print(f'El resultado de la división: {round(resultado, 2)}') #pedimos que el resultado se redondee a dos decimales
# Orden para poder ejectuar el programa directamente, si se le nombra, ya que no lo importamos.    
if __name__ == "__main__":
    dividir_numeros() 


# 9)Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista 
# excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", 
# "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función  filter()

def mascotas_permitidas(mascotas):
    '''
    La función recibe una lista de nombres de mascotas y devuelve una nueva lista 
    excluyendo ciertas mascotas prohibidas en España.
    
    Parámetros:
        -mascotas (list): Lista de nombres de mascotas a filtrar.
    
    Return:
        -list: Nueva lista con las mascotas permitidas, excluyendo las no permitidas.
    '''
    # Lista de mascotas prohibidas
    mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"] 
    # devolvemos un print del resultado de un filter() para filtrar con una función lambda
    # las mascotas que no están en la lista de prohibidas, convirtiendolo a lista
    return print(list(filter(lambda mascota: mascota not in mascotas_prohibidas, mascotas)))

# Caso de uso:
mascotas = ["Mapache", "Perro", "Gato", "Serpiente Pitón", "Conejo", "Cocodrilo", "Oso", "Hamster"]
mascotas_permitidas(mascotas) 

    
# 10) Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, 
# lanza una excepción personalizada y maneja el error adecuadamente.
class ListaVaciaError(Exception): #consultado en IA, como crear una excepción personalizada
    pass  # Definimos una excepción personalizada llamada ListaVacia

def calcular_promedio(lista_numeros):     
    '''
    La función recibe una lista de números y calcula su promedio. Si la lista está vacía, 
    lanza una excepción personalizada y maneja el error adecuadamente.
    
    Parámetros:
        -numeros (list): Lista de números a procesar.
    
    Return:
        -float: Promedio de los números en la lista.

    Control excepciones:
        - Excepción personalizada "ListaVacíaError": Si la lista está vacía.
    '''
    try:
        if not lista_numeros:
            raise ListaVaciaError("La lista está vacía, no se puede calcular el promedio.")
        promedio = sum(lista_numeros) / len(lista_numeros)  # Calcula el promedio
        print(f'El promedio de la lista es: {promedio}')  # Imprime el promedio
   # Si entra la excepción personalizada, esta parte la recoge y muestra el mensaje de error
    except ListaVaciaError as e:
        print(e) 


# 11)Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor 
# no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las 
# excepciones adecuadamente.
def pedir_edad():
    '''
    La función solicita al usuario que introduzca su edad y maneja excepciones 
    para valores no numéricos o fuera del rango esperado.
    
    Parámetros:
        -edad (int): Edad introducida por el usuario.
    
    Return:
        -str: Mensaje indicando si la edad es válida o no.
    '''
    try:
        edad = int(input("Por favor, introduce tu edad: "))
        if edad < 0 or edad > 120:
            raise ValueError("Edad fuera del rango esperado (0-120).")
    except ValueError as e:
        return print(f'Error: {e}')
    else:
        return print(f'Tu edad es: {edad}')


# 12)Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. 
# Usa la función  map()

def longitud_palabras(frase):
    '''
    La función recibe una frase y devuelve una lista con la longitud de cada palabra.
    
    Parámetros:
        -frase (str): Frase a procesar.
    
    Return:
        -list: Lista con la longitud de cada palabra en la frase.
    '''
    # Utilizamos map() para aplicar la función len a cada palabra de la frase
    # Primero dividimos la frase en palabras usando split() y luego aplicamos len a cada palabra
    longitudes = list(map(lambda palabra: len(palabra), frase.split())) 
    return longitudes

#caso de uso:
frase1 = "Hola mundo esto es una prueba"
print(longitud_palabras(frase1))  


# 13) Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en 
# mayusculas y minúsculas. Las letras no pueden estar repetidas .Usa la función  map()
def letras_mayus_minus(caracteres):
    '''
    La función recibe un conjunto de caracteres y devuelve una lista de tuplas 
    con cada letra en mayúsculas y minúsculas, sin repeticiones.
    
    Parámetros:
        -caracteres (str): Conjunto de caracteres a procesar.
    
    Return:
        -list: Lista de tuplas con cada letra en mayúsculas y minúsculas.
    '''
    # Utilizamos set() para eliminar duplicados 
    letras = set(caracteres)
    return list(map(lambda letra: (letra.upper(), letra.lower()), letras))  # Con función lamda marcamos una lista que
    #englobe el map() que tendrá por tanto una lista con tuplas de parejas de los en mayuscula y minuscula
     
# Caso de uso:
conjunto_caracteres = "3abcaBC123"

print(letras_mayus_minus(conjunto_caracteres))


# 14) Crea una función que retorne las palabras de una lista de palabras que comience con una letra en 
# especifico. Usa la función filter()

def palabras_con_letra(palabras, letra):
    '''
    La función recibe una lista de palabras y una letra, y devuelve una lista 
    con las palabras que comienzan con la letra especificada.
    
    Parámetros:
        -palabras (list): Lista de palabras a filtrar.
        -letra (str): Letra con la que deben comenzar las palabras.
    
    Return:
        -list: Lista de palabras que comienzan con la letra especificada.
    '''
    # Utilizamos filter() para filtrar las palabras que comienzan con la letra especificada
    return list(filter(lambda palabra: palabra.startswith(letra), palabras))
    # Observación: la mayoría de los casos que vemos hasta ahora se pueden solucionar con bucles FOR como 
    # en este caso:
    #      resultado = []
    #   for palabra in palabras:
    #       if palabra.startswith(letra):
    #           resultado.append(palabra)
    #   return resultado
    # Las funciones lambda y en este caso filter() son más concisas, aunque pueden ser a veces menos legibles para principiantes 
    # y se pueden ser complejas si no lo fragmentamos.

#Caso de uso:
lista_palabras = ["manzana", "banana", "cereza", "mango", "pera"]
print(palabras_con_letra(lista_palabras, "m"))  # Salida: ['manzana', 'mango']


# 15) Crea una función  lambda  que  sume 3 a cada número de una lista dada.
def suma_tres(lista_numeros):
    '''
    La función recibe una lista de números y devuelve una nueva lista 
    con 3 sumados a cada número.
    
    Parámetros:
        -lista_numeros (list): Lista de números a procesar.
    
    Return:
        -list: Nueva lista con 3 sumados a cada número.
    '''
    return list(map(lambda x: x + 3, lista_numeros))


# 16) Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista 
# de todas las palabras que sean más largas que n. Usa la función  filter()
def palabras_mas_largas(cadena, n):
    '''
    La función recibe una cadena de texto y un número entero n, y devuelve una lista 
    de todas las palabras que son más largas que n.
    
    Parámetros:
        -cadena (str): Cadena de texto a procesar.
        -n (int): Número entero que define la longitud mínima de las palabras.
    
    Return:
        -list: Lista de palabras que son más largas que n.
    '''
    # Dividimos la cadena en palabras y usamos filter() para filtrar las palabras más largas que n
    return list(filter(lambda palabra: len(palabra) > n, cadena.split()))

# Caso de uso:
cadena_texto = "Esta es una cadena de texto con varias palabras"
n = 4
print(palabras_mas_largas(cadena_texto, n))
    

# 17) Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] 
# corresponde al número quinientos setenta y dos (572). Usa la función  reduce()

from functools import reduce  #para utilizar la función reduce() debemos importarla desde el módulo functools

def convierte_a_numero(lista_digitos):
    '''
    La función recibe una lista de dígitos y devuelve el número correspondiente.
    
    Parámetros:
        -lista_digitos (list): Lista de dígitos a convertir.
    
    Return:
        -int: Número correspondiente a la lista de dígitos.
    '''
    # Utilizamos reduce() para combinar los dígitos en un solo número con una operación matemática
    # que multiplica el número acumulado por 10 y le suma el siguiente dígito.
    numero = reduce(lambda x, y: x * 10 + y, lista_digitos)
    return numero

# Caso de uso:
lista_digitos = [5, 7, 2]
convierte_a_numero(lista_digitos)


# 18) Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes 
# (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 
# 90.

def calificacion_alta(estudiante): 
    '''
    La función recibe una lista de diccionarios con información de estudiantes y 
    devuelve una lista de estudiantes con calificación mayor o igual a 90.
    
    Parámetros:
        -estudiante (list): Lista de diccionarios con información de estudiantes.
    
    Return:
        -list: Lista de estudiantes aprobados (calificación >= 90).
    '''
    # Utilizamos filter() para filtrar los estudiantes con calificación >= 90
    estudiantes_destacados = list(filter(lambda estudiante: estudiante['calificacion'] >= 90, estudiantes))
    return estudiantes_destacados

# Caso de uso:
# Creamos una lista de diccionarios con información de estudiantes
estudiante = [
    {"nombre": "Ana García", "edad": 20, "calificacion": 95},
    {"nombre": "Carlos López", "edad": 19, "calificacion": 87},
    {"nombre": "María Rodríguez", "edad": 21, "calificacion": 92},
    {"nombre": "Juan Pérez", "edad": 22, "calificacion": 78},
    {"nombre": "Laura Martínez", "edad": 20, "calificacion": 96},
    {"nombre": "Pedro Sánchez", "edad": 19, "calificacion": 89},
    {"nombre": "Isabel Torres", "edad": 21, "calificacion": 93},
    {"nombre": "Miguel Herrera", "edad": 20, "calificacion": 85},
    {"nombre": "Carmen Ruiz", "edad": 22, "calificacion": 90},
    {"nombre": "Diego Morales", "edad": 19, "calificacion": 88}
]
calificacion_alta(estudiante)


#19) Crea una función  lambda  que filtre los números impares de una lista dada.
def filtrar_impares(numeros):
    '''
    La función recibe una lista de números y devuelve una nueva lista 
    con los números impares filtrados.
    
    Parámetros:
        -numeros (list): Lista de números a filtrar.
    
    Return:
        -list: Nueva lista con los números impares.
    '''
    impares = list(filter(lambda numero: numero % 2 != 0, numeros))
    return impares

# Caso de uso:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtrar_impares(numeros)


# 20) Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int.
# Usa la función filter()

def filtrar_enteros(lista_enteros_caracteres):
 
    '''
    La función recibe una lista con elementos de tipo integer y string, 
    y devuelve una nueva lista sólo con los valores int.
    
    Parámetros:
        -lista_enteros_caracteres (list): Lista de elementos int y string a filtrar.
    
    Return:
        -list: Nueva lista con solo los valores int.
    '''
    # Utilizamos filter() para filtrar los elementos que son de tipo int ayudandonos de la función isinstance(),
    # que he buscando en documentación Python filtrando con Chatgpt.
    enteros = list(filter(lambda x: isinstance(x, int), lista_enteros_caracteres))
    return enteros

# Caso de uso:
lista = [1, 'dos', 3, 'cuatro', 5, 'seis', 7, 'ocho', 9, 'diez']
filtrar_enteros(lista)