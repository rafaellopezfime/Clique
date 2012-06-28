import random
from sys import argv

def main():
    
    genera = False

    try:
        entrada = open(argv[1], 'r')
        print 'Leyendo instancia del archivo <%s>...' % argv[1]
        
        objetos = None
        for linea in entrada.readlines():
            linea = linea.strip()
            if len(linea) == 0:
                continue
            tokens = linea.split()
            try:
                if tokens[0] == '#':
                    print 'Comentario: %s' % linea
                else:
                    if objetos is None:
                        objetos = list()
                        
                    else:
                        k = float(tokens[0])
                        densidad = float(tokens[1])
                       
            except:
                print 'Linea rara: ' % linea
        entrada.close()
        n = len(objetos)
        print 'Son %d objetos en la instancia.' % n
    except:
        genera = True

    if genera:
        n = int(argv[1]) # raw_input('Cantidad de objetos: '))
        k = float(argv[2]) #raw_input('Camarilla inicial: '))
        densidad = float(argv[3]) #raw_input('Densidad de arista: '))
        print '# Generando %d objetos' % n
	print '# Camarilla inicial %d' % k
	print '# Densidad de aristas %f' % densidad

      
      #agregar nodos al azar
	for i in range (n):
		for j in range (n):
			if (i != j):
				if ( i <= k and j <= k ):
					print "Los nodos [%d, %d] estan unidos" % (i, j)

				else:
					if ( random.random() <= densidad ):
						print "Los nodos [%d, %d] estan unidos" % (i, j)
					else:
						print "Los nodos [%d, %d] no estan unidos" % (i, j)

			else:
				print ""

main()
