# primos3.py
import primos_subs as pr

primes,nprime = pr.primos_vector(1000)

print ("# primos encpontrados ", nprime)

nprint = 0
for i in range(1,nprime):
      nprint = nprint + 1
      if (nprint%10==0 ):
         print ("%4i" % (primes[i]))
      else:
         print ("%4i" % (primes[i]),end="")
print('')

