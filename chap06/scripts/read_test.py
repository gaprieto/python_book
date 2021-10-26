"""
read_test.py
 Lectura simple de un archivo de texto
"""

# linea por linea
print('Lectura de archivo: linea por linea')
fname = 'data/test_file.dat'
f = open(fname, 'r')
for line in f:
   print(line, end='')
f.close()

# poner en una lista
print('')
print('Lectura de archivo: en una lista')
f = open(fname, 'r')
f_list = list(f)
print(f_list)
print(f_list[1])
f.close()

# lectura completa
print('Lectura de archivo: en una variable')
f = open(fname, 'r')
text = f.read()
print(text)


