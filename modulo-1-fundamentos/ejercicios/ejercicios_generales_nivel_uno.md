## Ejercicios Generales nivel básico 1
### Te entregamos 20 ejercicios con todo lo visto en el primer módulo. Cada uno con su respuesta. Desarróllalos solo, si necesitas ayuda ve a las soluciones como último recurso.

---

### 1. Calcular el total a pagar en una panadería

- Enunciado
    Pide al usuario cuántos panes (precio 800 c/u) y cuántas marraquetas (precio 600 c/u) compró, y muestra el total a pagar.

- Solución

```python
precio_pan = 800
precio_marraqueta = 600

cantidad_pan = int(input("¿Cuántos panes compraste? "))
cantidad_marraqueta = int(input("¿Cuántas marraquetas compraste? "))

total = cantidad_pan * precio_pan + cantidad_marraqueta * precio_marraqueta

print("El total a pagar es:", total)
```


### 2. Conversor de minutos a horas

- Enunciado
    Pide al usuario una cantidad de minutos y muestra cuántas horas completas son, y cuántos minutos sobran.

- Solución

```python
minutos = int(input("Ingresa la cantidad de minutos: "))

horas = minutos // 60
resto_minutos = minutos % 60

print("Son", horas, "hora(s) y", resto_minutos, "minuto(s).")
```



### 3. Descuento simple en una tienda

- Enunciado
    Pide al usuario el precio de un producto.
    Si el precio es mayor o igual a 20.000, aplica un 10% de descuento. Si no, cobra el precio normal.
    Muestra el total a pagar.

- Solución

```python
precio = float(input("Ingresa el precio del producto: "))

if precio >= 20000:
    descuento = precio * 0.10
    total = precio - descuento
else:
    total = precio

print("El total a pagar es:", total)
```


### 4. Verificar mayoría de edad

- Enunciado
    Pide la edad de una persona y muestra si es “Mayor de edad” (18 o más) o “Menor de edad”.

- Solución

```python
edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")
```    


### 5. Promedio de notas simple

- Enunciado
    Pide tres notas (pueden ser flotantes), calcula el promedio y muestra si la persona “Aprueba” (promedio ≥ 4.0) o “Reprueba”.

- Solución

```python
nota1 = float(input("Ingresa la primera nota: "))
nota2 = float(input("Ingresa la segunda nota: "))
nota3 = float(input("Ingresa la tercera nota: "))

promedio = (nota1 + nota2 + nota3) / 3

print("Tu promedio es:", promedio)

if promedio >= 4.0:
    print("Apruebas")
else:
    print("Repruebas")
```


### 6. Cálculo de sueldo diario

- Enunciado
    Pide al usuario cuántas horas trabajó en el día y su valor por hora.
    Calcula y muestra su pago por el día.
    Si trabajó más de 8 horas, las horas extra se pagan al 50% más (1.5 veces el valor normal).

- Solución

```python
horas = float(input("Horas trabajadas hoy: "))
valor_hora = float(input("Valor por hora: "))

if horas <= 8:
    pago = horas * valor_hora
else:
    horas_normales = 8
    horas_extra = horas - 8
    pago = horas_normales * valor_hora + horas_extra * valor_hora * 1.5

print("Tu pago por el día es:", pago)
```


### 7. Verificar si un número es par o impar

- Enunciado
    Pide un número entero y muestra si es “Par” o “Impar”.
    Esto podría servir, por ejemplo, para decidir turnos por números pares/impares.

- Solución

```python
numero = int(input("Ingresa un número entero: "))

if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")
```


### 8. Evaluar presupuesto de compra

- Enunciado
    Pide el presupuesto disponible y el precio de un producto.
    Si el presupuesto alcanza, muestra “Puedes comprarlo” y cuánto dinero sobraría.
    Si no alcanza, muestra “No puedes comprarlo” y cuánto falta.

- Solución

```python
presupuesto = float(input("Tu presupuesto disponible: "))
precio = float(input("Precio del producto: "))

if presupuesto >= precio:
    sobra = presupuesto - precio
    print("Puedes comprarlo. Te sobran", sobra)
else:
    falta = precio - presupuesto
    print("No puedes comprarlo. Te faltan", falta)
```


### 9. Verificación de contraseña simple

- Enunciado
    Define una contraseña fija en el código (por ejemplo "secreto123").
    Pide al usuario que la ingrese.
    Si coincide, muestra “Acceso concedido”, si no, “Acceso denegado”.

- Solución

```python
contrasena_guardada = "secreto123"

contrasena_usuario = input("Ingresa la contraseña: ")

if contrasena_usuario == contrasena_guardada:
    print("Acceso concedido")
else:
    print("Acceso denegado")
```


### 10. Calculadora de índice de masa corporal (IMC)

- Enunciado
    Pide peso (kg) y altura (m).
    Calcula el IMC con la fórmula 
    IMC = peso / altura 2
    
    Muestra el valor del IMC y un mensaje:
        Menor a 18.5: “Bajo peso”
        Entre 18.5 y 24.9: “Normal”
        25 o más: “Sobrepeso”

- Solución

```python
peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))

imc = peso / (altura ** 2)

print("Tu IMC es:", imc)

if imc < 18.5:
    print("Bajo peso")
elif imc < 25:
    print("Normal")
else:
    print("Sobrepeso")
``` 

### 11. Clasificar temperatura ambiente

- Enunciado
    Pide la temperatura en grados Celsius.
    
    Muestra:

        “Frío” si es menor a 10
        “Templado” si está entre 10 y 25 (incluyendo 10 y 25)
        “Caluroso” si es mayor a 25

- Solución

```python
temp = float(input("Temperatura en °C: "))

if temp < 10:
    print("Frío")
elif temp <= 25:
    print("Templado")
else:
    print("Caluroso")
```

### 12. Envío gratuito según monto

- Enunciado
    Pide el monto de la compra online.
    Si el monto es mayor o igual a 50.000, el envío es gratis.
    Si no, el envío cuesta 3.000.
    Muestra el costo total (compra + envío).

- Solución

```python
monto = float(input("Monto de la compra: "))

if monto >= 50000:
    envio = 0
else:
    envio = 3000

total = monto + envio

print("Costo de envío:", envio)
print("Total a pagar:", total)
```


### 13. Comparar dos números (por ejemplo, ofertas)

- Enunciado
    Pide dos precios de productos similares (por ejemplo, dos marcas distintas).
    Indica cuál es más barato o si son iguales.

- Solución

```python
precio1 = float(input("Precio del producto 1: "))
precio2 = float(input("Precio del producto 2: "))

if precio1 < precio2:
    print("El producto 1 es más barato")
elif precio2 < precio1:
    print("El producto 2 es más barato")
else:
    print("Ambos productos tienen el mismo precio")
```


### 14. Cálculo de consumo de agua diario

- Enunciado
    Pide cuántos vasos de agua (250 ml c/u) bebió la persona en el día.
    Calcula cuántos litros tomó.
    Si tomó menos de 2 litros, muestra “Debes beber más agua”, si no, “Buen consumo de agua”.

- Solución

```python
vasos = int(input("¿Cuántos vasos de agua tomaste hoy? (250 ml c/u): "))

mililitros = vasos * 250
litros = mililitros / 1000

print("Has bebido", litros, "litros de agua.")

if litros < 2:
    print("Debes beber más agua")
else:
    print("Buen consumo de agua")
```


### 15. Descuento según tipo de cliente

- Enunciado
    Pide el monto de la compra y el tipo de cliente:

        "normal" → sin descuento

        "frecuente" → 5% descuento

        "vip" → 10% descuento

    Calcula el total con el descuento correspondiente.

- Solución

```python
monto = float(input("Monto de la compra: "))
tipo = input("Tipo de cliente (normal/frecuente/vip): ")

if tipo == "normal":
    descuento = 0
elif tipo == "frecuente":
    descuento = monto * 0.05
elif tipo == "vip":
    descuento = monto * 0.10
else:
    descuento = 0
    print("Tipo de cliente no reconocido, sin descuento.")

total = monto - descuento

print("Descuento aplicado:", descuento)
print("Total a pagar:", total)
```


### 16. Cálculo de nota final con asistencia

- Enunciado
    Pide la nota final (promedio de pruebas) y el porcentaje de asistencia.
    Para aprobar se requiere:

        Nota ≥ 4.0
        Asistencia ≥ 75%

    Muestra si la persona “Aprueba” o “Reprueba”.

- Solución

```python
nota = float(input("Nota final: "))
asistencia = float(input("Asistencia (porcentaje, sin %): "))

if nota >= 4.0 and asistencia >= 75:
    print("Aprueba")
else:
    print("Reprueba")
```

### 17. Conversor de moneda simple (CLP a USD)

- Enunciado
    Pide un monto en CLP y un valor de dólar (por ejemplo, 950 CLP).
    Convierte el monto a dólares y muestra el resultado.
    Si el monto en dólares es menor a 10, muestra “Monto pequeño en USD”, si no, “Monto significativo”.

- Solución

```python
monto_clp = float(input("Monto en CLP: "))
valor_dolar = float(input("Valor actual del dólar en CLP: "))

monto_usd = monto_clp / valor_dolar

print("Equivale a", monto_usd, "USD")

if monto_usd < 10:
    print("Monto pequeño en USD")
else:
    print("Monto significativo")
```


### 18. Calcular consumo de combustible en un viaje

- Enunciado
    Pide la distancia recorrida (km) y el rendimiento del auto (km por litro).
    Calcula cuántos litros se usaron.
    Si se usaron más de 20 litros, muestra “Alto consumo”, si no, “Consumo moderado”.

- Solución

```python
distancia = float(input("Distancia recorrida (km): "))
rendimiento = float(input("Rendimiento del auto (km por litro): "))

litros = distancia / rendimiento

print("Litros consumidos:", litros)

if litros > 20:
    print("Alto consumo")
else:
    print("Consumo moderado")
```


### 19. Verificar si un año es bisiesto (versión básica)

- Enunciado
    Pide un año y muestra si es bisiesto o no usando la regla simplificada:

    Es bisiesto si es divisible por 4.
    (Nota: es una versión simplificada para nivel básico.)

- Solución

```python
anio = int(input("Ingresa un año: "))

if anio % 4 == 0:
    print("El año es bisiesto (regla simple)")
else:
    print("El año no es bisiesto (regla simple)")
```

### 20. Cálculo de tarifa de estacionamiento

- Enunciado
    Pide las horas de estacionamiento de un vehículo.
    La tarifa es:

        1.000 por cada hora completa
        Si hay fracción de hora (ej: 2.5 horas), se cobra la hora extra completa (2.5 → 3 horas).

    Calcula y muestra el total a pagar.

-  Solución

```python
horas = float(input("Horas de estacionamiento: "))

horas_cobradas = int(horas)

if horas != horas_cobradas:
    horas_cobradas = horas_cobradas + 1

tarifa_por_hora = 1000
total = horas_cobradas * tarifa_por_hora

print("Horas cobradas:", horas_cobradas)
print("Total a pagar:", total)
```