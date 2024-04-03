receita = {
    'jan': 100, 'fev':200, 'mar':500
}

receita['abr'] = 350

novo_dado = {'mai':500}
receita.update(novo_dado)

print(receita)
print(novo_dado)