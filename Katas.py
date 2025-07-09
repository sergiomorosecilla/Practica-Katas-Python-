
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

