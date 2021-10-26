# primos4.py

import clase.homework as hw
import numpy as np
import reshape_prime as rp

# Primero, obtenga el vector con muchos primos
primes,nprime = hw.primos_vector(1000)
print ("# primos encontrados ", nprime)

# Ahora, reorganize matriz, con diferentes tamaños
c4 = rp.reshape_prime(primes,4)
print("Matrix organized in spiral")
print(c4)

c = rp.reshape_prime(primes,5)
print("Matrix organized in spiral")
print(c)

c = rp.reshape_prime(primes,6)
print("Matrix organized in spiral")
print(c)

c = rp.reshape_prime(primes,7)
print("Matrix organized in spiral")
print(c)



