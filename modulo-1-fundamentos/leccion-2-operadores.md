# Lección 2: Operadores en Python

En esta lección usamos variables para hacer cálculos, comparar valores y combinar condiciones con operadores aritméticos, de comparación y lógicos.

---

## 1. Introducción

**Pregunta gancho**  
¿Cómo decide un programa si puedes entrar a una sala de cine solo si tienes cierta edad **y** además tu nombre está en una lista?

La respuesta está en los **operadores**: símbolos como `+`, `-`, `==`, `>`, `and`, `or` que permiten hacer cálculos y tomar decisiones a partir de tus variables.

**Objetivos de la lección**
  - Usar operadores aritméticos para hacer cuentas básicas.
  - Usar operadores de comparación para obtener resultados `True` o `False`.
  - Combinar condiciones con operadores lógicos `and`, `or`, `not`.
  - Hacer pequeños programas interactivos usando `input()`.


---



## 2. Operadores aritméticos

Los operadores **aritméticos** sirven para hacer cuentas con números.

| Operador | Significado      | Ejemplo        |
|--------- |------------------|----------------|
| `+`      | Suma             | `5 + 3` → `8`  |
| `-`      | Resta            | `5 - 3` → `2`  |
| `*`      | Multiplicación   | `5 * 3` → `15` |
| `/`      | División         | `5 / 2` → `2.5`|
| `//`     | División entera  | `5 // 2` → `2` |
| `%`      | Módulo (resto)   | `5 % 2` → `1`  |
| `**`     | Potencia         | `2 ** 3` → `8` |

Ejemplo básico:

```python
a = 10
b = 3

suma = a + b         # 13
resta = a - b        # 7
producto = a * b     # 30
division = a / b     # 3.333...
division_entera = a // b  # 3
resto = a % b        # 1
potencia = a ** b    # 1000

print("Suma:", suma)
print("Resta:", resta)
print("Producto:", producto)
print("División:", division)
print("División entera:", division_entera)
print("Resto:", resto)
print("Potencia:", potencia)
```

---



## 3. Operadores de comparación
Los operadores de comparación devuelven siempre un valor booleano: True o False.

| Operador | Significado        | Ejemplo        |
|--------- |--------------------|----------------|
| ==       | Igual que          | 5 == 5 → True  |
| !=       | Distinto de        | 5 != 3 → True  |
| >        | Mayor que          | 5 > 3 → True   |
| <        | Menor que          | 3 < 5 → True   |
| >=       | Mayor o igual que  | 5 >= 5 → True  |
| <=       | Menor o igual que  | 3 <= 5 → True  |




Ejemplo:

```python
edad = 18

print(edad > 17)    # True  (es mayor de 17)
print(edad >= 18)   # True  (es mayor o igual a 18)
print(edad < 18)    # False
print(edad == 18)   # True
print(edad != 18)   # False
```

---



## 4. Operadores lógicos
Los operadores lógicos permiten combinar comparaciones.


| Operador |   Significado    |    Ejemplo      |
|--------- |------------------|-----------------|
| and      |      Y           | cond1 and cond2 |
| or       |      O           | cond1 or cond2  |
| not      |      NO          | not cond1       |


Ejemplo:

```python
edad = 20
tiene_entrada = True

puede_entrar = (edad >= 18) and tiene_entrada
print(puede_entrar)  # True

es_menor_o_sin_entrada = (edad < 18) or (not tiene_entrada)
print(es_menor_o_sin_entrada)  # False
```

---



## 5. Mini calculadora con input() (repaso)
Aquí combinamos todo lo anterior con un uso básico de input(). Recuerda: input() siempre devuelve texto (str), por eso convertimos a int o float para poder sumar.

```python
print("Calculadora súper simple")

numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

suma = numero1 + numero2
resta = numero1 - numero2
producto = numero1 * numero2
division = numero1 / numero2

print("Suma:", suma)
print("Resta:", resta)
print("Producto:", producto)
print("División:", division)
```

---



## 6. Ejemplos prácticos de la lección

El código completo de esta lección puede ir en
modulo-1-fundamentos/ejemplos/ejemplos_leccion_2_operadores.py


### 6.1 Clasificar edad con comparación

```python
edad = int(input("¿Cuál es tu edad?"))

es_menor = edad < 18
es_adulto = edad >= 18

print("¿Menor de edad?", es_menor)
print("¿Mayor o igual a 18?", es_adulto)
```


### 6.2 Verificar acceso con operadores lógicos

```python
edad = int(input("¿Cuál es tu edad? "))
tiene_entrada = input("¿Tienes entrada? (s/n): ")

tiene_entrada_bool = (tiene_entrada == "s")

puede_entrar = (edad >= 18) and tiene_entrada_bool

print("¿Puede entrar?", puede_entrar)
```

---



## 7. Ejercicios

Puedes guardar las soluciones en
modulo-1-fundamentos/ejercicios/ejercicios_leccion_2.py



- Ejercicio 1 (fácil) – Operaciones básicas

  Pide por teclado dos números y muestra:

  La suma.

  La resta.

  La multiplicación.

  La división.

  Usa float() para permitir decimales.




- Ejercicio 2 (medio) – Comparar edades

  Pide la edad de dos personas y muestra:

  Quién es mayor.

  Si tienen la misma edad.

  Si la primera persona es mayor o igual que la segunda.

  Usa operadores de comparación.




- Ejercicio 3 (medio) – Aprobado o reprobado

  Pide una nota (0 a 100) y muestra:

  True si la nota es mayor o igual a 60 (aprobado).

  False en caso contrario.

  Usa una variable booleana aprobado = nota >= 60 y muéstrala con print(aprobado).

  


- Ejercicio 4 (desafío) – Entrada a evento

  Un evento tiene estas reglas:

  Debes tener al menos 18 años.

  Debes tener entrada ("s") o estar en la lista VIP ("s").

  Pide:

  Edad.

  Si tiene entrada (s/n).

  Si está en la lista VIP (s/n).

  Calcula una variable booleana puede_entrar usando operadores lógicos y muestra el resultado (True o False).

---




## 8. Resumen y siguiente paso

En esta lección viste:

  - Cómo usar operadores aritméticos para hacer cuentas básicas.

  - Cómo usar operadores de comparación para obtener valores True o False.

  - Cómo combinar condiciones con and, or, not.

  - Cómo usar input() para hacer pequeños programas interactivos.

**En la próxima lección crearás condicionales if, elif, else, usando todas estas comparaciones y operadores lógicos para tomar decisiones reales en tu código.**