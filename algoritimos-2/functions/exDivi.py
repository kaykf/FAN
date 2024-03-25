num = int(input('Digite o número: '))
divisor = int(input('Por quanto você quer dividir esse número: '))

def divisao():
    resultado = num / divisor
    resto = num % divisor
    if resto == 0:
        return (f'{resultado} sem resto')
    else:
        return(f'{resultado} com resto {resto}')
    
print(divisao())