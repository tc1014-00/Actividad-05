#encoding: UTF-8
# Jorge Daniel Juárez Ruiz
# Convertir los numeros 1-10 a romanos

def convertirArabigo(a):
    if a>=1 and a<=10:
        if a<=3:
            r=a*("I")
            return r
        elif 5<=a<=8:
            r=a-5
            r="V"+r*"I"
            return r
        elif a==4:
            r="IV"
            return r
        elif a==9:
            r="IX"
            return r
        elif a==10:
            r="X"
            return r
    else:
        r="ERROR: No es un numero de 1 a 10"
        return r

def main(): 
    numArabigo=int(input("Numero romano de 1-10"))
    numRomano=convertirArabigo(numArabigo)
    print(numRomano)
    
main()