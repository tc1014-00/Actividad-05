#encoding: UTF-8
#David Salvador Ruiz Roa
#5

def convertir(peso,altura):
    a = peso/(altura*altura)
    return a

def idm(masa):
    b = ""
    
    if masa>25:
        b = "Sobrepeso"
    
    elif masa<26 and masa>18.5:
        b = "Peso Normal"
    
    elif masa<18.5: 
        b = "Bajo Peso"
        
    return b
        

def main():
    peso = int(input("ingrese peso"))    
    altura = int(input("ingrese altura"))
    
    masa = convertir(peso,altura)
    indice = idm(masa)
    
    print("Estado:",indice)
    
main()