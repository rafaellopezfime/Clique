import random

def main ():
n = int(raw_input("Dame el total de nodos: "))
print "Generando %d nodos" % n

k = int(raw_input("clique inicial: "))
print "Generando %d cliques" % k

densidad = float(raw_input("Densidad del arco: "))
print "Generando %f densidad" % densidad

#agregar nodos al azar
for i in range (n):
for j in range (n):
if (i != j):
if ( i <= k and j <= k ):
    print "El nodo [%d, %d] estan unidos" % (i, j)
else: 
if ( random.random() <= densidad ):
print "El nodo [%d, %d] estan unidos" % (i, j)

else: 
print ""

main()
