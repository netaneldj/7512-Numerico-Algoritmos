import math

def regula_falsi(f,inicio,fin,error):
	raiz = []
	if(regula_falsi_rec(f,inicio,fin,error,raiz)):
		return raiz[0]
	raise ValueError("No hay raiz")	
	
def regula_falsi_rec(f,inicio,fin,error,raiz):
	medio = calcular_medio(f,inicio,fin)
	if(modulo(f(inicio))<=error or modulo(f(medio))<=error or modulo(f(fin))<=error):
		raiz.append(medio)
		return True
	if(f(inicio)*f(medio)>0 and f(medio)*f(fin)>0):
		return False
	if(f(inicio)*f(medio)<0):
		regula_falsi_rec(f,inicio,medio,error,raiz)
	regula_falsi_rec(f,medio,fin,error,raiz)
	return True	
	
def calcular_medio(f,inicio,fin):
	return (fin*f(inicio)-inicio*f(fin))/(f(inicio)-f(fin))

	
def modulo(n):
	if(n<0):
		return -n
	return n

def f(x):
	'''return x*x/4 - math.sin(x)'''
	return math.sin(x)-0.5*math.sqrt(x) 
	
def main():
	'''print(regula_falsi(f,1.5,2,0.02))'''
	print(regula_falsi(f,0.000001,2,0.02))
main()
