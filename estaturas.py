import random
l = list()
m = 0
n = 0
#Ingresamos aleatoriamente las estaturas a una lista.
for e in range(0,32):
	l.append(random.randrange(100,200))

'''Comparamos las estaturas ingresadas, los maximos lo almacenamos en una mueva lista, 
	y los minimos en un diccionario, son 16 comparaciones.'''
dic = {}
a = 0
b = 1
l2 = list()
for i in range((len(l)/2)):
	if(l[a]>=l[b]):
		dic[l[b]] = [l[a],l[b]]
		l2.append(l[a])
	a +=2
	b +=2

#Eliminamos  los maximos de la lista original
for j in l2:
	if j in l:
		l.remove(j)

#Eliminamos los minimos de la lista original.
l3 = dic.keys()
for k in l3:
	if k in l:
		l.remove(k)

#Comvertimos a tuplas la lista de maximos y la nueva lista del que hemos quitado los maximos y minimo.
l4 = tuple(l2)
l5 = tuple(l)

#Creamos una lista final de maximos de la lista  de maximos, minimos y lo que sobraron de la lista original. 
lf = [max(l5),max(l3),max(l4)]
lf.sort()

#resultado.
print('Primer maximo ' + str(lf[-1])+' Segundo maximo '+str(lf[-2]))
	

