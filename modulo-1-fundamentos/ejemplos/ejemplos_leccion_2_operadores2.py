edad = int(input("¿Cuál es tu edad? "))
tiene_entrada = input("¿Tienes entrada? (s/n): ")

tiene_entrada_bool = (tiene_entrada == "s")

puede_entrar = (edad >= 18) and tiene_entrada_bool

print("¿Puede entrar?", puede_entrar)