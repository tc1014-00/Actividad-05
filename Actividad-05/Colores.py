#encoding: UTF-8
#Autor: Hector manuel Takami Flores
#Calcula colores

def convierteCaracteres1(c1):
    caracter=c1
    color1=caracter.lower()
    return color1
def convierteCaracteres2(c2):    
    caracter=c2
    color2=caracter.lower()
    return color2
    
def calculaColor(c1,c2):
    color=""
    if c1=="rojo":
        if c2=="amarillo":
            color="naranja"
            return color
        elif c2=="azul":
            color="morado"
            return color
        elif c2=="rojo":
            color="rojo"
            return color
    if c1=="azul":
        if c2=="amarillo":
            color="verde"
            return color
        elif c2=="azul":
            color="azul"
            return color
        elif c2=="rojo":
            color="morado"
            return color
    if c1=="amarillo":
        if c2=="amarillo":
            color="amarillo"
            return color
        elif c2=="azul":
            color="verde"
            return color
        elif c2=="rojo":
            color="naranja"
            return color
    else:
        color="Error"
        return color
            


def main():
    c1=str(input("Introduzca el primer color"))
    c2=str(input("Introduzca el segundo color"))
    print(c1,"+",c2,"=",calculaColor(c1,c2))
    
    
main() 