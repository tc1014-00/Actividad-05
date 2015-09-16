#Encoding:UTF-8
#Autor: Paola Castillo Nacif
#El programa mostrara los colores resultantes de diferentes combinaciones

def combinarColores(c1m,c2m,c1M,c2M):
    color=""
    if (c1m=="rojo" and c2m=="azul") or (c1m=="azul" and c2m=="rojo"):
        color="Morado"
    elif (c1m=="rojo" and c2m=="amarillo") or (c1m=="amarillo" and c2m=="rojo"):
        color="Naranja"
    elif (c1m=="azul" and c2m=="amarillo") or (c1m=="amarillo" and c2m=="azul"):
        color="Verde"
    elif (c1m=="rojo" and c2m=="rojo"):
        color="Rojo"
    elif (c1m=="amarillo" and c2m=="amarillo"):
        color="Amarillo"
    elif (c1m=="azul" and c2m=="azul"):
        color="Azul"
    elif (c1M=="rojo" and c2M=="azul") or (c1M=="azul" and c2M=="rojo"):
        color="Morado"
    elif (c1M=="rojo" and c2M=="amarillo") or (c1M=="amarillo" and c2M=="rojo"):
        color="Naranja"
    elif (c1M=="azul" and c2M=="amarillo") or (c1M=="amarillo" and c2M=="azul"):
        color="Verde"
    elif (c1M=="rojo" and c2M=="rojo"):
        color="Rojo"
    elif (c1M=="amarillo" and c2M=="amarillo"):
        color="Amarillo"
    elif (c1M=="azul" and c2M=="azul"):
        color="Azul"
    else:
        color="Error"
    return color
    
def main():
    c1=input("Inserte color uno")
    c1m=c1.lower()
    c1M=c1.upper()
    c2=input("Inserte color dos")
    c2m=c2.lower()
    c2M=c2.upper()
    cResultante=combinarColores(c1m,c2m,c1M,c2M)
    print("El color resultante de su combinacion es:",cResultante)
main()