# Lección 3: Condicionales if, elif, else

En esta lección usamos comparaciones y operadores lógicos para tomar decisiones con `if`, `elif` y `else`.

---


## 1. Introducción

**Pregunta gancho**  
¿Cómo hace un programa para decidir si un usuario puede pasar, si aprobó una prueba o qué mensaje mostrar según su edad?

La respuesta está en las **estructuras condicionales**: bloques `if`, `elif`, `else` que permiten ejecutar código solo cuando se cumple una condición booleana.

**Objetivos de la lección**
- Entender la estructura básica de `if` y `if/else`.
- Encadenar varias condiciones con `elif`.
- Combinar comparaciones y operadores lógicos dentro de un `if`.

---

## 2. if simple

Un `if` ejecuta un bloque de código **solo si** la condición es `True`. Si es `False`, se salta ese bloque.

Sintaxis:

```python
edad = 20

if edad >= 18:
    print("Eres mayor de edad.")
```

Si edad es 20, se imprime el mensaje. Si edad fuera 15, no se imprimiría nada.



## 3. if / else
else permite ejecutar un bloque alternativo cuando la condición del if es False.

```python
edad = int(input("¿Cuál es tu edad? "))

if edad >= 18:
    print("Puedes entrar al evento.")
else:
    print("No puedes entrar, eres menor de edad.")
```

Si edad >= 18 es True, se ejecuta el bloque del if.

Si es False, se ejecuta el bloque del else. Solo uno de los dos bloques se ejecuta.



## 4. if / elif / else
elif significa “si no se cumplió lo anterior, prueba esta otra condición”. Permite tener varias ramas.

```python
nota = int(input("Ingresa tu nota (0 a 100): "))

if nota >= 60:
    print("Aprobado")
elif nota >= 40:
    print("En recuperación")
else:
    print("Reprobado")
```

Lógica:

Primero se evalúa nota >= 60.

Si eso es False, prueba nota >= 40.

Si también es False, ejecuta el else.

Solo una de las ramas se ejecuta.




## 5. Combinando condiciones
Dentro de un if se pueden combinar comparaciones con and, or, not.

```python
edad = int(input("¿Cuál es tu edad? "))
tiene_entrada = input("¿Tienes entrada? (s/n): ")

tiene_entrada_bool = (tiene_entrada == "s")

if edad >= 18 and tiene_entrada_bool:
    print("Puedes entrar.")
else:
    print("No puedes entrar.")
```

edad >= 18 and tiene_entrada_bool solo es True si las dos condiciones se cumplen.



## 6. Ejemplos prácticos
Veamos algunos ejemplos prácticos que nos ayudarán a comprender mejor la implementación de las condicionales.


### 6.1 Clasificar edad en rangos

```python
edad = int(input("¿Cuál es tu edad? "))

if edad < 12:
    print("Eres un niño o niña.")
elif edad < 18:
    print("Eres adolescente.")
elif edad < 65:
    print("Eres adulto.")
else:
    print("Eres adulto mayor.")
```


### 6.2 Revisitando “comparar edades” (versión con if)

```python
edad1 = int(input("Edad de la primera persona: "))
edad2 = int(input("Edad de la segunda persona: "))

if edad1 > edad2:
    print("La primera persona es mayor.")
elif edad2 > edad1:
    print("La segunda persona es mayor.")
else:
    print("Tienen la misma edad.")
```


## 7. Especificaciones del método lower()
.lower() es un método de strings que convierte TODAS las letras mayúsculas de un texto a minúsculas. No afecta números, símbolos ni espacios.
​

- Sintaxis:
    texto.lower()

    No recibe parámetros.
    Devuelve un nuevo string (el original no cambia).
    Solo afecta letras A-Z → a-z.


- Cuándo usarlo (situaciones reales)
Úsalo siempre cuando compares texto de usuario porque la gente escribe variado:

    Usuario escribe: "SÍ", "Si", "si", "SÍ", "sI".
    Sin lower(): necesitas 5 comparaciones.
    Con lower(): solo 1 comparación == "sí".

Casos típicos en programas reales:

    Validar "sí/no", "si/no", "SÍ/NO"
    Menús: "salir", "SALIR", "Salir"
    Nombres de usuario (case-insensitive)
    Procesar respuestas de formularios

- Ejemplo 1: Menú simple restaurante
Para tu lección 3 - justo antes del ejercicio 24:

```python
print("MENÚ RÁPIDO")
print("1. Completo italiano")
print("2. Hamburguesa")
print("3. Salir")

opcion = input("Elige opción (1/2/3): ")

if opcion.lower() == "salir" or opcion.lower() == "3":
    print("¡Gracias por visitarnos!")
else:
    print("Preparando tu pedido...")
```


- Ejemplo 2: Validación sí/no genérica
Para explicar el concepto antes de los ejercicios grandes:

```python
pregunta = input("¿Cliente frecuente? (sí/no): ")
es_frecuente = pregunta.lower() == "sí"

if es_frecuente:
    print("¡Hola cliente frecuente! 5% descuento")
else:
    print("¡Bienvenido!")
```
Guardamos la respuesta en es_frecuente como True o False. Así usamos el resultado después sin repetir lower().


- Ejemplo 3: Directo en variable

```python
es_estudiante = input("¿Estudiante? (sí/no): ").lower() == "sí"
```



## 8. Ejercicios

Las soluciones las puedes encontrar en la carpeta ejercicios


- Ejercicio 1 (fácil) – Par o impar
Pide un número entero por teclado y muestra:

"El número es par" si el resto al dividir por 2 es 0.

"El número es impar" en caso contrario.

Pista: usa el operador % y un if/else.



- Ejercicio 2 (medio) – Calculadora con operación
Pide:

Un primer número (float).

Un segundo número (float).

Una operación (+, -, *, /).

Según la operación ingresada, muestra el resultado correspondiente. Si la operación no es válida, muestra un mensaje de error.



- Ejercicio 3 (medio) – Sistema de notas
Pide una nota de 0 a 100 y muestra:

"Excelente" si la nota es mayor o igual a 90.

"Bueno" si está entre 75 y 89.

"Suficiente" si está entre 60 y 74.

"Insuficiente" si es menor a 60.

Usa if / elif / else encadenados.



- Ejercicio 4 (desafío) – Menú simple
Crea un menú de texto como este:

text
Menú:
1. Saludar
2. Mostrar mi edad en 5 años
3. Salir

Elige una opción: 
Si elige 1: pide el nombre y saluda.

Si elige 2: pide la edad y muestra la edad que tendrá en 5 años.

Si elige 3: muestra un mensaje de despedida.

Si elige otra cosa: muestra "Opción no válida".

Usa if / elif / else y input().



## 9. Resumen y siguiente paso
En esta lección viste:

- Cómo usar if para ejecutar código solo cuando una condición es verdadera.

- Cómo usar if/else para cubrir dos caminos posibles.

- Cómo encadenar varias condiciones con elif.

- Cómo combinar comparaciones y operadores lógicos en un if.

**En la próxima lección usarás bucles while y for para repetir acciones muchas veces sin copiar y pegar código.**