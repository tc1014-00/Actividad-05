#encoding UTF-8
#Autor: Mauricio Medrano, A01272273
# Imprimiendo Numeros Romanos

def convertir(numeroNormal):
    
    numeroRomano = " " 
    
    if numeroNormal <= 3 and numeroNormal >=1: 
      numeroRomano = numeroNormal*"I" 
    elif numeroNormal == 4: 
      numeroRomano = "IV" 
    elif numeroNormal >= 5 and numeroNormal <= 8:
      numeroRomano = "V" + "I" *(numeroNormal % 5)
    elif numeroNormal == 9: 
      numeroRomano = "IV" 
    elif numeroNormal == 10:  
      numeroRomano = "X"
    else : 
      numeroRomano = "error"  
    
    return numeroRomano

def main():
    numeroNormal = int(input("Numero Normal")) 
    numeroR = convertir(numeroNormal) 
    print ("El numero romano es", numeroR) 
main()
    
   