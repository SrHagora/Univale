numeros = []


for i in range(5):
    try:
        numero = int(input("Digite um número inteiro: "))
        numeros.append(numero)
    except ValueError:
        print("Você não digitou um número inteiro.")

# Calcula a soma dos números na lista
soma = 0
for numero in numeros:
    soma += numero

# Exibe a lista de números e a soma
print("Números digitados:", numeros)
print("Soma dos números:", soma)
