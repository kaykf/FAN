a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

def somar (a,b,c):
    resultado = a+ b+ c
    return  resultado

print(f'O resultado é {somar(a,b,c)}')