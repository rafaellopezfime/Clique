import random
from sys import argv

def lectura(archivo):
    entrada = open(archivo, 'r')
    print 'Leyendo instancia del archivo <%s>...' % argv[1]
    
    nodos = None
    for linea in entrada.readlines():
        linea = linea.strip()
        if len(linea) == 0:
            continue
        tokens = linea.split()
        try:
            if tokens[0] == '#':
                print 'Comentario: %s' % linea
            else:
                if nodos is None:
                    nodos = list()
                else:
                    c_inicial = float(tokens[0])
                    densidad = float(tokens[1])
        except:
            print 'Linea rara: ' % linea
    entrada.close()
    n = len(nodos)
    print 'Se crearon %d nodos.' % n
    return (k, n)

def genera(argv):
    try:
        n = int(argv[1]) 
    except:
        n = int(raw_input('Cantidad de nodos: '))
    print '# Generando %d nodos' % n

    try:
        k = int(argv[2]) 
    except:
        k = int(raw_input('clique inicial: '))
	print '# Clique incial de grado: %d' % k

    try:
        p = float(argv[3]) 
    except:
        p = float(raw_input('densidad: '))
	print '# densidad: %f' % p
	
	nodos = list() #lista de todos los nodos conectados

	for i in range(n):
		for j in range(n):
				if (i != j and j>=i):
					if (i<k and j<k):
						nodos.append((i,j))
						nodos.append((j,i))
						print "SI [%d -> %d]" % (i, j)
					else:
						if (random.random () <= p):
							nodos.append((i,j))
							nodos.append((j,i))
							print "SI [%d -> %d]" % (i, j)
						#else:
						#	print "NO [%d -> %d]" % (i, j)
				#else:
				#	print "NO [%d -> %d]" % (i, j)
    return (k, nodos)

def muestra(k, nodos):
	print "nodos conectados(adyacentes)"
	for (i, j) in nodos:
		print i, j
    
def inferior(k, nodos):
	cota = 2
	return cota

def superior(k, nodos):
	cota = 5
	return cota

def main():
    try:
        (k, nodos) = lectura(argv[1])
    except:
        (k, nodos) = genera(argv)

    muestra(k, nodos)

    print '# Cota inferior: %f' % inferior(k, nodos)
    print '# Cota superior: %f' % superior(k, nodos)

    return


main()
