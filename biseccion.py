import math

def biseccion(f,inicio,fin,error):
	raiz = []
	if(biseccion_rec(f,inicio,fin,error,raiz)):
		return raiz[0]
	raise ValueError("No hay raiz")


def biseccion_rec(f,inicio,fin,error,raiz):
	medio = calcular_medio(inicio,fin)
	if(modulo(f(inicio))<=error or modulo(f(medio))<=error or modulo(f(fin))<=error):
		raiz.append(medio)
		return True
	if(f(inicio)*f(medio)>0 and f(medio)*f(fin)>0):
		return False
	if(f(inicio)*f(medio)<0):
		biseccion_rec(f,inicio,medio,error,raiz)
	biseccion_rec(f,medio,fin,error,raiz)
	return True

def calcular_medio(inicio,fin):
	return (inicio+fin)/2
	
def modulo(n):
	if(n<0):
		return -n
	return n

def f(x):
	return x*x/4 - math.sin(x) 

def main():
    print(biseccion(f,1.5,2,0.02))
main()
