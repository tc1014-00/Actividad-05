#encoding: UTF-8
# Jorge Daniel Juarez Ruiz
# Dar a conocer el color que resulta al mezclar dos primarios

def mezclarColores (c1,c2):
    cr=""
    if c1=="rojo":
        if c2=="amarillo":
            cr="Naranja"
            return cr
        elif c2=="azul":
            cr="Morado"
            return cr
        elif c2=="rojo":
            cr="Rojo"
            return cr
    if c1=="amarillo":
        if c2=="amarillo":
            cr="Amarillo"
            return cr
        elif c2=="azul":
            cr="Verde"
            return cr
        elif c2=="rojo":
            cr="Naranja"
            return cr
    if c1=="azul":
        if c2=="amarillo":
            cr="Verde"
            return cr
        elif c2=="azul":
            cr="Azul"
            return cr
        elif c2=="rojo":
            cr="Morado"
            return cr
    else:
        cr="ERROR: No tecleo rojo, amarillo o azul"
        return cr
    

def main():
    color1=input("Color 1")
    c1= color1.lower()
    color2=input("Color 2")
    c2= color2.lower()
    resultante=mezclarColores(c1, c2)
    print (resultante)
    
main()