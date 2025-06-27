# Certificación PCEP™ – Certified Entry-Level Python Programmer (examen PCEP-30-0x)

- [Certificación PCEP™ – Certified Entry-Level Python Programmer (examen PCEP-30-0x)](#certificación-pcep--certified-entry-level-python-programmer-examen-pcep-30-0x)
  - [Historia](#historia)
  - [Sobre errores](#sobre-errores)
    - [1. SyntaxError](#1-syntaxerror)
    - [2. IndentationError](#2-indentationerror)
    - [3. NameError](#3-nameerror)
    - [4. TypeError](#4-typeerror)
    - [5. IndexError](#5-indexerror)
    - [6. KeyError](#6-keyerror)
    - [7. ValueError](#7-valueerror)
    - [8. AttributeError](#8-attributeerror)
    - [9. ImportError](#9-importerror)
    - [10. ZeroDivisionError](#10-zerodivisionerror)
  - [Sobre print](#sobre-print)
    - [1. Imprimir una cadena de texto](#1-imprimir-una-cadena-de-texto)
    - [2. Imprimir múltiples valores](#2-imprimir-múltiples-valores)
    - [3. Uso del parámetro `sep`](#3-uso-del-parámetro-sep)
    - [4. Uso del parámetro `end`](#4-uso-del-parámetro-end)
    - [5. Imprimir valores formateados](#5-imprimir-valores-formateados)
    - [6. Uso de `str.format()`](#6-uso-de-strformat)
    - [7. Imprimir listas y diccionarios](#7-imprimir-listas-y-diccionarios)
    - [8. Imprimir con saltos de línea](#8-imprimir-con-saltos-de-línea)
    - [9. Imprimir sin espacio adicional](#9-imprimir-sin-espacio-adicional)
    - [10. Redirigir la salida a un archivo](#10-redirigir-la-salida-a-un-archivo)
    - [11. Imprimir caracteres especiales](#11-imprimir-caracteres-especiales)
  - [Resumen reglas de operadores](#resumen-reglas-de-operadores)

## Historia

Python fue creado por **Guido van Rossum**, nacido en 1956 en Haarlem, Países Bajos.

La **PSF (Python Software Foundation)**, una comunidad que tiene como objetivo desarrollar, mejorar, expandir y popularizar Python y su entorno. El presidente del PSF es el mismo Guido von Rossum, y por eso, estos pythons se llaman canónicos. También se consideran Pythons de referencia, ya que cualquier otra implementación del lenguaje debe seguir todos los estándares establecidos por la PSF.

Guido van Rossum usó el lenguaje de programación "C" para implementar la primera versión de su lenguaje y esta decisión aún está vigente. Todos los Pythons que provienen del PSF están escritos en el lenguaje "C". Hay muchas razones para este enfoque. Uno de ellos (probablemente el más importante) es que gracias a él, Python puede ser portado y migrado fácilmente a todas las plataformas con la capacidad de compilar y ejecutar programas en lenguaje "C" (prácticamente todas las plataformas tienen esta función, lo que abre muchas posibilidades de expansión).

Esta es la razón por la cual la implementación de PSF a menudo se denomina CPython. Este es el Python más influyente entre todos los Pythons del mundo.

## Sobre errores

1. El traceback (que es la ruta que recorre el código a través de diferentes partes del programa; puedes ignorarlo por ahora, ya que está vacío en un código tan simple) ;
2. La ubicación del error (el nombre del archivo que contiene el error, el número de línea y el nombre del módulo); nota: el número puede ser engañoso, ya que Python suele mostrar el lugar donde notó por primera vez los efectos del error, no necesariamente el error en sí;
3. El contenido de la línea errónea; nota: la ventana del editor de IDLE no muestra números de línea, pero muestra la ubicación actual del cursor en la esquina inferior derecha; utilízalo para localizar la línea errónea en un código fuente largo;
4. El nombre del error y una breve explicación.

Resumen de los errores más comunes en Python, junto con ejemplos y explicaciones sobre cómo ocurren y cómo pueden solucionarse:

### 1. SyntaxError

Ocurre cuando el intérprete de Python encuentra un error de sintaxis en el código.

**Ejemplo:**

```python
print("Hola mundo"
```

**Solución:**
Asegúrate de que todas las estructuras de control, funciones y bloques de código están correctamente cerrados.

```python
print("Hola mundo")
```

### 2. IndentationError

Se produce cuando la indentación del código no es consistente.

**Ejemplo:**

```python
if True:
print("Hola mundo")
```

**Solución:**
Asegúrate de que la indentación sea consistente (generalmente cuatro espacios o un tabulador).

```python
if True:
    print("Hola mundo")
```

### 3. NameError

Se lanza cuando una variable o función no ha sido definida.

**Ejemplo:**

```python
print(valor)
```

**Solución:**
Define la variable o asegúrate de que esté correctamente escrita.

```python
valor = 10
print(valor)
```

### 4. TypeError

Ocurre cuando una operación o función es aplicada a un objeto de un tipo inapropiado.

**Ejemplo:**

```python
print(5 + "5")
```

**Solución:**
Asegúrate de que los tipos de los operandos sean compatibles.

```python
print(5 + int("5"))
# o
print(str(5) + "5")
```

### 5. IndexError

Se produce cuando intentas acceder a un índice que está fuera del rango de una lista o tupla.

**Ejemplo:**

```python
lista = [1, 2, 3]
print(lista[3])
```

**Solución:**
Asegúrate de que el índice está dentro del rango de la lista o tupla.

```python
lista = [1, 2, 3]
if len(lista) > 3:
    print(lista[3])
else:
    print("Índice fuera de rango")
```

### 6. KeyError

Se lanza cuando intentas acceder a una clave que no existe en un diccionario.

**Ejemplo:**

```python
diccionario = {"a": 1, "b": 2}
print(diccionario["c"])
```

**Solución:**
Verifica que la clave existe en el diccionario antes de acceder a ella.

```python
diccionario = {"a": 1, "b": 2}
print(diccionario.get("c", "Clave no encontrada"))
```

### 7. ValueError

Se produce cuando una función recibe un argumento de tipo correcto pero con un valor inapropiado.

**Ejemplo:**

```python
int("abc")
```

**Solución:**
Asegúrate de que el valor proporcionado a la función sea apropiado.

```python
try:
    print(int("abc"))
except ValueError:
    print("Valor inválido para la conversión a entero")
```

### 8. AttributeError

Ocurre cuando intentas acceder a un atributo que no existe para un objeto.

**Ejemplo:**

```python
cadena = "hola"
cadena.append("mundo")
```

**Solución:**
Verifica que el objeto tiene el atributo o método que intentas utilizar.

```python
cadena = "hola"
cadena = cadena + " mundo"
print(cadena)
```

### 9. ImportError

Se lanza cuando un módulo no puede ser importado.

**Ejemplo:**

```python
import modulo_inexistente
```

**Solución:**
Asegúrate de que el módulo existe y está disponible en tu entorno.

```python
# Instalar el módulo si es necesario
# pip install modulo_existente

import modulo_existente
```

### 10. ZeroDivisionError

Ocurre cuando intentas dividir por cero.

**Ejemplo:**

```python
resultado = 10 / 0
```

**Solución:**
Verifica que el denominador no sea cero antes de realizar la división.

```python
denominador = 0
if denominador != 0:
    resultado = 10 / denominador
else:
    print("División por cero no permitida")
```

Estos son algunos de los errores más comunes en Python. Identificar y entender estos errores te ayudará a escribir y depurar tu código de manera más eficiente.

## Sobre print

Ejemplos comunes de la función `print` en Python y sus características:

### 1. Imprimir una cadena de texto

La forma más básica de `print` es imprimir una cadena de texto.

**Ejemplo:**

```python
print("Hola, mundo!")
```

**Salida:**

```text
Hola, mundo!
```

### 2. Imprimir múltiples valores

Puedes imprimir múltiples valores separándolos con comas.

**Ejemplo:**

```python
print("El valor es:", 42)
```

**Salida:**

```text
El valor es: 42
```

### 3. Uso del parámetro `sep`

El parámetro `sep` define el separador entre los valores.

**Ejemplo:**

```python
print("Hola", "mundo", sep="-")
```

**Salida:**

```text
Hola-mundo
```

### 4. Uso del parámetro `end`

El parámetro `end` define lo que se imprimirá al final. Por defecto, es una nueva línea (`\n`).

**Ejemplo:**

```python
print("Hola", end=" ")
print("mundo")
```

**Salida:**

```text
Hola mundo
```

### 5. Imprimir valores formateados

Usando f-strings (disponible en Python 3.6+), puedes formatear cadenas de manera más legible.

**Ejemplo:**

```python
nombre = "Alice"
edad = 30
print(f"Nombre: {nombre}, Edad: {edad}")
```

**Salida:**

```text
Nombre: Alice, Edad: 30
```

### 6. Uso de `str.format()`

Otra forma de formatear cadenas es usando el método `str.format()`.

**Ejemplo:**

```python
nombre = "Bob"
edad = 25
print("Nombre: {}, Edad: {}".format(nombre, edad))
```

**Salida:**

```text
Nombre: Bob, Edad: 25
```

### 7. Imprimir listas y diccionarios

Puedes imprimir estructuras de datos como listas y diccionarios directamente.

**Ejemplo:**

```python
lista = [1, 2, 3]
diccionario = {"nombre": "Carlos", "edad": 28}
print(lista)
print(diccionario)
```

**Salida:**

```text
[1, 2, 3]
{'nombre': 'Carlos', 'edad': 28}
```

### 8. Imprimir con saltos de línea

Puedes incluir saltos de línea (`\n`) dentro de cadenas para imprimir en varias líneas.

**Ejemplo:**

```python
print("Línea 1\nLínea 2\nLínea 3")
```

**Salida:**

```text
Línea 1
Línea 2
Línea 3
```

### 9. Imprimir sin espacio adicional

Cuando imprimes múltiples valores, `print` agrega un espacio por defecto entre ellos. Puedes cambiar esto usando `sep=""`.

**Ejemplo:**

```python
print("123", "456", sep="")
```

**Salida:**

```text
123456
```

### 10. Redirigir la salida a un archivo

Puedes redirigir la salida de `print` a un archivo usando el parámetro `file`.

**Ejemplo:**

```python
with open("salida.txt", "w") as archivo:
    print("Hola, archivo!", file=archivo)
```

Este código creará un archivo llamado `salida.txt` con el contenido `Hola, archivo!`.

### 11. Imprimir caracteres especiales

Puedes imprimir caracteres especiales usando secuencias de escape.

**Ejemplo:**

```python
print("Una comilla simple: \', una comilla doble: \", y una barra invertida: \\")
```

**Salida:**

```text
Una comilla simple: ', una comilla doble: ", y una barra invertida: \
```

Estos son algunos de los usos más comunes de la función `print` en Python. Cada uno demuestra diferentes características y capacidades de la función para diversas necesidades de impresión y formateo de texto.

## Resumen reglas de operadores

1. Una expresión es una combinación de valores (o variables, operadores, llamadas a funciones, aprenderás de ello pronto) las cuales son evaluadas y dan como resultado un valor, por ejemplo, 1 + 2.

2. Los operadores son símbolos especiales o palabras clave que son capaces de operar en los valores y realizar operaciones matemáticas, por ejemplo, el *multiplica dos valores: x* y.

3. Los operadores aritméticos en Python: + (suma), - (resta), *(multiplicación), / (división clásica: regresa un flotante siempre), % (módulo: divide el operando izquierdo entre el operando derecho y regresa el residuo de la operación, por ejemplo, 5 % 2 = 1), **(exponenciación: el operando izquierdo se eleva a la potencia del operando derecho, por ejemplo, 2** 3 = 2* 2 * 2 = 8), // (división entera: retorna el número resultado de la división, pero redondeado al número entero inferior más cercano, por ejemplo, 3 // 2.0 = 1.0)

4. Un operador unario es un operador con solo un operando, por ejemplo, -1, o +3.

5. Un operador binario es un operador con dos operandos, por ejemplo, 4 + 5, o 12 % 5.

6. Algunos operadores actúan antes que otros, a esto se le llama - jerarquía de prioridades:

   - El operador ** (exponencial) tiene la prioridad más alta;
   - Posteriormente los operadores unarios + y - (nota: los operadores unarios a la derecha del operador exponencial enlazan con mayor fuerza, por ejemplo 4 ** -1 es igual a 0.25)
   - Después *, /, //, y %,
   Finalmente, la prioridad más baja: los operadores binarios + y -.
7. Las sub-expresiones dentro de paréntesis siempre se calculan primero, por ejemplo,  15 - 1 *( 5*( 1 + 2 ) ) = 0.

8. Los operadores de exponenciación utilizan enlazado del lado derecho, por ejemplo, 2 **2** 3 = 256.
