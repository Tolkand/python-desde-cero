
#ejemplo 1: Operadores de comparación

edad = int(input("¿Cuál es tu edad?"))

es_menor = edad < 18
es_adulto = edad >= 18

print("¿Menor de edad?", es_menor)
print("¿Mayor o igual a 18?", es_adulto)




#ejemplo 2: Operadores lógicos

edad = int(input("¿Cuál es tu edad? "))
tiene_entrada = input("¿Tienes entrada? (s/n): ")

tiene_entrada_bool = (tiene_entrada == "s")

puede_entrar = (edad >= 18) and tiene_entrada_bool

print("¿Puede entrar?", puede_entrar)