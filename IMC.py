#encoding: UTF-8
#Autor: Brian Saggiante, A01377511
#IMC

def calculaIMC(e,p):
    if e<=0 or p<=0:
        IMC='...ERROR...'
        return IMC
    else:
        IMC=p/(e**2)
        return IMC
        
def rangoDePeso(IMC):
    if IMC<=0:
        rango='...ERROR...'
        return rango
    if IMC<18.5:
        rango='La persona es de bajo peso'
        return rango
    if 18.5<=IMC<=25:
        rango='La persona tiene un peso normal'
        return rango
    if IMC>25:
        rango='La persona tiene sobrepeso'
        return rango




def main():
    peso=float(input('Escribe el peso de la persona en kg'))
    estatura=float(input('Escribe la estatura de la persona en m'))
    IMC=calculaIMC(peso,estatura)
    rango=rangoDePeso(IMC)
    print('El indice de masa corporal de la persona es: ',IMC)
    print('El rango en el que se encuentra la persona: ',rango)
main()