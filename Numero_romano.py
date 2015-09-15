#encoding: UTF-8
#Autor: Brian Saggiante, A01377511
#Numeros Romanos

def cambioNumero(numero):
    if (numero<=3 and numero>=1):
        romano=numero*'I'
    elif(numero==4):
        romano='IV'
    elif(numero==5):
        romano='V'
    elif(numero>=6 and numero<=8):
        romano='VI'+'I'*(numero%3)
    elif(numero==9):
        romano='IX'
    elif(numero==10):
        romano='X'
    else:
        romano='error'
    return romano





def main():
    numero=int(input('El numero que se cambiara es: '))
    nRomano=cambioNumero(numero)
    print('El numero %i que se convierte a numero romano es'%numero,nRomano)
main()