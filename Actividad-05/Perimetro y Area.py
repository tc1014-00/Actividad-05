#encoding:UTF-8
#Autor:Hector Manuel Takami Flores
#Calcula el Perimetro y Area
from Graphics import*

def calculaArea(r1b,r1h,r2b,r2h):
    A1=r1b*r1h
    A2=r2b*r2h
    if A1>A2:
        a=print("El primer rectangulo tiene mayor Area")
        a=print("Rectangulo1(Area)=",A1,"m2")
        a=print("Rectangulo2(Area)=",A2,"m2")   
    elif A2>A1:
        a=print("El segundo rectangulo tiene mayor Area")
        a=print("Rectangulo1(Area)=",A1,"m2")
        a=print("Rectangulo2(Area)=",A2,"m2")  
    elif A1==A2:
        a=print("Ambos tienen la misma Area")
        a=print("Rectangulo1(Area)=",A1,"m2")
        a=print("Rectangulo2(Area)=",A2,"m2") 
    else:
        a=print("")
        
    return a 
    
def calculaPerimetro(r1b,r1h,r2b,r2h):
    P1= ((r1b*2)+(r1h*2))
    P2= ((r2b*2)+(r2h*2))
    return P1,P2
    
def dibujar(r1b,r1h,r2b,r2h):
    win = Window("Rectangulos", 500, 500)
    r1 = Rectangle((r1b, r1h), (10, 10))
    r1.fill = Color("red")
    r1.draw(win)
    

    r2 = Rectangle((r2b, r2h), (300,10))
    r2.fill = Color("blue")
    r2.draw(win)
 #Probar con valores de 100 para arriba
    
    
def main():    
    print("Ingrese las medidas del primer rectangulo(mtrs)") 
    r1b=int(input("Base"))
    r1h=int(input("Altura"))
    print("Ingrese las medidas del segundo rectangulo(mtrs)")
    r2b=int(input("Base"))
    r2h=int(input("Altura"))
    
    a=calculaArea(r1b,r1h,r2b,r2h)
    print (a)
    b=calculaPerimetro(r1b,r1h,r2b,r2h)
    print("Perimetro Rectangulo 1 y Perimetro Rectangulo 2",b)
    
     
    dibujar(r1b,r1h,r2b,r2h)
    
main()