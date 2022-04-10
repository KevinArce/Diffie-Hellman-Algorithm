# Diffie-Hellman-Algorithm
Implementacion del algortimo Diffie-Hellman en Python
-----------------------------------------------------

La criptografía de curva elíptica (ECC) existe desde mediados de la década de 1980, pero todavía se la considera 
la recién llegada al mundo de SSL y solo ha comenzado a ganar adopción en los últimos años. ECC es un enfoque matemático 
fundamentalmente diferente al cifrado que el venerable algoritmo RSA. Una curva elíptica es una función algebraica (y2 = x3 ax b) 
que parece una curva simétrica paralela al eje x cuando se traza. (Consulte las figuras a continuación). 
Al igual que con otras formas de criptografía de clave pública, ECC se basa en una propiedad unidireccional en la que es fácil 
realizar un cálculo pero no es factible revertir o invertir los resultados del cálculo para encontrar los números originales. 
ECC utiliza operaciones matemáticas diferentes a las de RSA para lograr esta propiedad. 
La forma más fácil de explicar esta matemática es: para una curva elíptica, una línea solo pasará por tres puntos a lo largo de la curva (P, Q y R), 
y al conocer dos de los puntos (P y Q), el otro (R) se puede calcular fácilmente, pero con solo R, los otros dos, P y Q, no se pueden derivar.

![image](https://user-images.githubusercontent.com/29236093/162641197-5656e7c0-4955-4614-8ea2-8eda9a3957f5.png)

Cuyas ecuaciones son como la siguiente: 
y^2 = x(x^2+69x+100)
