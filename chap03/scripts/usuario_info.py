# usuario_info.py
# Código que solicita información del usuario
# y reporta los resultados
#

name   = input("Cuál es su nombre? ")

txt    = input('Cuál es su altura (m)? ')
alt    = float(txt)

txt   = input('Cuánto pesa Ud. (kg)? ')
weigh = float(txt)

print ('%s, Ud. mide %4.2f m y pesa %5.1f kg' 
       % (name,alt,weigh))

