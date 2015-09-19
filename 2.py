#encoding:UTF-8
#David Salvador Ruiz Roa
#ejercicio 2

def calcularA1(a,b):
    area = a*b
    return area
    
def calcularP1(a,b):
    perimetro = (2*a) + (2*b)
    return perimetro
    
def calcularA2(A,B):
    area = A*B
    return area
    
def calcularP2(A,B):
    perimetro = (2*A) + (2*B)
    return perimetro 
   
def main():
    a = int(input("Base 1"))
    b = int(input("Altura 1"))
    A = int(input("Base 2"))
    B = int(input("Altura 2"))
    
    area1 = calcularA1(a,b)
    perimetro1 = calcularP1(a,b)
    area2 = calcularA2(A,B)
    perimetro2 = calcularP2(A,B)
    
    print("Area del rectangulo 1: ",area1)
    print("Perimetro del rectangulo 1: ",perimetro1)
    print("Area del rectangulo 2: ",area2)
    print("Perimetro del rectangulo 2: ",perimetro2)
    
    





main()