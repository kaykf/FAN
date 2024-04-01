def calculadora():
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    op = str(input('Digite a operação(+,-,*,/): '))
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 / num2
    else:
        return 'Valor inválido'
    
print(calculadora())