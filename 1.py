#encoding: UTF-8 
#David Salvador Ruiz Roa
# Numeros Romanos


def convertirRomano(numero):
    Roman = ""
    if numero == 1:
        Roman = "I"
    elif numero == 2:
        Roman = "II"
    elif numero == 3:
        Roman = "III"
    elif numero == 4:
        Roman = "IV"
    elif numero == 5:
        Roman = "V"
    elif numero == 6:
        Roman = "VI"
    elif numero == 7:
        Roman = "VII"
    elif numero == 8:
        Roman = "VIII"
    elif numero == 9:
        Roman = "IX"
    elif numero == 10:
        Roman = "X"
    else:
        Roman = "ERROR, El número no es de 1-10"
    
    return Roman
    

def main():
    numero = int(input("Digite un número entre 1 y 10"))
    Romano = convertirRomano(numero)
    print("El número romano es:",Romano)
    
main()