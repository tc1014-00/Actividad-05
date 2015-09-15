# encoding: UTF-8
# Autor:Humberto Serra Mendieta
# Recibe dos colores y devuelve color resultante

def convertirCaracteres1(color1):
    caracter=(color1)
    nombrecolor=caracter.lower()
    return nombrecolor
    
def convertirCaracteres2(color2):
    caracter=(color2)
    nombrecolor=caracter.lower()
    return nombrecolor
    
def combinarColor(c1,c2):
    if c1=="rojo":
        if c2=="azul":
            color="morado"
        elif c2=="amarillo":
            color="naranja"
        else:
            color="error"
    elif c1=="azul":
        if c2=="rojo":
            color="morado"
        elif c2=="amarillo":
            color="verde"
        else:
            color="error"
    elif c1=="amarillo":
        if c2=="rojo":
            color="naranja"
        elif c2=="azul":
            color="verde"
        else:
            color="error"    
    return color


def main():
    color1=str(input("Escriba el color 1"))
    color2=str(input("Escriba el color 2"))
    c1=convertirCaracteres1(color1)
    c2=convertirCaracteres2(color2)
    if c1=="rojo":
        if c2=="azul":
            cc=combinarColor(c1,c2)
            print(c1,"+",c2,"=",cc)
        elif c2=="amarillo":
            cc=combinarColor(c1,c2)
            print(c1,"+",c2,"=",cc) 
        elif c2=="rojo":
            print(c1,"+",c2,"= rojo")
        else:
            print("El color 2 no es primario")
    elif c1=="azul":
        if c2=="rojo":
            cc=combinarColor(c1,c2)
            print(c1,"+",c2,"=",cc)
        elif c2=="amarillo":
            cc=combinarColor(c1,c2)
            print(c1,"+",c2,"=",cc) 
        elif c2=="azul":
            print(c1,"+",c2,"= azul")    
        else:
            print("El color 2 no es primario")    
    elif c1=="amarillo":
        if c2=="azul":
            cc=combinarColor(c1,c2)
            print(c1,"+",c2,"=",cc)
        elif c2=="rojo":
            cc=combinarColor(c1,c2)
            print(c1,"+",c2,"=",cc) 
        elif c2=="amarillo":
            print(c1,"+",c2,"= amarillo")     
        else:
            print("El color 2 no es primario")        
    else: 
        print("El color 1 no es primario")
main() 