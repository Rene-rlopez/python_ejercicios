
numero1 = '10'
numero2 = '6'
operador = '+'


if len(numero1) > 4 or len(numero2) > 4:
    print('Error: Numbers cannot be more than four digits.')

length = max(len(numero1), len(numero2)) + 2

print(f"{numero1:>{length}}")
print(f"{operador}{numero2:>{length - 1}}")
print(f"-" * length)