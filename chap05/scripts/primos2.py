"""
primos2.py
"""
import primos_subs as pr

nmax = 1000
primes,nprime = pr.primos_vector(nmax)

print ("# primos encontrados ", nprime)
print (primes)
