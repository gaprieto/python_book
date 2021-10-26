# presión litosférica 
# con función en Modulo propio

import clase.homework as hw
fmt = "%5.1f %14.1f "

print('Prof.  Presión (MPa)')
for i in range(11):
   h = float(i)*5*1000  # depth(m)
   P = hw.lithos_press(h)        # Pascal
   PMpa = P/1e6      # MPa
   print(fmt %(h/1000 ,PMpa))


