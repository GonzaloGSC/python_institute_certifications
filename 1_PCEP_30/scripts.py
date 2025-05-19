import time

# 1.3. Sección 3 - Descarga e instalación de Python

print("Hisssssss...\n")

# 2.1.1 Tu primer programa

print("¡Hola, Mundo!\n")

# 2.1.13   LAB   Dando formato a la salida

# Escenario
# Te recomendamos encarecidamente que juegues con el código que hemos escrito para y realiza algunos (quizás incluso destructivos) cambios. Siéntete libre de modificar cualquier parte del código, pero hay una condición - aprende de tus errores y saca tus propias conclusiones.

# Intenta:

# minimizar el número de invocaciones de la función print() insertando \n en las cadenas;
# hacer que la flecha sea el doble de grande (pero mantener las proporciones)
# duplica la flecha, colocando ambas flechas una al lado de la otra; nota: una cadena se puede multiplicar usando el siguiente truco: "string" * 2 producirá "stringstring" (pronto contaremos más al respecto)
# elimina cualquiera de las comillas y observe detenidamente la respuesta de Python; presta atención a dónde Python ve un error - ¿es este el lugar donde realmente existe el error?
# haz lo mismo con algunos de los paréntesis;
# cambia cualquiera de las palabras print por otra cosa, que difiera solo en mayúsculas y minúsculas (por ejemplo, Print) - qué sucede ahora?
# reemplaza algunas de las comillas con apóstrofes; observa lo que sucede con cuidado.

###################
print("original version:\n")
###################
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****\n")
###################
print("solution:\n")
###################
print(
    "        *         "*2,
    "       * *        "*2,
    "      *   *       "*2,
    "     *     *      "*2,
    "    *       *     "*2, 
    "   *         *    "*2, 
    "  *           *   "*2, 
    " *             *  "*2, 
    "******     ****** "*2, 
    "     *     *      "*2, 
    "     *     *      "*2, 
    "     *     *      "*2, 
    "     *     *      "*2, 
    "     *     *      "*2, 
    "     *     *      "*2, 
    "     *******      "*2,
    sep='\n'
)

# 3.2.7   LAB   Fundamentos del bucle for – contando lentamente (mississippily)

# Escribe un bucle for que cuente hasta cinco.
    # Cuerpo del bucle: imprime el número de iteración del bucle y la palabra "Mississippi".
    # Cuerpo del bucle, emplea : time.sleep(1)

# Escribe una función print con el mensaje final.

for i in range(1, 6):
    print(f'{i} Mississippi')
    time.sleep(1)
print('Lista o no, aquí vengo!')


# 3.2.9   LAB   La sentencia break - atrapado en un bucle

while True:
    cosa = input('Ingrese palabra:')
    if isinstance(cosa, str) and cosa == 'chupacabra':
        print('Has dejado el bucle con éxito.')
        break
    
# 3.2.10   LAB   La sentencia continue – el Feo Devorador de Vocales

# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable user_word.
user_word = input('Ingrese palabra:').upper()
for letter in user_word:
    # Completa el cuerpo del bucle for.
    if letter in ['A', 'E', 'I', 'O', 'U']:
        continue
    print(letter)
    
# 3.2.11   LAB   La sentencia continue – el Lindo Devorador de Vocales

word_without_vowels = ""

# Indicar al usuario que ingrese una palabra
# y asignarla a la variable user_word.

user_word = input('Ingrese palabra:').upper()
for letter in user_word:
    # Completa el cuerpo del bucle.
    if letter in ['A', 'E', 'I', 'O', 'U']:
        continue
    word_without_vowels += letter
# Imprimir la palabra asignada a word_without_vowels.
print(word_without_vowels)

# 3.2.14   LAB   Fundamentos del bucle while

blocks = int(input("Ingresa el número de bloques: "))
height = 0
if blocks > 0:
    blocks_left = blocks
    for i in range(1, blocks):
        if i <= blocks_left:
            blocks_left -= i
            height += 1
            continue
        break
print('La altura de la pirámide: ', height)

# 3.2.15   LAB   La hipótesis de Collatz

count = 0
c0 = input('Ingrese un numero: ')
if c0.isdigit() and int(c0) > 0:
    c0 = int(c0)
    while True:
        if c0%2 == 0:
            c0 = c0 / 2
        else:
            c0 = 3 * c0 + 1
        count += 1
        print(int(c0))
        if c0 == 1:
            print('pasos =', count-1)
            break
               
# 3.6.6   LAB   Operaciones con listas: conceptos básicos

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Escribe tu código aquí.
my_list_filtered = []
for item in my_list:
    if item not in my_list_filtered:
        my_list_filtered.append(item)
#
print("La lista con elementos únicos:")
print(my_list_filtered)

# NOTAS PRUEBA MÓDULO 3

# 1%2=1 -> 1 (0001)
# 1<<1 -> 0010 (2)
# 2<<1 -> 0100 (4)
# 4<<1 -> 1000 (8)

# z = 10
# y = 0
# x = True or False

# a = 1
# b = 0
# c = 1 & 0 -> 0001 & 0000 = 0000
# d = 1 | 0 -> 0001 | 0000 = 0001
# e = 1 ^ 0 -> 0001 | 0000 = 0001
# print(c + d + e) = 2

# my_list = [1, 2, 3]
# my_list = [1, 1, 2, 3]
# my_list = [1, 1, 1, 2, 3]
# my_list = [1, 1, 1, 1, 2, 3]

# t = [[3-i for i in range (3)] for j in range (3)] :
[
    [3, 2, 1], 
    [3, 2, 1], 
    [3, 2, 1]
]
# Con i=0:
# t[i][i] =  3
# Con i=1:
# t[i][i] =  2
# Con i=2:
# t[i][i] =  1
