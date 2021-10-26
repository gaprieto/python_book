# futbol.py
# Programa para interactuar con strings

a = input("Who is the best soccer player in the world ")

if (a.find("onal")>-1 or a.find("rist")>-1):
   print("Eres hincha del Real Madrid")
elif (a.find("Leo")>-1 or a.find("essi")>-1):
   print("Te gusta el Barcelona")
else:
   print("De acuerdo, James debe jugar mas en el RM")


