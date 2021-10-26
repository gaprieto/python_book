"""
adivine_entero2.py
Juego donde el usuario adivina un número, 
usando funciones
"""

def guess_number(number):
    """ Función para adivinar un número
    Función del usuario que hace el trabajo de 
    interactuar con el usuario y evaluar si adivinó el número.
    Entrada: number - un número, que el usuario no conoce

    Salida: guesses - Número de intentos
    """
    guesses  = 1
    guess    = int(input('Adivine un número del 1 al 1000: '))
    while guess!=number:
        guesses = guesses + 1
        if (guess>number):
            print(guess," es muy alto")
        elif (guess<number):
            print(guess," es muy bajo")
        guess = int(input("Adivine otra vez: "))
    
    return guesses

#-------------------------------------
# El programa principal
#-------------------------------------
import numpy as np                  

# Obtenga número aleatorio [1, 1000)
rnum = np.random.randint(1, 1000) 

# Llame a la funci´øn que interactua con usuario
nguess = guess_number(rnum)

print("\nExcelente, adivinaste en ",nguess, ' intentos')
