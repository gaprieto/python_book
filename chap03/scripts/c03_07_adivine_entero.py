# adivine_entero.py
# Juego donde el usuario adivina un número
#

import numpy as np  

# Genera un número aleatorio entre [1 y 1000)
number = np.random.randint(1,1000)

# Empieze el juego y cuente los intentos. 
guesses  = 1
guess    = int(input('Adivine un número del 1 al 1000: '))

while guess!=number:
    guesses = guesses + 1
    if (guess>number):
        print(guess," es muy alto")
    elif (guess<number):
        print(guess," es muy bajo")
    
    guess = int(input("Adivine otra vez: "))

print("\nExcelente, adivinaste en ",guesses, ' intentos')

