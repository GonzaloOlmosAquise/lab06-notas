n1 = float(input("Ingrese la nota 1: "))
n2 = float(input("Ingrese la nota 2: "))
n3 = float(input("Ingrese la nota 3: "))

promedio = (n1 + n2 + n3)/3

print(f"El promedio es: {promedio}")
if promedio >= 10.5:
    print("Aprobado")
else:
    print("Desaprobado")
    
#Todo esto es nuevo 