## Ejercicios Generales nivel básico 3
### Te entregamos esta tercera tanda de 20 ejercicios con todo lo visto en el primer módulo. Cada uno con su respuesta. Desarróllalos solo, si necesitas ayuda ve a las soluciones como último recurso.

---

### 41. Bono escolar con múltiples condiciones

-Enunciado
    Pide ingreso familiar mensual, cantidad de hijos en edad escolar y si viven en zona rural.
    Otorga bono si:

        Ingreso ≤ 600.000 OR 4+ hijos escolarizados
        Y además viven en zona rural OR tienen al menos 1 hijo con necesidades especiales.

- Solución

```python
ingreso = float(input("Ingreso familiar mensual: "))
hijos_escolares = int(input("Hijos en edad escolar: "))
rural = input("¿Viven en zona rural? (sí/no): ").lower() == "sí"
necesidades_especiales = input("¿Hijo con necesidades especiales? (sí/no): ").lower() == "sí"

if (ingreso <= 600000 or hijos_escolares >= 4) and (rural or necesidades_especiales):
    print("Bono escolar otorgado")
else:
    print("No califica para bono escolar")
```


### 42. Tarjeta de fidelidad supermercado

- Enunciado
    Pide monto compra mensual acumulado, si es cliente hace +1 año y si compra productos básicos.
    Descuento especial si:

        Monto ≥ 200.000 AND antigüedad ≥ 1 año
        O compra productos básicos Y tiene +5 visitas mensuales.

- Solución

```python
monto_acumulado = float(input("Monto acumulado mensual: "))
antiguedad = int(input("Años como cliente: "))
productos_basicos = input("¿Compra productos básicos? (sí/no): ").lower() == "sí"
visitas = int(input("Visitas mensuales: "))

if (monto_acumulado >= 200000 and antiguedad >= 1) or \
   (productos_basicos and visitas >= 5):
    print("Descuento especial de fidelidad")
else:
    print("Descuento normal")
```    


### 43. Evaluación crédito comercio

- Enunciado
    Pide sueldo líquido, deudas mensuales pendientes y puntaje SII.
    Aprueba crédito si:

        (Sueldo ≥ 800.000 AND deudas ≤ 300.000)
        OR puntaje SII ≥ 700 Y sueldo > deudas * 2.

- Solución

```python
sueldo = float(input("Sueldo líquido: "))
deudas = float(input("Deudas mensuales: "))
puntaje_sii = int(input("Puntaje SII (400-850): "))

if (sueldo >= 800000 and deudas <= 300000) or \
   (puntaje_sii >= 700 and sueldo > deudas * 2):
    print("Crédito comercial aprobado")
else:
    print("Crédito rechazado")
```


### 44. Permiso municipal para ampliación casa

- Enunciado
    Pide metros cuadrados a ampliar, distancia a lote vecino, si es primera ampliación y si cumple normas sísmicas.
    Aprueba si:

        Metros ≤ 20 OR (distancia ≥ 2m AND normas sísmicas)
        Y es primera ampliación OR ya tiene permiso anterior.

- Solución

```python
metros = float(input("Metros cuadrados a ampliar: "))
distancia_vecino = float(input("Distancia a lote vecino (m): "))
primera_ampliacion = input("¿Primera ampliación? (sí/no): ").lower() == "sí"
normas_sismicas = input("¿Cumple normas sísmicas? (sí/no): ").lower() == "sí"
permiso_anterior = input("¿Permiso anterior? (sí/no): ").lower() == "sí"

if (metros <= 20 or (distancia_vecino >= 2 and normas_sismicas)) and \
   (primera_ampliacion or permiso_anterior):
    print("Permiso municipal aprobado")
else:
    print("Permiso denegado")
```


### 45. Evaluación técnica para AFP

- Enunciado
    Pide cotizaciones AFP, sueldo base, edad al afiliarse y si tiene contrato indefinido.
    Rentabilidad esperada alta si:

        Cotizaciones ≥ 120 AND contrato indefinido
        OR (edad ≤ 35 AND sueldo ≥ 1.200.000).

- Solución

```python
cotizaciones = int(input("Meses cotizados AFP: "))
sueldo = float(input("Sueldo base: "))
edad_afiliacion = int(input("Edad al afiliarse AFP: "))
contrato_indefinido = input("¿Contrato indefinido? (sí/no): ").lower() == "sí"

if (cotizaciones >= 120 and contrato_indefinido) or \
   (edad_afiliacion <= 35 and sueldo >= 1200000):
    print("Rentabilidad AFP esperada: ALTA")
else:
    print("Rentabilidad AFP esperada: MEDIA")
```


### 46. Control acceso condominio con mascotas

- Enunciado
    Pide si es residente, hora entrada (0-23), lleva mascota y tiene permiso mascota.
    Permite entrada si:

        Es residente OR (hora entre 8-20 Y tiene permiso mascota)
        Y no lleva mascota OR tiene autorización especial.

- Solución

```python
residente = input("¿Es residente? (sí/no): ").lower() == "sí"
hora = int(input("Hora entrada (0-23): "))
mascota = input("¿Lleva mascota? (sí/no): ").lower() == "sí"
permiso_mascota = input("¿Permiso mascota? (sí/no): ").lower() == "sí"
autorizacion_especial = input("¿Autorización especial? (sí/no): ").lower() == "sí"

if (residente or (8 <= hora <= 20 and permiso_mascota)) and \
   (not mascota or autorizacion_especial):
    print("Acceso al condominio autorizado")
else:
    print("Acceso denegado")
```


### 47. Subsidio de vivienda DS1

- Enunciado
    Pide ingreso nuclear familiar, cantidad personas hogar, hijos menores y ahorro previo.
    Califica subsidio si:

        (Ingreso ≤ 1.200.000 OR 5+ personas hogar)
        Y ahorro ≥ 10 UF
        Y tiene al menos 1 hijo menor OR es adulto mayor.

- Solución

```python
ingreso_familiar = float(input("Ingreso nuclear familiar: "))
personas_hogar = int(input("Personas en hogar: "))
hijos_menores = input("¿Hijos menores? (sí/no): ").lower() == "sí"
adulto_mayor = input("¿Adulto mayor en hogar? (sí/no): ").lower() == "sí"
ahorro_uf = float(input("Ahorro en UF: "))

if (ingreso_familiar <= 1200000 or personas_hogar >= 5) and \
   ahorro_uf >= 10 and (hijos_menores or adulto_mayor):
    print("Califica para subsidio DS1")
else:
    print("No califica")
```


### 48. Evaluación riesgo Isapre

- Enunciado
    Pide edad, IMC, fuma (sí/no), presión arterial alta y antecedentes diabéticos.
    Riesgo alto si:

        Edad ≥ 60 OR IMC ≥ 30
        O (fuma AND presión alta)
        O antecedentes diabéticos Y edad ≥ 45.

- Solución

```python
edad = int(input("Edad: "))
imc = float(input("IMC: "))
fuma = input("¿Fuma? (sí/no): ").lower() == "sí"
presion_alta = input("¿Presión arterial alta? (sí/no): ").lower() == "sí"
diabeticos = input("¿Antecedentes diabéticos? (sí/no): ").lower() == "sí"

if edad >= 60 or imc >= 30 or \
   (fuma and presion_alta) or \
   (diabeticos and edad >= 45):
    print("Riesgo Isapre: ALTO")
else:
    print("Riesgo Isapre: BAJO")
```


### 49. Promoción 2x1 restaurante

- Enunciado
    Pide cantidad platos principales, bebidas, postres y si es cliente frecuente.
    Aplica 2x1 si:

        Compra ≥ 4 platos principales
        O (2 platos principales AND 2 bebidas AND cliente frecuente)
        O total ≥ 40.000 cualquier combinación.

- Solución

```python
platos = int(input("Platos principales: "))
bebidas = int(input("Bebidas: "))
postres = int(input("Postres: "))
cliente_frecuente = input("¿Cliente frecuente? (sí/no): ").lower() == "sí"
total = float(input("Total compra: "))

if platos >= 4 or \
   (platos >= 2 and bebidas >= 2 and cliente_frecuente) or \
   total >= 40000:
    print("Promoción 2x1 aplica")
else:
    print("Promoción no aplica")
```


### 50. Licencia médica electrónica

- Enunciado 
    Pide días solicitados, tiene reposo absoluto, certificado exámenes y antigüedad laboral.
    Aprueba licencia si:

        Días ≤ 10 OR (reposo absoluto AND certificado exámenes)
        Y antigüedad ≥ 6 meses
        O es urgencia vital.

- Solución

```python
dias = int(input("Días licencia solicitada: "))
reposo_absoluto = input("¿Reposo absoluto? (sí/no): ").lower() == "sí"
certificado = input("¿Certificado exámenes? (sí/no): ").lower() == "sí"
antiguedad = int(input("Meses en empresa: "))
urgencia_vital = input("¿Urgencia vital? (sí/no): ").lower() == "sí"

if (dias <= 10 or (reposo_absoluto and certificado)) and \
   (antiguedad >= 6 or urgencia_vital):
    print("Licencia médica aprobada")
else:
    print("Licencia rechazada")
```


### 51. Turno ético diferencial

- Enunciado
    Pide edad paciente, horas desde inicio síntomas, prioridad médica asignada y si acompaña adulto.
    Acceso inmediato si:

        Edad ≤ 5 OR edad ≥ 75
        O prioridad = "alta"
        O (síntomas ≥ 12h AND acompaña adulto).

- Solución

```python
edad = int(input("Edad paciente: "))
horas_sintomas = int(input("Horas desde inicio síntomas: "))
prioridad = input("Prioridad médica (alta/media/baja): ")
acompanado = input("¿Acompañado por adulto? (sí/no): ").lower() == "sí"

if edad <= 5 or edad >= 75 or prioridad == "alta" or \
   (horas_sintomas >= 12 and acompañado):
    print("Acceso inmediato")
else:
    print("Turno normal")
```


### 52. Certificado escolar para viaje

- Enunciado
    Pide faltas injustificadas, promedio anual, conducta docente y destino viaje (nacional/internacional).
    Otorga certificado si:

        Faltas ≤ 5 AND promedio ≥ 5.0
        O conducta "excelente" Y destino nacional
        O internacional Y promedio ≥ 6.5.

- Solución

```python
faltas = int(input("Faltas injustificadas: "))
promedio = float(input("Promedio anual: "))
conducta = input("Conducta docente (buena/excelente): ")
destino = input("Destino (nacional/internacional): ")

if (faltas <= 5 and promedio >= 5.0) or \
   (conducta == "excelente" and destino == "nacional") or \
   (destino == "internacional" and promedio >= 6.5):
    print("Certificado escolar otorgado")
else:
    print("Certificado denegado")
```


### 53. Pago parcial universidad

- Enunciado
    Pide arancel anual, cuotas pagadas, promedio semestre anterior y si tiene beca.
    Autoriza pago parcial si:

        Cuotas ≥ 50% AND promedio ≥ 5.0
        O tiene beca Y arancel ≤ 4.000.000
        O promedio ≥ 6.0 Y compromiso escrito.

- Solución

```python
arancel = float(input("Arancel anual: "))
cuotas_pagadas = float(input("Porcentaje cuotas pagadas: "))
promedio = float(input("Promedio semestre anterior: "))
beca = input("¿Tiene beca? (sí/no): ").lower() == "sí"
compromiso = input("¿Compromiso escrito? (sí/no): ").lower() == "sí"

if (cuotas_pagadas >= 50 and promedio >= 5.0) or \
   (beca and arancel <= 4000000) or \
   (promedio >= 6.0 and compromiso):
    print("Pago parcial autorizado")
else:
    print("Debe pagar completo")
```


### 54. Control de inventario farmacia

- Enunciado
    Pide stock actual paracetamol, stock ibuprofeno, ventas diarias promedio y urgencia reposición.
    Alerta crítica si:

        (Paracetamol ≤ 50 OR ibuprofeno ≤ 30)
        Y ventas ≥ 100 unidades/día
        O urgencia = "alta".

- Solución

```python
stock_paracetamol = int(input("Stock paracetamol: "))
stock_ibuprofeno = int(input("Stock ibuprofeno: "))
ventas_diarias = int(input("Ventas diarias promedio: "))
urgencia = input("Urgencia reposición (alta/media): ")

if (stock_paracetamol <= 50 or stock_ibuprofeno <= 30) and \
   ventas_diarias >= 100 or urgencia == "alta":
    print("ALERTA CRÍTICA: Reponer inmediatamente")
else:
    print("Stock aceptable")
```


### 55. Evaluación profesor para bono

- Enunciado
    Pide horas cátedra semanales, alumnos por curso, evaluación directivos y años experiencia.
    Bono desempeño si:

        Horas ≥ 20 AND alumnos ≤ 35 por curso
        O evaluación "excelente" Y experiencia ≥ 10 años
        O combina horas ≥ 15 Y evaluación "muy buena".

- Solución

```python
horas_catedra = int(input("Horas cátedra semanales: "))
alumnos_curso = int(input("Alumnos por curso: "))
evaluacion = input("Evaluación directivos (muy buena/excelente): ")
experiencia = int(input("Años experiencia: "))

if (horas_catedra >= 20 and alumnos_curso <= 35) or \
   (evaluacion == "excelente" and experiencia >= 10) or \
   (horas_catedra >= 15 and evaluacion == "muy buena"):
    print("Bono desempeño otorgado")
else:
    print("No califica bono")
```


### 56. Autorización junta vecinos

- Enunciado
    Pide porcentaje vecinos a favor, presupuesto requerido, impacto medio ambiente y si es seguridad pública.
    Aprueba proyecto si:

        Vecinos ≥ 70% OR presupuesto ≤ 500.000
        Y no impacta medio ambiente
    O es seguridad pública.

- Solución

```python
vecinos_favor = float(input("Porcentaje vecinos a favor: "))
presupuesto = float(input("Presupuesto requerido: "))
impacto_ambiental = input("¿Impacta medio ambiente? (sí/no): ").lower() == "sí"
seguridad_publica = input("¿Seguridad pública? (sí/no): ").lower() == "sí"

if (vecinos_favor >= 70 or presupuesto <= 500000) and \
   not impacto_ambiental or seguridad_publica:
    print("Proyecto aprobado por junta")
else:
    print("Proyecto rechazado")
```


### 57. Control horario colegio diferencial

- Enunciado
    Pide hora entrada, grado curso, justificación firmada y si es alumno destacado.
    Permite entrada tarde si:

        Hora ≤ 8:30 OR justificación firmada
        Y (grado ≤ 5 básico OR alumno destacado)
        O es director/a de curso.

- Solución

```python
hora_entrada = float(input("Hora entrada (ej: 8.45): "))
grado = int(input("Grado curso (1-12): "))
justificacion = input("¿Justificación firmada? (sí/no): ").lower() == "sí"
destacado = input("¿Alumno destacado? (sí/no): ").lower() == "sí"
director_curso = input("¿Director/a de curso? (sí/no): ").lower() == "sí"

if (hora_entrada <= 8.5 or justificacion) and \
   (grado <= 5 or destacado) or director_curso:
    print("Entrada autorizada")
else:
    print("Entrada no autorizada")
```


### 58. Evaluación riesgo incendio forestal

- Enunciado
    Pide temperatura ambiente, humedad relativa, velocidad viento, sequía acumulada y proximidad población.
    Alerta roja si:

        Temperatura ≥ 35 OR (humedad ≤ 20 AND viento ≥ 30 km/h)
        Y sequía ≥ 60 días
        O proximidad población Y viento ≥ 40 km/h.

- Solución

```python
temperatura = float(input("Temperatura (°C): "))
humedad = float(input("Humedad relativa (%): "))
viento = float(input("Velocidad viento (km/h): "))
sequia_dias = int(input("Días sequía acumulada: "))
proximidad_poblacion = input("¿Cerca población? (sí/no): ").lower() == "sí"

if temperatura >= 35 or (humedad <= 20 and viento >= 30):
    condicion1 = True
else:
    condicion1 = False

if condicion1 and sequia_dias >= 60 or \
   (proximidad_poblacion and viento >= 40):
    print("ALERTA ROJA incendio forestal")
else:
    print("Alerta amarilla")
```


### 59. Certificación instalador gas

- Enunciado
    Pide años experiencia, cursos certificados, inspecciones aprobadas último año y sin accidentes registrados.
    Certifica instalador si:

        Experiencia ≥ 5 años AND cursos ≥ 3
        O (inspecciones ≥ 20 AND sin accidentes)
        Y examen teórico aprobado.

- Solución

```python
experiencia = int(input("Años experiencia: "))
cursos = int(input("Cursos certificados: "))
inspecciones = int(input("Inspecciones aprobadas último año: "))
sin_accidentes = input("¿Sin accidentes? (sí/no): ").lower() == "sí"
examen_teorico = input("¿Examen teórico aprobado? (sí/no): ").lower() == "sí"

if (experiencia >= 5 and cursos >= 3) or \
   (inspecciones >= 20 and sin_accidentes) and examen_teorico:
    print("Certificación instalador gas OTORGADA")
else:
    print("Certificación NO OTORGADA")
```


### 60. Autorización evento público municipal
- Enunciado
    Pide cantidad asistentes esperados, distancia bomberos, tiene seguro eventos, organizador conocido y si es feriado.
    Autoriza evento si:

        (Asistentes ≤ 500 OR bomberos ≤ 5km)
        Y tiene seguro eventos
        Y (organizador conocido OR no es feriado)
        O es evento cultural municipal.

- Solución

```python
asistentes = int(input("Asistentes esperados: "))
distancia_bomberos = float(input("Distancia bomberos (km): "))
seguro_eventos = input("¿Seguro eventos? (sí/no): ").lower() == "sí"
organizador_conocido = input("¿Organizador conocido? (sí/no): ").lower() == "sí"
feriado = input("¿Día feriado? (sí/no): ").lower() == "sí"
evento_cultural = input("¿Evento cultural municipal? (sí/no): ").lower() == "sí"

if (asistentes <= 500 or distancia_bomberos <= 5) and \
   seguro_eventos and (organizador_conocido or not feriado) or \
   evento_cultural:
    print("Evento público AUTORIZADO")
else:
    print("Evento NO AUTORIZADO")
```    