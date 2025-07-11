# PYTHON INSTITUTE CERTIFICATIONS

- [PYTHON INSTITUTE CERTIFICATIONS](#python-institute-certifications)
  - [LABORATORIO 1: Un Display LED](#laboratorio-1-un-display-led)
    - [Tiempo Estimado (L1)](#tiempo-estimado-l1)
    - [Nivel de dificultad (L1)](#nivel-de-dificultad-l1)
    - [Objetivos (L1)](#objetivos-l1)
    - [Escenario (L1)](#escenario-l1)
    - [Datos de prueba (L1)](#datos-de-prueba-l1)
  - [LABORATORIO 2: Pila Contadora](#laboratorio-2-pila-contadora)
    - [Tiempo Estimado (L2)](#tiempo-estimado-l2)
    - [Nivel de Dificultad (L2)](#nivel-de-dificultad-l2)
    - [Objetivos (L2)](#objetivos-l2)
    - [Escenario (L2)](#escenario-l2)
  - [LABORATORIO 3: Colas alias FIFO](#laboratorio-3-colas-alias-fifo)
    - [Tiempo Estimado (L3)](#tiempo-estimado-l3)
    - [Nivel de Dificultad (L3)](#nivel-de-dificultad-l3)
    - [Objetivos (L3)](#objetivos-l3)
    - [Escenario (L3)](#escenario-l3)
    - [Salida Esperada (L3)](#salida-esperada-l3)
  - [LABORATORIO 4: Colas alias FIFO: parte 2](#laboratorio-4-colas-alias-fifo-parte-2)
    - [Tiempo Estimado (L4)](#tiempo-estimado-l4)
    - [Nivel de Dificultad (L4)](#nivel-de-dificultad-l4)
    - [Objetivos (L4)](#objetivos-l4)
    - [Escenario (L4)](#escenario-l4)
    - [Saluda Esperada (L4)](#saluda-esperada-l4)
  - [LABORATORIO 5: La clase Timer](#laboratorio-5-la-clase-timer)
    - [Tiempo Estimado (L5)](#tiempo-estimado-l5)
    - [Nivel de Dificultad (L5)](#nivel-de-dificultad-l5)
    - [Objetivos (L5)](#objetivos-l5)
    - [Escenario (L5)](#escenario-l5)
    - [Salida Esperada (L5)](#salida-esperada-l5)
  - [LABORATORIO 6: Días de la semana](#laboratorio-6-días-de-la-semana)
    - [Tiempo Estimado (L6)](#tiempo-estimado-l6)
    - [Nivel de Dificultad (L6)](#nivel-de-dificultad-l6)
    - [Objetivos (L6)](#objetivos-l6)
    - [Escenario (L6)](#escenario-l6)
    - [Salida Esperada (L6)](#salida-esperada-l6)
  - [LABORATORIO 7: Puntos en un plano](#laboratorio-7-puntos-en-un-plano)
    - [Tiempo Estimado (L7)](#tiempo-estimado-l7)
    - [Nivel de Dificultad (L7)](#nivel-de-dificultad-l7)
    - [Objetivos (L7)](#objetivos-l7)
    - [Escenario (L7)](#escenario-l7)
    - [Salida esperada (L7)](#salida-esperada-l7)
  - [LABORATORIO 8: Triángulo](#laboratorio-8-triángulo)
    - [Tiempo Estimado (L8)](#tiempo-estimado-l8)
    - [Nivel de Dificultad (L8)](#nivel-de-dificultad-l8)
    - [Objetivos (L8)](#objetivos-l8)
    - [Escenario (L8)](#escenario-l8)
    - [Salida esperada (L8)](#salida-esperada-l8)

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

### Datos de prueba (L1)

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

### Escenario (L3)

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

## LABORATORIO 5: La clase Timer

### Tiempo Estimado (L5)

30-60 minutos

### Nivel de Dificultad (L5)

Fácil/Medio

### Objetivos (L5)

Mejorar las habilidades del estudiante para definir clases desde cero.
Definir y usar variables de instancia.
Definir y usar métodos.

### Escenario (L5)

Necesitamos una clase capaz de contar segundos. ¿Fácil? No es tan fácil como podrías pensar, ya que tendremos algunos requisitos específicos.

Léelos con atención, ya que la clase sobre la que escribes se utilizará para lanzar cohetes en misiones internacionales a Marte. Es una gran responsabilidad. ¡Contamos contigo!

Tu clase se llamará Timer (temporizador en español). Su constructor acepta tres argumentos que representan horas (un valor del rango [0..23]; usaremos tiempo militar), minutos (del rango [0. .59]) y segundos (del rango [0..59]).

Cero es el valor predeterminado para todos los parámetros anteriores. No es necesario realizar ninguna comprobación de validación.

La clase en sí debería proporcionar las siguientes facilidades:

Los objetos de la clase deben ser "imprimibles", es decir, deben poder convertirse implícitamente en cadenas de la siguiente forma: "hh:mm:ss", con ceros a la izquierda agregados cuando cualquiera de los valores es menor que 10.
La clase debe estar equipada con métodos sin parámetros llamados next_second() y previous_second (), incrementando el tiempo almacenado dentro de los objetos en +1/-1 segundos respectivamente.
Emplea las siguientes sugerencias:

Todas las propiedades del objeto deben ser privadas.
Considera escribir una función separada (¡no un método!) para formatear la cadena con el tiempo.
Completa la plantilla que te proporcionamos en el editor. Ejecuta tu código y comprueba si el resultado es el mismo que el nuestro.

### Salida Esperada (L5)

```bash
23:59:59
00:00:00
23:59:59
```

## LABORATORIO 6: Días de la semana

### Tiempo Estimado (L6)

30-60 minutos

### Nivel de Dificultad (L6)

Fácil/Medio

### Objetivos (L6)

Mejorar las habilidades del estudiante para definir clases desde cero.
Definir y usar variables de instancia.
Definir y usar métodos.

### Escenario (L6)

Tu tarea es implementar una clase llamada Weeker. Sí, tus ojos no te engañan, este nombre proviene del hecho de que los objetos de esta clase podrán almacenar y manipular los días de la semana.

El constructor de la clase acepta un argumento: una cadena. La cadena representa el nombre del día de la semana y los únicos valores aceptables deben provenir del siguiente conjunto:

Lun Mar Mie Jue Vie Sab Dom

Invocar al constructor con un argumento desde fuera de este conjunto debería generar la excepción WeekDayError (defínela tu mismo; no te preocupes, pronto hablaremos sobre la naturaleza objetiva de las excepciones). La clase debe proporcionar las siguientes facilidades:

Los objetos de la clase deben ser "imprimibles", es decir, deben poder convertirse implícitamente en cadenas de la misma forma que los argumentos del constructor.
La clase debe estar equipada con métodos de un parámetro llamados add_days(n) y subtract_days(n), siendo n un número entero que actualiza el día de la semana almacenado dentro del objeto mediante el número de días indicado, hacia adelante o hacia atrás.
Todas las propiedades del objeto deben ser privadas.
Completa la plantilla que te proporcionamos en el editor, ejecuta su código y verifica si tu salida se ve igual que la nuestra.

### Salida Esperada (L6)

```bash
Lun
Mar
Dom
Lo siento, no puedo atender tu solicitud.
```

## LABORATORIO 7: Puntos en un plano

### Tiempo Estimado (L7)

30-60 minutos

### Nivel de Dificultad (L7)

Fácil/Medio

### Objetivos (L7)

Mejorar las habilidades del estudiante para definir clases desde cero.
Definir y usar variables de instancia.
Definir y usar métodos.

### Escenario (L7)

Visitemos un lugar muy especial: un plano con el sistema de coordenadas cartesianas (puedes obtener más información sobre este concepto [aquí](https://en.wikipedia.org/wiki/Cartesian_coordinate_system).

Cada punto ubicado en el plano puede describirse como un par de coordenadas habitualmente llamadas x y y. Queremos que escribas una clase en Python que almacene ambas coordenadas como números flotantes. Además, queremos que los objetos de esta clase evalúen las distancias entre cualquiera de los dos puntos situados en el plano.

La tarea es bastante fácil si empleas la función denominada hypot() (disponible a través del módulo math) que evalúa la longitud de la hipotenusa de un triángulo rectángulo más detalles [aquí](https://en.wikipedia.org/wiki/Hypotenuse) y [aquí](https://docs.python.org/3.7/library/math.html#trigonometric-functions).

Así es como imaginamos la clase:

- Se llama Point.
- Su constructor acepta dos argumentos (x y y respectivamente), ambos por defecto se igualan a cero.
- Todas las propiedades deben ser privadas.
- La clase contiene dos métodos sin parámetros llamados getx() y gety(), que devuelven cada una de las dos coordenadas (las coordenadas se almacenan de forma privada, por lo que no se puede acceder a ellas directamente desde el objeto).
- La clase proporciona un método llamado distance_from_xy(x,y), que calcula y devuelve la distancia entre el punto almacenado dentro del objeto y el otro punto dado en un par de números flotantes.
- La clase proporciona un método llamado distance_from_point(point), que calcula la distancia (como el método anterior), pero la ubicación del otro punto se da como otro objeto de clase Point.

Completa la plantilla que te proporcionamos en el editor, ejecuta tu código y verifica si tu salida se ve igual que la nuestra.

### Salida esperada (L7)

```bash
1.4142135623730951
1.4142135623730951
```

## LABORATORIO 8: Triángulo

### Tiempo Estimado (L8)

30-60 minutos

### Nivel de Dificultad (L8)

Fácil/Medio

### Objetivos (L8)

Mejorar las habilidades del estudiante para definir clases desde cero.
Emplear composición.

### Escenario (L8)

Ahora vamos a colocar la clase Point (ver Lab 3.4.1.14) dentro de otra clase. Además, vamos a poner tres puntos en una clase, lo que nos permitirá definir un triángulo.¿Cómo podemos hacerlo?

La nueva clase se llamará Triangle y esto es lo que queremos:

- El constructor acepta tres argumentos - todos ellos son objetos de la clase Point.
- Los puntos se almacenan dentro del objeto como una lista privada.
- La clase proporciona un método sin parámetros llamado perimeter(), que calcula el perímetro del triángulo descrito por los tres puntos; el perímetro es la suma de todas las longitudes de los lados (lo mencionamos para que conste, aunque estamos seguros de que tú mismo lo conoces perfectamente).
- Completa la plantilla que te proporcionamos en el editor, ejecuta tu código y verifica si tu salida se ve igual que la nuestra.

### Salida esperada (L8)

```bash
3.414213562373095
```
