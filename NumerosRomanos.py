#Encoding:UTF-8
#Autor: Paola Castillo Nacif
#Descripcion: El programa mostrara

def convNum(n):
    if n>10:
        n="Error"
    elif n==10:
        n="X"
    elif n==5:
        n="V"
    elif n>=1:
        v=((n//5)*"V")
        i=(((n%5))*"I")
        n=v+i
    elif n==1:
        n="I"
    return n
        
def main(): 
    n=int(input("Inserte numero arabigo"))
    resultadoR=convNum(n)
    print("Su numero en romano es:",resultadoR)
main()
