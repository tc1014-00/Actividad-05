#encoding: UTF-8
#David Salvador Ruiz Roa
#3

def mezclar(c1,c2):
    r = ""
    if c1 == "rojo" and c2 == "azul":
        r = "Morado"
    elif c1 == "azul" and c2 == "rojo":
        r = "Morado"
    elif c1 == "rojo" and c2 == "amarillo":
        r = "Naranja"
    elif c1 == "amarillo" and c2 == "rojo":
        r = "Naranja"
    elif c1 == "azul" and c2 == "amarillo":
        r = "Verde"
    elif c1 == "amarillo" and c2 == "azul":
        r = "Verde"
    else:
        r = "Error"
    return r
    
    
def main():
    color1 = raw_input("Escriba el primer color (Rojo, Azul, Amarillo)")
    color2 = raw_input("Escriba el segundo color (Rojo, Azul, Amarillo)")
    
    c1 = color1.lower()
    c2 = color2.lower()
    
    colorR = mezclar(c1,c2)
    print("El color resultante es:",colorR)
    
    
    



main()