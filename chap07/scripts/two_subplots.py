"""
two_subplots.py
 Programa para iniciar 2 subplots en una sola figura
 subplots están vacíos
"""
import numpy as np
import matplotlib.pyplot as plt

fig,ax = plt.subplots(nrows=1,ncols=2)
print(ax)
plt.savefig('../figs/chap07_obj2.pdf',bbox_inches='tight', pad_inches=0)
plt.show()

