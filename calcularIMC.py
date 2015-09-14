#encoding: UTF-8
# Jorge Daniel Juarez Ruiz
# Calcular el IMC

def calcularIMC(e,m):
    if e<=0 or m<0:
        imc="ERROR"
        return imc
    else:
        imc=m/(e**2)
        return imc

def describirEstado(imc):
    est=""
    if imc=="ERROR":
        est="ERROR"
        return est
    if imc <18.5:
        est="Bajo peso"
        return est
    if 18.5<=imc<=25:
        est="Peso normal"
        return est
    if imc>25:
        est="Sobrepeso"
        return est
    
    

def main():
    estatura=float(input("Estatura en m"))
    masa=float(input("masa en kg"))
    imc=calcularIMC(estatura,masa)
    estado=describirEstado(imc)
    print(imc)
    print (estado)
    
main()