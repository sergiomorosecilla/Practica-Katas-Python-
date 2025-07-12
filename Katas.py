
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
    Esta función recibe una lista de números y un valor opcional nota_aprobado, 
    calcula la media de los números en la lista y determina si la media es mayor o 
    igual que nota_aprobado. Devuelve una tupla con la media y el estado ("aprobado" o "suspenso").
    
    Parámetros:
        -lista_numeros (list): Lista de números a procesar.
        -nota_aprobado (float): Valor opcional para determinar el estado de aprobado/suspenso.
    
    Return:
        -tuple: Tupla con la media y el estado.
    '''
    if not lista_numeros:  # Verifico si la lista está vacía
        return print("La lista está vacía, no se puede calcular la media ni la calificación.")
    
    media = sum(lista_numeros) / len(lista_numeros)  # Calcula la media
    estado = "aprobado" if media >= nota_aprobado else "suspenso"  # Determina el estado
    
    return (media, estado)

# Caso de uso:
lista_numeros = [6, 7, 8, 9, 10]
calificación = calculo_aprobado(lista_numeros) 
print(calificación) 


# 6) Escribe una función que calcule el factorial de un número de manera recursiva.
