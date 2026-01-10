
# Lección 1: Variables y Tipos de Datos

En esta lección creamos nuestras primeras variables en Python y probamos tipos de datos básicos.

---

## 1. Introducción

**Pregunta gancho**  
¿Cómo hace un programa para “recordar” tu nombre, tu edad o un puntaje de juego?.

La respuesta corta es: usando **variables**. Una variable es un espacio en la memoria con un nombre, donde el programa puede guardar y recuperar información cuando la necesite.

**Objetivos de la lección**
- Entender qué es una variable.
- Conocer los tipos básicos: `int`, `float`, `str`, `bool`.
- Escribir un pequeño programa usando variables.

**Por qué es importante**  
Todas las aplicaciones que guardan información usan variables. Sin entender esto, nada de lo que viene después tiene base sólida.

---

## 2. Conceptos clave

### 2.1 ¿Qué es una variable?

Una **variable** es un nombre que apunta a un valor en memoria.  
La puedes imaginar como una **caja con etiqueta** donde guardas algo.

Sintaxis básica:

```python
nombre_variable = valor
```

Ejemplo:

```python
nombre = "Ana"
edad = 28
```

### 2.2 Tipos de datos básicos

En Python usaremos, por ahora, estos tipos:

     int: números enteros (10, -3, 2026)

     float: números con decimales (3.14, 1.75)

     str: texto entre comillas ("Hola", 'Python')

     bool: verdadero o falso (True, False)

Ejemplo:

```python
entero = 10
decimal = 3.14
texto = "Python"
es_programador = True
```

Para ver el tipo:

```python
print(type(entero))          # <class 'int'>
print(type(decimal))         # <class 'float'>
print(type(texto))           # <class 'str'>
print(type(es_programador))  # <class 'bool'>
```

---

## 3. Ejemplos prácticos

El código completo de estos ejemplos está en
modulo-1-fundamentos/ejemplos/ejemplos_semana_1.py

### 3.1 Ejemplo básico de variables

```python
nombre = "Ana"
edad = 28

print("Nombre:", nombre)
print("Edad:", edad)
```

Salida:

     Nombre: Ana

     Edad: 28


### 3.2 Conversión de tipos (casting)

```python
numero = 42
numero_texto = str(numero)   # "42"

texto = "100"
texto_numero = int(texto)    # 100

print(type(numero_texto))    # <class 'str'>
print(texto_numero + 50)     # 150
```


### 3.3 Error común

Esto produce error:

     resultado = "10" + 5

Forma correcta:

     resultado = int("10") + 5

     print(resultado)  # 15



### 3.4 Un primer vistazo a `input()` (adelanto)

A veces queremos que el usuario escriba datos por teclado. Para eso usaremos la función `input()`.  
La veremos con más detalle en la Lección 2, pero aquí va un primer ejemplo simple:

```python
nombre = input("¿Cómo te llamas? ")
print("Hola", nombre)
```



---

## 4. Ejercicios
Puedes escribir y probar estos ejercicios en
modulo-1-fundamentos/ejercicios/ejercicios_leccion_1.py

 

 
Ejercicio 1 (fácil)

Crea variables para:

     Tu nombre (str)

     Tu edad (int)

     Tu altura en metros (float)

     Si te gusta programar (bool)

Muestra cada variable junto con su tipo usando type().

 


Ejercicio 2 (medio)

     Tienes este código:

```python
    numero = "25"
```

     Convierte 'numero' a int y súmale 10.

     Completa el programa para que imprima 35.




Ejercicio 3 (desafío)

     Escribe un programa que:

     Pida tu nombre por teclado.

     Pida tu edad por teclado.

     Calcule en qué año naciste (puedes suponer que estamos en 2026).

     Muestre un mensaje como:

       Hola Ana, probablemente naciste en 1998.

---

## 5. Resumen y siguiente paso

En esta lección viste:

     Qué es una variable y cómo declararla.

     Cuatro tipos básicos: int, float, str, bool.

     Cómo usar type() y cómo convertir entre tipos.


**En la próxima lección aprenderás a usar operadores aritméticos y de comparación para hacer cálculos y tomar decisiones simples.**


