#ejercicio 1 leccion_2_operadores

numero1 = input("ingreseprimer número: ")
numero2 = input("ingrese segundo número: ")

suma = float(numero1) + float(numero2)
resta = float(numero1) - float(numero2)
multiplicacion = float(numero1) * float(numero2)
division = float(numero1) / float(numero2)

print("la suma es: " + str(suma))
print("la resta es: " + str(resta))
print("la multiplicación es: " + str(multiplicacion))
print("la división es: " + str(division))

#ejercicio 2 leccion_2_operadores

persona1 = int(input("Ingresa la edad de la persona 1: "))
persona2 = int(input("Ingresa la edad de la persona 2: "))

print("la persona1 es mayor", persona1 > persona2)
print("la persona2 es mayor", persona2 >  persona1)
print("las edades son iguales", persona1 == persona2)
print("la persona1 es mayor o igual a la persona2", persona1 >= persona2)


#ejercicio 3 leccion_2_operadores

ingresa = input("Ingresa tu nota(de 0 a 100):")

aprobado = int(ingresa) >= 60   

print("¿El estudiante está aprobado?", aprobado) 
     
