# Guía Práctica de Implementación - Semana por Semana

## Fase 0: Preparación Previa (Primeros Pasos - 2-3 horas)

### 1. Configura tu Entorno

**Instalación de Python:**
```bash
# En Windows: descarga desde python.org
# En Linux/Mac:
python3 --version  # Verificar si está instalado
```

**Instala VS Code:**
1. Ve a https://code.visualstudio.com
2. Descarga para tu sistema operativo
3. Instala

**En VS Code, instala extensiones:**
1. Click en icono de extensiones (izquierda)
2. Busca "Python" (Microsoft)
3. Click en instalar

### 2. Crea tu Repositorio en GitHub

```bash
# 1. Crea carpeta de proyecto
mkdir python-desde-cero
cd python-desde-cero

# 2. Inicia git
git init

# 3. Crea estructura
mkdir modulo-{1,2,3,4,5,6}/ejemplos
mkdir proyectos-integradores
touch README.md
touch .gitignore
touch PROGRESO.md

# 4. Contenido de .gitignore
echo "__pycache__/" >> .gitignore
echo "*.pyc" >> .gitignore
echo ".DS_Store" >> .gitignore
```

### 3. Tu Primer Commit

```bash
# Crear archivo inicial
echo '# Python desde Cero

Aprendiendo Python y creando tutoriales simultáneamente.

## Estructura del Curso

- Módulo 1: Fundamentos
- Módulo 2: Control de Flujo
- Módulo 3: Funciones
- Módulo 4: Estructuras de Datos
- Módulo 5: Archivos
- Módulo 6: POO' > README.md

# Hacer primer commit
git add .
git commit -m "Inicializar proyecto Python desde Cero"

# Conectar con GitHub (crea repo en GitHub primero)
git remote add origin https://github.com/TU_USUARIO/python-desde-cero.git
git branch -M main
git push -u origin main
```

---

## Semana 1: Instalación y Variables

### Lunes-Miércoles: APRENDIZAJE

**Lunes: Instalación**

Tareas:
- [ ] Descargar e instalar Python
- [ ] Verificar instalación: `python --version`
- [ ] Abrir VS Code
- [ ] Crear carpeta `modulo-1-fundamentos`
- [ ] Crear archivo `hola_mundo.py`

```python
# hola_mundo.py
print("¡Hola, mundo!")
```

En terminal:
```bash
cd modulo-1-fundamentos
python hola_mundo.py
```

Deberías ver: `¡Hola, mundo!`

Notas de aprendizaje:
```markdown
# Día 1: Mi primer programa

## Qué aprendí
- Python se instala en tu computadora
- Los archivos Python terminan en .py
- print() es una función para mostrar texto
- python archivo.py ejecuta el programa

## Confusiones
- [ninguna por ahora]

## Para la próxima
- Entender qué es una variable
```

---

**Martes: Variables Básicas**

```python
# variables.py
nombre = "Tu Nombre"
edad = 25

print(nombre)
print(edad)
print("Mi nombre es " + nombre)
print("Tengo " + str(edad) + " años")
```

Ejecutar y ver output:
```
Tu Nombre
25
Mi nombre es Tu Nombre
Tengo 25 años
```

Notas:
```markdown
# Día 2: Variables

## Qué aprendí
- Una variable es una "caja" que almacena información
- Creamos variables con: nombre = valor
- print() muestra el contenido de una variable
- str() convierte números a texto

## Preguntas
- ¿Qué otros tipos de datos existen?
- ¿Cuál es la diferencia entre "texto" y números?
```

---

**Miércoles: Tipos de Datos**

```python
# tipos_datos.py
numero = 42
decimal = 3.14
texto = "Python"
verdadero = True
falso = False

print(type(numero))    # <class 'int'>
print(type(decimal))   # <class 'float'>
print(type(texto))     # <class 'str'>
print(type(verdadero)) # <class 'bool'>

# Conversión de tipos
numero_string = str(numero)
print(type(numero_string))  # <class 'str'>

numero_convertido = int("50")
print(numero_convertido + 5)  # 55
```

Notas finales de aprendizaje esta semana:
```markdown
# Resumen Semana 1

## Conceptos clave
1. Las variables almacenan datos
2. Los tipos básicos son: int, float, str, bool
3. type() muestra el tipo de una variable
4. Podemos convertir entre tipos

## Código escrito
- hola_mundo.py
- variables.py
- tipos_datos.py

## Sentimiento
😊 Entusiasmado, entiendo lo básico
```

---

### Jueves: CONSOLIDACIÓN

**Revisar lo aprendido:**
- [ ] ¿Qué es una variable? (respuesta: un nombre que almacena un valor)
- [ ] ¿Cuáles son los 4 tipos básicos? (respuesta: int, float, str, bool)
- [ ] ¿Cómo vemos el tipo de un dato? (respuesta: con type())

**Crear ejemplos claros:**

Crear archivo `ejemplos-semana-1.py`:
```python
# ========== EJEMPLO 1: VARIABLE SIMPLE ==========
print("=== VARIABLES SIMPLES ===")
nombre = "Juan"
print(f"El nombre es: {nombre}")

# ========== EJEMPLO 2: DIFERENTES TIPOS ==========
print("\n=== DIFERENTES TIPOS ===")
edad = 25  # int
altura = 1.75  # float
es_estudiante = True  # bool
ciudad = "Santiago"  # str

print(f"Edad: {edad} (tipo: {type(edad).__name__})")
print(f"Altura: {altura} (tipo: {type(altura).__name__})")
print(f"¿Estudiante?: {es_estudiante} (tipo: {type(es_estudiante).__name__})")
print(f"Ciudad: {ciudad} (tipo: {type(ciudad).__name__})")

# ========== EJEMPLO 3: CONVERSIÓN ==========
print("\n=== CONVERSIÓN DE TIPOS ===")
numero = 42
numero_string = str(numero)
print(f"Número original: {numero} (tipo: {type(numero).__name__})")
print(f"Convertido a string: {numero_string} (tipo: {type(numero_string).__name__})")

string_numero = int("100")
print(f"String '100' convertido a int: {string_numero + 50}")
```

**Outline para tutorial:**
```markdown
# Tutorial: Variables y Tipos de Datos

## Introducción (2 min)
- ¿Qué es una variable?
- ¿Por qué es importante?
- Comparación: variable = caja que guarda algo

## Conceptos (5 min)
- Definición de variable
- Cómo crear una variable
- Los 4 tipos básicos
- type() para verificar

## Ejemplos Prácticos (8 min)
- Ejemplo 1: Variable simple
- Ejemplo 2: Diferentes tipos
- Ejemplo 3: Conversión

## Ejercicios (4 min)
- Fácil: Crear variables
- Medio: Usar conversión
- Difícil: Programa pequeño

## Resumen (2 min)
- Puntos clave
- Próximo: Operadores
```

---

### Viernes-Sábado: CREACIÓN DEL TUTORIAL

**Viernes:**

Crear archivo: `modulo-1-fundamentos/leccion-1-variables.md`

```markdown
# Lección 1: Variables y Tipos de Datos en Python

## Introducción

Imagina que eres un chef y necesitas guardar ingredientes mientras cocinas.
Una variable es exactamente eso: un contenedor que almacena información
para que puedas usarla después.

## ¿Qué es una Variable?

Una variable es un nombre que representa un valor guardado en la memoria
de tu computadora.

**Sintaxis básica:**
```python
nombre_variable = valor
```

### Ejemplo Simple

```python
nombre = "Juan"
edad = 25
```

En estos ejemplos:
- `nombre` es una variable que contiene el texto "Juan"
- `edad` es una variable que contiene el número 25

## Los 4 Tipos de Datos Básicos

### 1. Enteros (int)
Son números sin decimales. Ejemplos: 25, -5, 1000

```python
edad = 25
estudiantes = 30
temperatura = -10
```

### 2. Decimales (float)
Son números con punto decimal. Ejemplos: 3.14, 1.75, -0.5

```python
precio = 19.99
altura = 1.75
promedio = 7.5
```

### 3. Textos (str)
Son cadenas de caracteres entre comillas. Pueden ser simples o dobles.

```python
nombre = "Juan"
apellido = 'Pérez'
mensaje = "Hola, mundo!"
```

### 4. Booleanos (bool)
Son valores de verdadero o falso. Solo tienen 2 valores posibles.

```python
es_programador = True
tiene_experiencia = False
```

## Verificar el Tipo de Dato

Usa la función `type()` para saber qué tipo es un dato:

```python
edad = 25
print(type(edad))  # <class 'int'>

nombre = "Juan"
print(type(nombre))  # <class 'str'>

altura = 1.75
print(type(altura))  # <class 'float'>
```

## Conversión de Tipos

A veces necesitas cambiar un dato de un tipo a otro.

### De número a texto
```python
numero = 42
numero_como_texto = str(numero)  # Ahora es "42"
print(type(numero_como_texto))  # <class 'str'>
```

### De texto a número
```python
texto = "100"
numero = int(texto)  # Ahora es 100
print(numero + 50)  # 150
```

## Errores Comunes

### Error 1: Confundir tipos

❌ **INCORRECTO:**
```python
resultado = "10" + 5  # ¡Error! No puedes sumar texto y número
```

✅ **CORRECTO:**
```python
resultado = int("10") + 5  # Convertir primero
print(resultado)  # 15
```

## Resumen

- Una variable almacena un valor con un nombre
- Los 4 tipos básicos son: int, float, str, bool
- `type()` te dice qué tipo es un dato
- `int()`, `str()`, `float()` convierten entre tipos

## Próxima lección

En la siguiente lección aprenderemos sobre operadores
para hacer cálculos y comparaciones.
```

**Sábado:**

Crear ejercicios: `modulo-1-fundamentos/ejercicios-1.py`

```python
# EJERCICIO 1: FÁCIL
# Crea variables para tu nombre, edad y ciudad
# Luego imprime cada una

nombre = "Tu nombre aquí"
edad = 25
ciudad = "Santiago"

print(nombre)
print(edad)
print(ciudad)

# ===================================

# EJERCICIO 2: MEDIO
# Crea variables con todos los tipos
# Verifica el tipo de cada una

numero = 42
decimal = 3.14
texto = "Python"
verdadero = True

print(type(numero))
print(type(decimal))
print(type(texto))
print(type(verdadero))

# ===================================

# EJERCICIO 3: DESAFIANTE
# Pide el nombre y edad del usuario
# Calcula aproximadamente qué año nació

nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuál es tu edad? "))

año_actual = 2026
año_nacimiento = año_actual - edad

print(f"Hola {nombre}, probablemente naciste en {año_nacimiento}")
```

---

### Domingo: PUBLICACIÓN

```bash
# Agregar archivos
git add modulo-1-fundamentos/

# Hacer commit
git commit -m "Lección 1: Variables y Tipos de Datos - Tutorial, ejemplos y ejercicios"

# Enviar a GitHub
git push origin main
```

Actualizar `README.md`:
```markdown
# Python desde Cero

Aprendiendo Python y creando tutoriales simultáneamente.

## Módulo 1: Fundamentos Básicos

### Lecciones
- [Lección 1: Variables y Tipos de Datos](modulo-1-fundamentos/leccion-1-variables.md)

### Código de Ejemplos
- [Ejemplos Semana 1](modulo-1-fundamentos/ejemplos-semana-1.py)

### Ejercicios
- [Ejercicios Lección 1](modulo-1-fundamentos/ejercicios-1.py)

---

## Progreso General

- [x] Semana 1: Variables y Tipos
- [ ] Semana 2: Operadores
- [ ] Semana 3-4: Control de Flujo
- [ ] Semana 5-6: Funciones
- [ ] Semana 7-10: Estructuras de Datos
- [ ] Semana 11-12: Archivos
- [ ] Semana 13-16: POO
```

Actualizar `PROGRESO.md`:
```markdown
# Progreso de Aprendizaje

## Semana 1: Variables y Tipos de Datos

### Aprendizaje ✅
- [x] Instalar Python y VS Code
- [x] Crear primer programa (hola_mundo.py)
- [x] Entender qué es una variable
- [x] Aprender 4 tipos de datos
- [x] Aprender conversión de tipos

### Creación de Contenido ✅
- [x] Tutorial escrito en Markdown
- [x] Código de ejemplos
- [x] Ejercicios con soluciones
- [ ] Video (opcional para después)

### Publicación ✅
- [x] Commit a GitHub
- [x] Actualizar README

### Reflexión
**Qué fue fácil:** Las variables y los tipos básicos
**Qué fue difícil:** Entender por qué importa la conversión de tipos
**Qué aprendí:** Python es muy flexible con tipos
**Motivación:** 8/10 - ¡Avanzando bien!

---

## Semana 2: Próxima...
```

---

## Semanas Siguientes: Patrón a Repetir

Cada semana siguiente sigue el **mismo patrón:**

1. **Lunes-Miércoles:** Aprende + practica + toma notas
2. **Jueves:** Consolida + crea ejemplos claros
3. **Viernes-Sábado:** Escribe tutorial + crea ejercicios
4. **Domingo:** Publica + actualiza documentación

---

## Herramientas Recomendadas (por Orden de Importancia)

### Esencial
- VS Code (escritura de código)
- Git + GitHub (versionamiento)
- Python 3.9+ (lenguaje)

### Para Tutoriales en Video (opcional)
- OBS Studio (grabar pantalla)
- DaVinci Resolve (editar videos)
- Audacity (editar audio)

### Para Documentación
- Markdown (formato texto)
- MkDocs (generar sitio documentación)

---

## Métricas para Rastrear Progreso

Cada semana registra:

```
SEMANA X RESUMEN
================
Horas de aprendizaje: X horas
Horas de creación: X horas
Líneas de código: X líneas
Tutoriales completados: X
Ejercicios creados: X
Commits a GitHub: X

Sentimiento: 😊/😐/😞
Confianza en tema: X%
Motivación: Alta/Media/Baja
```

Esto te ayuda a mantener consistencia y celebrar progreso.
