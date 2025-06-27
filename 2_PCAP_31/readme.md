# PYTHON INSTITUTE CERTIFICATIONS

- [PYTHON INSTITUTE CERTIFICATIONS](#python-institute-certifications)
  - [LABORATORIO 1: Un Display LED](#laboratorio-1-un-display-led)

## LABORATORIO 1: Un Display LED

### Tiempo Estimado (L1)

30 minutos

### Nivel de dificultad (L1)

Medio

### Objetivos (L1)

Mejorar las habilidades del alumno al trabajar con cadenas.
Usar cadenas para representar datos que no son texto.

### Escenario (L1)

Seguramente has visto un display de siete segmentos.

Es un dispositivo (a veces electrónico, a veces mecánico) diseñado para presentar un dígito decimal utilizando un subconjunto de siete segmentos. Si aún no sabes lo qué es, consulta la siguiente liga en Wikipedia: <https://en.wikipedia.org/wiki/Seven-segment_display>.

Tu tarea es escribir un programa que puede simular el funcionamiento de un display de siete segmentos, aunque vas a usar LEDs individuales en lugar de segmentos.

Cada dígito es construido con 13 LEDs (algunos iluminados, otros apagados, por supuesto), así es como lo imaginamos:

```txt
# ### ### # # ### ### ### ### ### ### 
#   #   # # # #   #     # # # # # # # 
# ### ### ### ### ###   # ### ### # # 
# #     #   #   # # #   # # #   # # # 
# ### ###   # ### ###   # ### ### ###
```

**Nota:** el número 8 muestra todas las luces LED encendidas.

Tu código debe mostrar cualquier número entero no negativo ingresado por el usuario.

Consejo: puede ser muy útil usar una lista que contenga patrones de los diez dígitos.

### Datos de prueba

Entrada de muestra:

123

Salida de muestra:

```xt
# ### ### 
#   #   # 
# ### ### 
# #     # 
# ### ### 
```

Entrada de muestra:

9081726354

Salida de muestra:

```txt
### ### ###   # ### ### ### ### ### # # 
# # # # # #   #   #   # #     # #   # # 
### # # ###   #   # ### ### ### ### ### 
  # # # # #   #   # #   # #   #   #   # 
### ### ###   #   # ### ### ### ###   # 
```

## LABORATORIO 2: Pila Contadora

### Tiempo Estimado (L2)

20-45 minutos

### Nivel de Dificultad (L2)

Fácil/Medio

### Objetivos (L2)

Mejorar las habilidades del estudiante para definir clases.
Emplear clases existentes para crear nuevas clases equipadas con nuevas funcionalidades.

### Escenario (L2)

Recientemente te mostramos cómo extender las posibilidades de Stack definiendo una nueva clase (es decir, una subclase) que retiene todos los rasgos heredados y agrega algunos nuevos.

Tu tarea es extender el comportamiento de la clase Stack de tal manera que la clase pueda contar todos los elementos que son agregados (push) y quitados (pop). Emplea la clase Stack que proporcionamos en el editor.

Sigue las sugerencias:

Introduce una propiedad diseñada para contar las operaciones pop y nombrarla de una manera que garantice que esté oculta.
Inicializala a cero dentro del constructor.
Proporciona un método que devuelva el valor asignado actualmente al contador (nómbralo get_counter()).
Completa el código en el editor. Ejecútalo para comprobar si tu código da como salida 100.

## LABORATORIO 3: Colas alias FIFO

### Tiempo Estimado (L3)

20-45 minutos

### Nivel de Dificultad (L3)

Fácil/Medio

### Objetivos (L3)

Mejorar las habilidades del estudiante para definir clases desde cero.
Implementar estructuras de datos estándar como clases.
Escenario (L3)
Como ya sabes, una pila es una estructura de datos que realiza el modelo LIFO (último en entrar, primero en salir). Es fácil y ya te has acostumbrado a ello perfectamente.

Probemos algo nuevo ahora. Una cola (queue) es un modelo de datos caracterizado por el término FIFO: primero en entrar, primero en salir. Nota: una cola (fila) regular que conozcas de las tiendas u oficinas de correos funciona exactamente de la misma manera: un cliente que llegó primero también es el primero en ser atendido.

Tu tarea es implementar la clase Queue con dos operaciones básicas:

put(elemento), que coloca un elemento al final de la cola.
get(), que toma un elemento del principio de la cola y lo devuelve como resultado (la cola no puede estar vacía para realizarlo correctamente).
Sigue las sugerencias:

Emplea una lista como tu almacenamiento (como lo hicimos con la pila).
put() debe agregar elementos al principio de la lista, mientras que get() debe eliminar los elementos del final de la lista.
Define una nueva excepción llamada QueueError (elige una excepción de la cual se derivará) y generala cuando get() intentes operar en una lista vacía.
Completa el código que te proporcionamos en el editor. Ejecútalo para comprobar si tu salida es similar a la nuestra.

### Salida Esperada (L3)

```bash
1
perro
False
Error de Cola
```

## LABORATORIO 4: Colas alias FIFO: parte 2

### Tiempo Estimado (L4)

15-30 minutos

### Nivel de Dificultad (L4)

Fácil/Medio

### Objetivos (L4)

Mejorar las habilidades del estudiante para definir subclases.
Agregar nueva funcionalidad a una clase existente.

### Escenario (L4)

Tu tarea es extender ligeramente las capacidades de la clase Queue. Queremos que tenga un método sin parámetros que devuelva True si la cola está vacía y False de lo contrario.

Completa el código que te proporcionamos en el editor. Ejecútalo para comprobar si genera un resultado similar al nuestro.

A continuación, puedes copiar el código que usamos en el laboratorio anterior:

### Saluda Esperada (L4)

```bash
1
perro
False
Cola vacía
```
