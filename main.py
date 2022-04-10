#Contexto
#La criptografía de curva elíptica (ECC) existe desde mediados de la década de 1980, 
#pero todavía se la considera la recién llegada al mundo de SSL y solo ha comenzado a
#ganar adopción en los últimos años. ECC es un enfoque matemático fundamentalmente diferente 
#al cifrado que el venerable algoritmo RSA. Una curva elíptica es una función algebraica (y2 = x3 ax b) 
#que parece una curva simétrica paralela al eje x cuando se traza. 
#Al igual que con otras formas de criptografía de clave pública, ECC se basa en una propiedad 
#unidireccional en la que es fácil realizar un cálculo pero no es factible revertir o invertir 
#los resultados del cálculo para encontrar los números originales. 
#ECC utiliza operaciones matemáticas diferentes a las de RSA para lograr esta propiedad. 
#La forma más fácil de explicar esta matemática es: para una curva elíptica, una línea solo pasará 
#por tres puntos a lo largo de la curva (P, Q y R), y al conocer dos de los puntos (P y Q), el otro (R) 
#se puede calcular fácilmente, pero con solo R, los otros dos, P y Q, no se pueden derivar.

from random import randint

if __name__ == '__main__':

	P = 23
	
	G = 9
	
	
	print('El valor de P es :%d'%(P))
	print('El valor de G es :%d'%(G))
	
	# Alice seleccionara la llave privada a
	a = 4
	print('La PK para Alice es :%d'%(a))
	
	# Generamos la llave
	x = int(pow(G,a,P))
	
	# Bob seleccionara la llave privada b
	b = 3
	print('La PK para Bob es :%d'%(b))
	
	# Generamos la llave
	y = int(pow(G,b,P))
	
	
	# Llave secreta para Alice
	ka = int(pow(y,a,P))
	
	# Llave secreta para Bob
	kb = int(pow(x,b,P))
	
	print('La llave secreta para Alice es : %d'%(ka))
	print('La llave secreta para Bobo es : %d'%(kb))
