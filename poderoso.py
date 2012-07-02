import random
from sys import argv
import numpy

def genera(argv):
    try:
        n = int(argv[1]) 
    except:
        n = int(raw_input('Cantidad de nodos: '))
    print '# Generando %d nodos' % n

    try:
        k = int(argv[2]) 
    except:
        k = int(raw_input('Clique inicial: '))
    print '# Clique incial de grado: %d' % k

    try:
        p = float(argv[3]) 
    except:
        p = float(raw_input('Densidad: '))
    print '# Densidad: %f' % p
	
    adj = numpy.empty((n, n))
    m = 0
    for i in range(n):
        for j in range(n):
            if j > i:
                if (i < k and j < k) or (random.random () <= p):
                    #print "Arista (%d, %d) agregada." % (i, j)
                    adj[i, j] = adj[j, i] = 1
                    m += 1
                else:
                    adj[i, j] = adj[j, i] = 0
            elif j == i:
                adj[i, j] = adj[j, i] = 0
    print '# %d aristas generadas' % m
    return (adj, n, m)

def cotaInferior(adj, n, m):
	if m > 0:
            return 2
	else:
            return 1

def cotaSuperior(adj, n, m):
    grado = list()
    for i in range(n):
        print adj[i, :]
        grado.append(sum(adj[i, :]))
    #print grado
    return grado
		
def factible(solucion, adj):
    for nodo in solucion:
        for otroNodo in solucion:
            if not nodo == otroNodo and adj[nodo, otroNodo] == 0:
                return False
    return True

def objetivo(solucion):
    return len(solucion)	

def inicial(adj, n, m):
    intentos = 20
    seleccion = list()
    while intentos > 0:
        nodo = random.randint(0, n-1)
        if not nodo in seleccion:
            falta = False
            for incluido in seleccion:
                #print 'Checando si hay arista entre %d y %d' % (incluido, nodo)
                if not adj[incluido, nodo]:
                    falta = True
                    intentos -= 1
                    break
            if not falta:
                seleccion.append(nodo)
                #print 'Nodo %d agregado a la solucion inicial' % nodo
    return seleccion

def main():
    (adj, n, m) = genera(argv)

    print '# Cota inferior: %d' % cotaInferior(adj, n, m)
    print '# Cota superior: %d' % cotaSuperior(adj, n, m)

    solucion = inicial(adj, n, m)
    print '# Objetivo: %d' % objetivo(solucion)
    print '# Factible: %s' % factible(solucion, adj)

    return

main()