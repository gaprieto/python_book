# presión litosférica 
# con función interna

def lithos_press(depth,rho=2700.):
    import numpy as np

    g   = 9.8    # m/s2
    rho = 2700.0 # kg/m3
    
    P = g*rho*depth
    
    return P

#------------------------------------
# Main program
#------------------------------------

fmt = "%5.1f %14.1f "

print('Prof.  Presión (MPa)')
for i in range(11):
   h = float(i)*5*1000  # depth(m)
   P = lithos_press(h)        # Pascal
   PMpa = P/1e6      # MPa
   print(fmt %(h/1000 ,PMpa))

