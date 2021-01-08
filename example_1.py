billete_grosor = 0.11 * 0.001  # metros (0.11 mm)
sears_altura = 442  # Altura en metros
num_billetes = 1
dia = 1

while num_billetes * billete_grosor < sears_altura:
    print(dia, num_billetes, num_billetes * billete_grosor)
    dia = dia + 1
    num_billetes = num_billetes * 2

print('Número de días', dia)
print('Número de billetes', num_billetes)
print('Altura final', num_billetes * billete_grosor)

#La nueva línea adicional se puede suprimir
print('Hola ', end='')
print('Mi nombre es', 'Jake')

#input
nombre = input('Ingrese su nombre: ')
print('Tu nombre es', nombre)

#pass
a = 1
b = 2
if a > b:
    pass
else:
    print('Computer says false')
