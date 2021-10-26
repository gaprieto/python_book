# uer_info.py
# Simple code to ask the user some quick questions
# and report the results
#

name   = input("What is your name? ")

txt    = input('How tall are you? ')
alt = float(txt)

txt = input('How much do you weigh? ')
weigh = float(txt)

print ('%s, you are %4.2f tall and weigh %5.1f kg' 
       % (name,alt,weigh))

