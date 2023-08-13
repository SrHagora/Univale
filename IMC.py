

def calculo_de_imc (pesso, altura):
    IMC = pesso/altura **2
    return IMC

def interpretar_imc(imc):
    if IMC < 18.5:
        return "Abaixo do peso"
    elif IMC < 24.9:
        return "Peso normal"
    elif IMC < 29.9:
        return "Sobrepeso"
    else:
        return "Obeso"



altura = float (input("Qual e sua altura"))
pesso =  float (input("Qual e sua pesso"))
IMC = calculo_de_imc (pesso, altura)
interpretacao = interpretar_imc(IMC)

print(f"Seu IMC é {IMC:.2f}, o que é considerado {interpretacao}.")
