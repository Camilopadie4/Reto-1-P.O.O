from collections import defaultdict # Importamos este diccionario que permite crear listas vacias para cada palabra ordenada 
def filtrar_anagramas(lista): # Definimos una funcion que reciba una lista de palabras y busque anagramas 
    agrupar= defaultdict(list) # Permite agrupar palabras que sean anagramas 
    for palabra in lista: # Recorremos toda la lista de palabras 
        orden= "".join(sorted(palabra)) # Organizamos en orden alafabetico las palabras y las añadimos a una nueva cadena
        agrupar[orden].append(palabra) # Se añade las palabras correspondientes a la lista ordenada
        resultado= [palabra for grupo in agrupar.values() if len(grupo) > 1 for palabra in grupo] # Creamos una lista para guardar los anagramas 
    return resultado # Devuelve la lista con mas de un anagrama 
    
lista_palabras= input("ingrese lista de palabras separadas por espacios: ").split() # Solicitamos al usuario por consola 
Resultado= filtrar_anagramas(lista_palabras) # Llamamos a nuestra funcion "filtrar-anagramas" para que ejecute las palabras ingresadas
print("Lista de anagramas:", Resultado) # Finalmente, se imprime la lista de palabras que coinciden en sus carateres 
