"""
# Tehtävät

Tehtävät liittyvät ohjelmisto 2:n tehtävään 1:

1. Toteuta tehtävä 1 (jossa kolme tehtävää) pythonilla
1. Laske tehtävän 2 suorakulmaisen kolmion hypotenuusan pituus käyttäen sopivaa numpyn funktiota.
"""
import numpy

#1. tehtävä
print("Tehtävä 1")
A = numpy.array([2.493,0.911])
B = numpy.array([137.7,62.3])
C = numpy.array([30,45,60,90,120,135,150,180,270,360])
print(numpy.degrees(A))
print(numpy.radians(B))
print(numpy.radians(C))
#2 tehtävä
print("\nTehtävä 2")
print(numpy.hypot(1.6,2.3))