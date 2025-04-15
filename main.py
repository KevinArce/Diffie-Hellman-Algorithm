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
