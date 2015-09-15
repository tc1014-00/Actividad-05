#encoding: UTF-8
#Autor: Brian Saggiante, A01377511
#Mezcla de colores

def mezclaDeColores(c1,c2):
    if c1=='amarillo':
        if c2=='rojo':
            mezcla='Naranja'
            return mezcla
        elif c2=='azul':
            mezcla='Verde'
            return mezcla
        elif c2=='amarillo':
            mezcla='Amarillo'
            return mezcla
    
    if c1=='azul':
        if c2=='rojo':
            mezcla='Morado'
            return mezcla
        elif c2=='amarillo':
            mezcla='Verde'
            return mezcla
        elif c2=='azul':
            mezcla='Azul'
            return mezcla
            
    if c1=='rojo':
        if c2=='amarillo':
            mezcla='Naranja'
            return mezcla
        elif c2=='azul':
            mezcla='Morado'
            return mezcla
        elif c2=='rojo':
            mezcla='Rojo'
            return mezcla
    
            
    if c2=='Verde'or'Naranja'or'Morado':
        mezcla='...ERROR...el_usuario_no_tecleo_amarillo_rojo_azul'
        return mezcla       
    else:
        mezcla='...ERROR...el_usuario_no_tecleo_amarillo_rojo_azul'
        return mezcla
        

def main():
    color1=input('Dame el primer color')
    color2=input('Dame el segundo color')
    color1=color1.lower()
    color2=color2.lower()
    mezcla=mezclaDeColores(color1,color2)
    print('La mezcla de los colores dan: ',mezcla)
main()