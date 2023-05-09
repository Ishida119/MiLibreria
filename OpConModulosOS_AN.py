########################################################################## OPERACIONES DE FRACCIONES CON MÓDULOS DE ORDEN SUPERIOR
# from difflib import restore
# import MiLibrería
# import math

# # Leer fracción
# print("Para la primera fracción")
# num1=MiLibrería.LeerEntero(-50,50,"Digite numerador 1: ")
# den1=MiLibrería.LeerEntero(-50,50,"Digite denominador 1: ")
# print("Para la segunda fracción")
# num2=MiLibrería.LeerEntero(-50,50,"Digite numerador 2: ")
# den2=MiLibrería.LeerEntero(-50,50,"Digite denominador 2: ")

# # Simplificar cada fracción
# def simplificar(num, den):
#     if den == 0:
#         return "El denominador no puede ser 0"
#     else:
#         mcd = math.gcd(num, den)
#         num1 = num // mcd
#         den1 = den // mcd
#         return (num, den)
# fracción_1=simplificar(num1,den1)
# fracción_2=simplificar(num2,den2)
# # Calcular las operaciones
# def calcular_fracción(num1, den1, num2, den2, operación):
#     if den1 == 0 or den2 == 0:
#         return "El denominador no puede ser 0"
#     else:
#         if operación == "+":
#             num = (num1*den2) + (num2*den1)
#             den = den1 * den2
#         elif operación == "-":
#             num = (num1*den2) - (num2*den1)
#             den = den1 * den2
#         elif operación == "*":
#             num = num1 * num2
#             den = den1 * den2
#         elif operación == "/":
#             num = num1 * den2
#             den = num2 * den1
#         else:
#             return "Operación no válida"
#         return simplificar(num, den)

# # Programa principal
# operación = input("Ingrese la operación (+, -, *, /): ")
# resultado = calcular_fracción(num1, den1, num2, den2, operación)
# print(resultado)


########################################################################## OPERACIONES DE NÚMEROS CON MÓDULOS DE ORDEN SUPERIOR 
# from difflib import restore
# import MiLibrería

# ########################
# def Sumar(a,b):
#     return a+b
# def Restar(a,b):
#     return a-b
# def Multiplicar(a,b):
#     return a*b
# def Dividir(a,b):
#     return a//b
    
# def RealizarOperación(operación, a, b):
#     operaciones = {
#         1: Sumar,
#         2: Restar,
#         3: Multiplicar,
#         4: Dividir
#     }
#     return operaciones[operación](a, b)

# a = int(input("Ingrese un numero: "))
# b = int(input("Ingrese otro numero: "))
# opción = MiLibrería.LeerEntero(1, 4, "Escoge una operación sumar(1), restar(2), multiplicar(3), dividir (4)): ")

# resultado = RealizarOperación(opción, a, b)
# print("El resultado de la operación es :",resultado)

########################################################################## OPERACIONES DE NÚMEROS CON MÓDULOS ANÓNIMOS 

# from difflib import restore
# import MiLibrería

# Realizar_Operación = lambda operación, a, b: (
#     (a + b) if operación == 1
#     else (a - b) if operación == 2
#     else (a * b) if operación == 3
#     else (a // b)
# )

# a = int(input("Ingrese un numero: "))
# b = int(input("Ingrese otro numero: "))
# opción = MiLibrería.LeerEntero(1, 4, "Escoge una operación sumar(1), restar(2), multiplicar(3), dividir (4)): ")

# resultado = Realizar_Operación(opción, a, b)
# print("El resultado de la operación es :",resultado)




