## Ejercicios Generales nivel básico 2
### Te entregamos esta segunda tanda de 20 ejercicios con todo lo visto en el primer módulo. Cada uno con su respuesta. Desarróllalos solo, si necesitas ayuda ve a las soluciones como último recurso.

---

### 21. Boleta de remedios con descuento por adulto mayor

- Enunciado
    Pide el monto de la boleta de farmacia y la edad del cliente.
    Aplica 0% descuento si es adulto mayor (edad ≥ 65 AND monto ≤ 10.000).
    Si no cumple ambas condiciones, cobra normal.

- Solución

```python
monto = float(input("Monto de la boleta: "))
edad = int(input("Edad del cliente: "))

if edad >= 65 and monto <= 10000:
    descuento = monto * 0.0
    print("¡Descuento adulto mayor! Total:", monto - descuento)
else:
    print("Total normal:", monto)
```


### 22. Combo de mercado económico

- Enunciado
    Pide cantidad de arroz (1.500 c/u) y frijoles (2.000 c/u).
    Si compra (arroz ≥ 5 OR frijoles ≥ 3), aplica 10% descuento.

- Solución

```python
arroz = int(input("Kilos de arroz: "))
frijoles = int(input("Kilos de frijoles: "))

total = arroz * 1500 + frijoles * 2000

if arroz >= 5 or frijoles >= 3:
    descuento = total * 0.10
    print("¡Combo económico! Total:", total - descuento)
else:
    print("Total:", total)
```    


### 23. Permiso para trabajar en construcción

- Enunciado
    Pide edad y años de experiencia.
    Se aprueba si (edad ≥ 18 AND experiencia ≥ 1) OR es supervisor (experiencia ≥ 5).

- Solución

```python
edad = int(input("Edad: "))
experiencia = int(input("Años de experiencia: "))

if (edad >= 18 and experiencia >= 1) or experiencia >= 5:
    print("Aprobado para trabajar")
else:
    print("No cumple requisitos")
```

### 24. Descuento feriado largo en mall

- Enunciado
    Pide monto compra y si es fin de semana largo (sí/no).
    Descuento si (monto ≥ 30.000 AND fin_de_semana) OR monto ≥ 80.000.

- Solución

```python
monto = float(input("Monto compra: "))
fin_semana = input("¿Feriado largo? (sí/no): ").lower() == "sí"

if (monto >= 30000 and fin_semana) or monto >= 80000:
    total = monto * 0.90
    print("¡Descuento aplicado! Total:", total)
else:
    print("Total normal:", monto)
```


### 25. Evaluación integral estudiante

- Enunciado
    Pide promedio notas, asistencia % y conducta (buena/mala).
    Aprueba si (promedio ≥ 4.0 AND asistencia ≥ 75%) OR conducta excelente.

- Solución

```python
promedio = float(input("Promedio notas: "))
asistencia = float(input("Asistencia %: "))
conducta = input("Conducta (buena/excelente): ")

if (promedio >= 4.0 and asistencia >= 75) or conducta == "excelente":
    print("Estudiante aprobado")
else:
    print("No aprueba")
```

### 26. Seguro de auto básico

- Enunciado
    Pide años con licencia y edad del auto.
    Cubre siniestros si (licencia ≥ 3 AND auto ≤ 10 años) OR conductor joven responsable.

- Solución

```python
licencia = int(input("Años con licencia: "))
edad_auto = int(input("Edad del auto (años): "))
responsable = input("¿Joven responsable? (sí/no): ").lower() == "sí"

if (licencia >= 3 and edad_auto <= 10) or responsable:
    print("Seguro cubre siniestros")
else:
    print("No cubierto")
```


### 27. Tarifa Uber diferenciada

- Enunciado
    Pide distancia (km), hora pico (sí/no), aeropuerto (sí/no).
    Tarifa alta si hora pico AND distancia > 5 OR aeropuerto.

- Solución

```python
distancia = float(input("Distancia (km): "))
hora_pico = input("¿Hora punta? (sí/no): ").lower() == "sí"
aeropuerto = input("¿Hacia aeropuerto? (sí/no): ").lower() == "sí"

tarifa_normal = distancia * 800

if (hora_pico and distancia > 5) or aeropuerto:
    tarifa = tarifa_normal * 1.5
    print("Tarifa alta:", tarifa)
else:
    print("Tarifa normal:", tarifa_normal)
```


### 28. Crédito vivienda Suseso

- Enunciado
    Pide sueldo líquido, años en empresa, cotizaciones previas.
    Aprueba si (sueldo ≥ 500.000 AND empresa ≥ 2 años) OR cotizaciones ≥ 12.

- Solución

```python
sueldo = float(input("Sueldo líquido: "))
empresa = int(input("Años en empresa: "))
cotizaciones = int(input("Meses cotizados: "))

if (sueldo >= 500000 and empresa >= 2) or cotizaciones >= 12:
    print("Crédito vivienda aprobado")
else:
    print("Requisitos no cumplidos")
```

### 29. Entrada cine con descuento combinado

- Enunciado
    Pide edad, estudiante (sí/no), adulto mayor (sí/no).
    Descuento si (menor 12 OR estudiante) AND no adulto mayor.

- Solución

```python
edad = int(input("Edad: "))
estudiante = input("¿Estudiante? (sí/no): ").lower() == "sí"
adulto_mayor = input("¿Adulto mayor? (sí/no): ").lower() == "sí"

precio_normal = 8500

if (edad < 12 or estudiante) and not adulto_mayor:
    precio = precio_normal * 0.70
    print("Descuento aplicado:", precio)
else:
    print("Precio normal:", precio_normal)
```

### 30. Diagnóstico médico básico
 - Enunciado
    Pide fiebre (°C), dolor cabeza (sí/no), tos (sí/no).
    Sospecha Covid si (fiebre ≥ 38 OR tos) AND dolor cabeza.

- Solución

```python
fiebre = float(input("Temperatura (°C): "))
dolor_cabeza = input("¿Dolor de cabeza? (sí/no): ").lower() == "sí"
tos = input("¿Tos? (sí/no): ").lower() == "sí"

if (fiebre >= 38 or tos) and dolor_cabeza:
    print("Sospecha COVID - hacer test")
else:
    print("No presenta síntomas graves")
```

### 31. Bonificación AFP por ahorro voluntario

- Enunciado
    Pide sueldo, % ahorro voluntario, edad.
    Bonifica si (ahorro ≥ 5% AND sueldo ≤ 1.000.000) OR edad ≥ 55.

- Solución

```python
sueldo = float(input("Sueldo bruto: "))
ahorro_pct = float(input("% ahorro voluntario: "))
edad = int(input("Edad: "))

if (ahorro_pct >= 5 and sueldo <= 1000000) or edad >= 55:
    print("Bonificación AFP aplica")
else:
    print("No aplica bonificación")
```


### 32. Permiso circulación vencido

- Enunciado
    Pide mes permiso, mes actual, multas pendientes (sí/no).
    Puede circular si permiso ≥ mes actual OR sin multas.

- Solución

```python
permiso_mes = int(input("Mes de permiso (1-12): "))
mes_actual = int(input("Mes actual (1-12): "))
multas = input("¿Multas pendientes? (sí/no): ").lower() == "sí"

if permiso_mes >= mes_actual or not multas:
    print("Puede circular")
else:
    print("Permiso vencido + multas")
```

### 33. Evaluación profesor particular

- Enunciado
    Pide nota práctica, asistencia, puntualidad (todas 1-7).
    Excelente si (todas ≥ 6) OR (práctica = 7 AND asistencia ≥ 6).

- Solución

```python
practica = float(input("Nota práctica (1-7): "))
asistencia = float(input("Asistencia (1-7): "))
puntualidad = float(input("Puntualidad (1-7): "))

if (practica >= 6 and asistencia >= 6 and puntualidad >= 6) or \
   (practica == 7 and asistencia >= 6):
    print("Evaluación excelente")
else:
    print("Debe mejorar")
```


### 34. Subsidio escolar municipal

- Enunciado
    Pide ingreso familiar, cantidad hijos, colegio particular (sí/no).
    Aplica subsidio si (ingreso ≤ 800.000 OR 3+ hijos) AND no colegio particular.

- Solución

```python
ingreso = float(input("Ingreso familiar mensual: "))
hijos = int(input("Cantidad hijos: "))
particular = input("¿Colegio particular? (sí/no): ").lower() == "sí"

if (ingreso <= 800000 or hijos >= 3) and not particular:
    print("Subsidio escolar aprobado")
else:
    print("No califica")
```


### 35. Plan gimnasio con horario restringido

- Enunciado
    Pide edad, trabaja turno (sí/no), quiere mañanas (sí/no).
    Acceso mañanas si edad ≤ 25 OR (trabaja turno AND quiere mañanas).

- Solución

```python
edad = int(input("Edad: "))
turno = input("¿Trabaja turnos? (sí/no): ").lower() == "sí"
mananas = input("¿Quiere horario mañanas? (sí/no): ").lower() == "sí"

if edad <= 25 or (turno and mananas):
    print("Acceso horario mañanas OK")
else:
    print("Solo tardes disponibles")
```


### 36. Reembolso viaje Transantiago

- Enunciado
    Pide viajes mensuales, estudiante (sí/no), adulto mayor (sí/no).
    Reembolso si viajes ≥ 80 AND (estudiante OR adulto mayor).

- Solución

```python
viajes = int(input("Viajes mensuales tarjeta: "))
estudiante = input("¿Estudiante? (sí/no): ").lower() == "sí"
adulto_mayor = input("¿Adulto mayor? (sí/no): ").lower() == "sí"

if viajes >= 80 and (estudiante or adulto_mayor):
    print("Reembolso Transantiago aprobado")
else:
    print("No califica para reembolso")
```


### 37. Evaluación delivery Rappi

- Enunciado
    Pide tiempo entrega (min), distancia (km), propina recibida.
    Excelente si (tiempo ≤ 30 OR distancia ≤ 3km) AND propina ≥ 1.000.

- Solución

```python
tiempo = float(input("Tiempo entrega (min): "))
distancia = float(input("Distancia (km): "))
propina = float(input("Propina recibida: "))

if (tiempo <= 30 or distancia <= 3) and propina >= 1000:
    print("Evaluación excelente Rappi")
else:
    print("Debe mejorar servicio")
```


### 38. Acceso sala VIP aeropuerto

- Enunciado
    Pide clase boleto (E/P/N), millas acumuladas, tarjeta black (sí/no).
    Acceso si clase = Ejecutiva OR (millas ≥ 50.000 AND tarjeta black).

- Solución

```python
clase = input("Clase boleto (E/P/N): ")
millas = float(input("Millas acumuladas: "))
black = input("¿Tarjeta Black? (sí/no): ").lower() == "sí"

if clase == "E" or (millas >= 50000 and black):
    print("Acceso Sala VIP aprobado")
else:
    print("Acceso denegado")
```


### 39. Bonificación Isapre familiar
 
 - Enunciado
    Pide cantidad cotizantes familia, ingresos totales, hijos menores.
    Bonificación si (cotizantes ≥ 2 AND ingresos ≤ 2.000.000) OR hijos ≥ 3.

- Solución

```python
cotizantes = int(input("Cotizantes en familia: "))
ingresos = float(input("Ingresos familiares: "))
hijos = int(input("Hijos menores: "))

if (cotizantes >= 2 and ingresos <= 2000000) or hijos >= 3:
    print("Bonificación Isapre familiar")
else:
    print("No aplica bonificación")
```

### 40. Control acceso edificio

- Enunciado
    Pide código residente, hora actual (formato 24h), invitado autorizado (sí/no).
    Acceso si código correcto OR (hora entre 8-20h AND invitado autorizado).

- Solución

```python
codigo = input("Código residente: ")
hora = int(input("Hora actual (0-23): "))
invitado = input("¿Invitado autorizado? (sí/no): ").lower() == "sí"
codigo_correcto = codigo == "R567"

if codigo_correcto or (8 <= hora <= 20 and invitado):
    print("Acceso edificio autorizado")
else:
    print("Acceso denegado")
```    