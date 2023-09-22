# Função que exibe uma mensagem simples
def ola():
    print("Olá, mundo!")


ola()

#2
# Função que calcula a área de um retângulo
def calcular_area_retangulo(base, altura):
    area = base * altura
    print(f"A área do retângulo é {area} metros quadrados.")

calcular_area_retangulo(5, 3)


#3
# Função que calcula a média de uma lista de números
def calcular_media(numeros):
    if len(numeros) == 0:
        return None  
    soma = sum(numeros)
    media = soma / len(numeros)
    return media

lista_numeros = [10, 15, 20, 25, 30]
media_resultado = calcular_media(lista_numeros)
if media_resultado is not None:
    print(f"A média dos números é {media_resultado}")
else:
    print("A lista está vazia.")
