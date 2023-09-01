lista1 = ['Marcos','Nunes', 'Souza','Caio', 'Luana']
print(type(lista1))
print(len(lista1))
print(lista1[4])
 #duplicar a lista

lista2 = lista1 *2
print(lista2)


#Adivionar elementos na lista
lista1.append('Amanda')
print(lista1)

#REMOVER ELEMENTOS
lista1.remove('Caio')
print(lista1)
#remover pela posição
lista1.pop(3)
print(lista1)

#exemplo dicionario

dados_cliente = {

"Nome": "Maicon", 
"Endereço":"Rua Fds"
}

print(dados_cliente)['Nome']