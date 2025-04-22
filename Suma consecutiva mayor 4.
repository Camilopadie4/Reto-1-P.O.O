def mayor_suma_consecutiva(lista): # Definimos una funcion que evalue una lista de numeros(argumento)
    if len(lista) < 2: # La lista debe tener mas de 2 elementos
        return None
    mayor_suma= lista[0] + lista[1] # Iniciamos con una posible suma consecutiva mayor 
    
    for i in range(len(lista) - 1):  # Iteramos hasta el penultimo numero
        suma_actual = lista[i] + lista[i + 1]  # Realiza la suma consecutiva 
        if suma_actual > mayor_suma:  
            mayor_suma = suma_actual # Actualiza la lista con la mayor suma que vaya encontrando 
    return mayor_suma 

lista_numeros= [int(num) for num in input("ingrese numeros separados por espacios: ").split()]  # En esta lista guarda los numeros enteros que ingresa el usuario   
print("Mayor suma consecutiva generada:", mayor_suma_consecutiva(lista_numeros)) # Convocamos la funcion "Mayor-suma-consecutiva" y, si se cumple, imprime la mayor suma generada  

