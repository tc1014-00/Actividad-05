# encoding UTF-8
# Autor: Mauricio Medrano Castro, A01272273
# Calculando perimetro y area de rectangulos 

def calculoPerimetroUno (baseUno, alturaUno):  
    pUno = (2 * baseUno) + (2 * alturaUno) 

    return pUno
    
def calculoAreaUno (baseUno, alturaUno): 
    aUno = baseUno * alturaUno 
  
    return  aUno

def calculoPerimetroDos (baseDos, alturaDos):
    pDos = (2 * baseDos) + (2 * alturaDos)
    
    return pDos 
    
def calculoAreaDos (baseDos, alturaDos): 
    aDos = baseDos * alturaDos
    
    return aDos 
    
    




def main (): 

    baseUno = float(input("Longitud de la base del primer rectangulo")) 

    alturaUno = float(input("Longitud de la altura del primer rectangulo")) 
    
    baseDos = float(input("Longitu de la base del segundo rectangulo")) 
    
    alturaDos = float(input("Longitud de la altura del segundo rectangulo"))
    
    perimetroUno = calculoPerimetroUno(baseUno, alturaUno)
    
    areaUno = calculoAreaUno (baseUno, alturaUno) 
    
    perimetroDos = calculoPerimetroDos (baseDos, alturaDos)
    
    areaDos = calculoAreaDos (baseDos, alturaDos)
    
    print ( "El perimetro del primero rectangulo es", "%.2f" %  perimetroUno )
    
    print ("El area del primer rectangulo es", "%.2f" % areaUno ) 
    
    print ("El perimetro del segundo rectangulo es", "%.2f" % perimetroDos)
    
    print ("El area del segundo rectangulo es", "%.2f" % areaDos) 
main() 
