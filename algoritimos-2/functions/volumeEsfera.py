raio = int(input('Qual o valor do raio: '))

def volume(raio):
    volume_esfera = (4/3) * 3.14159 * raio**3
    return volume_esfera

print(volume(raio))