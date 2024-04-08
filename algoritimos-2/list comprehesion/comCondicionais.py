numeros = [1,2,3,4,5,6,7,8,9,10]

res = [numero * 2 if numero % 2 ==0 else numero / 2 for numero in numeros]

print(res)