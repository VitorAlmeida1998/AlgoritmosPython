import json

pedidos = []

def visualizar_pedido():
    # Abre o arquivo JSON
    with open("pedidos.json", "r") as f:
        pedidos = json.load(f)
# Imprime os pedidos
    for pedido in pedidos:
        print(pedido)


def cadastrar_pedido():

    #Informações dos clientes
    nome = input("Nome:")
    cpf = input("CPF:")
    endereco = input("Endereço")

    #Solicita o prato do cliente
    prato = input("Qual será seu prato:")

    #Adicione o pedido a lista
    pedidos.append({
        "nome": nome,
        "cpf": cpf,
        "endereço": endereco,
        "prato": prato,
    })

    with open ("pedidos.json","w") as f:
        json.dump(pedidos,f)


#Lista dos pedidos
print ("###########################################################")
print ("#                                                         #")
print ("#                   FAÇA SEU PEDIDO!                      #")
print ("#                                                         #")
print ("#                 (1) CADASTRAR PEDIDO                    #")
print ("#                 (2) VISUALIZAR PEDIDOS                  #")
print ("#                 (3) CADASTRAR PRATOS                    #")
print ("#                                                         #")
print ("#                                                         #")
print ("###########################################################")

option = int(input("Escolha uma opção:"))

if(option == 1):
    cadastrar_pedido()
elif(option == 2):
    visualizar_pedido()    

