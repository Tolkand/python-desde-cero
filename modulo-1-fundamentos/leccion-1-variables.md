# Lección 1: Variables y Tipos de Datos

En esta lección creo mis primeras variables en Python y pruebo distintos tipos de datos básicos.

---

## 1. Introducción

**Pregunta gancho:**  
¿Cómo hace un programa para “recordar” datos como tu nombre, tu edad o un puntaje?

**Qué aprenderás en esta lección:**
- Qué es una variable.
- Qué tipos de datos básicos existen en Python.
- Cómo mostrar esos valores por pantalla.

**Por qué importa:**  
Casi todo programa guarda y usa información. Las variables son la base de todo lo que vendrá después.

Conexión con la siguiente lección: en la próxima clase usarás estas variables para hacer **operaciones** con operadores aritméticos y lógicos.

---

## 2. Conceptos básicos

### 2.1 ¿Qué es una variable?

Una **variable** es un nombre que apunta a un valor en memoria.  
En la práctica, puedes pensarla como una **caja etiquetada** donde guardas algo.

Sintaxis:

## python
nombre_variable = valor
Ejemplo:

## python
nombre = "Ana"
edad = 28
2.2 Tipos de datos básicos
Python trae varios tipos de datos integrados. En esta lección veremos 4:

int: números enteros (sin decimales).

float: números decimales.

str: texto (cadenas de caracteres).

bool: valores lógicos, True o False.

## Ejemplo:

python
entero = 10          # int
decimal = 3.14       # float
texto = "Python"     # str
es_programador = True  # bool
Para saber qué tipo tiene una variable:

python
print(type(entero))        # <class 'int'>
print(type(decimal))       # <class 'float'>
print(type(texto))         # <class 'str'>
print(type(es_programador))# <class 'bool'>
3. Ejemplos prácticos
3.1 Ejemplo básico
python
nombre = "Ana"
edad = 28

print("Nombre:", nombre)
print("Edad:", edad)
Salida esperada:

text
Nombre: Ana
Edad: 28
3.2 Conversión de tipos (casting)
Muchas veces necesitas convertir datos. Por ejemplo, de número a texto o de texto a número.

python
numero = 42
numero_texto = str(numero)   # "42"

texto = "100"
texto_numero = int(texto)    # 100

print(type(numero_texto))    # <class 'str'>
print(texto_numero + 50)     # 150
3.3 Error común
python

# Esto genera error:
# resultado = "10" + 5

# Forma correcta:
resultado = int("10") + 5
print(resultado)  # 15