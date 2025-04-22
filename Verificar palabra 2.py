def palindromo(palabra):  # Definimos la funcion palindromo
    palabra = palabra.lower().strip() # Si por casulidad se ingresa una palabra en mayuculas, se la cambia a minusculas  
    longitud = len(palabra) # Obtenemos la cantidad de letras de la palabra ingresada 

    for i in range(longitud // 2): # Solamente iteramos la mitad de letras de la palabra ingresada 
        if palabra[i] != palabra[longitud - i - 1]: # Este condicional compara los caracteres de la palabra en ambos extremos
            return False # En caso de que los caracteres no sean iguales, retorna falso 
    return True # Pero si los caracteres son iguales, el programa constata que se ha ingresado un palindromo

palabra = input("ingrese una palabra: ") # Se solicita al usuario por consola una palabra 
if palindromo(palabra):   # Se convoca a la funcion palindromo para que verifique la palabra ingresada
    print(f'"{palabra}" es un palindromo') # Si cumple la funcion, imprime este mensaje con la palabra digitada 
else: 
    print(f'"{palabra}" no es un palindromo') # De lo contrario, imprime este mensaje. 
