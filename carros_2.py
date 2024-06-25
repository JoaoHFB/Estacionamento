'''
crie uma aplicação com python com o seguinte menu:
1 - adicionar 
2 - remover
3 - listar
4 - Verficiar se est\ na lista 
0 - sair
Onde seja possivel adicionar. remover, listar ou procurar os carros cadastrados em uma lista.
O usuario ira informar o nome do carro, a placa e o valor. 
Não deve deixar cadastrar a placa de uma carro que ja foi cadastrado anteriormente
utilize funções para desenvolver
'''
carros = () #Define uma lista
def menu(): #Entrega para o usuario um menu.
    print("1 - Adicionar")
    print("2 - Remover")
    print("3 - Listar")
    print("4 - Verificar se está na lista")
    print("0 - Sair")
    opt = input("Selecione a opção: ")
    return opt

def add(): #Adiciciona a função para adicionar carros ao programa
    placa = input('Digite a placa: ').upper()
    if placa in carros:
        print("Placa já cadastrada!")
        return
    modelo = input('Digite o modelo: ')
    valor = float(input("Digite o valor do veículo: "))
    carros[placa] = (modelo, valor)
    print("Carro adicionado com sucesso!")

def remover(): #Adiciciona a função para remover carros ao programa
    placa = input('Digite a placa do carro a ser removido: ').upper()
    if placa in carros:
        del carros[placa]
        print("Carro removido com sucesso!")
    else:
        print("Carro não encontrado!")

def listar(): #Lista todos os carros que foram adicionados
    if not carros:
        print("Nenhum carro cadastrado.")
    else:
        for placa, (modelo, valor) in carros.items():
            print(f"Placa: {placa}, Modelo: {modelo}, Valor: {valor}")

def buscar(): #Serve para buscar carros que ja foram adicinados
    placa = input('Digite a placa do carro que deseja verificar: ').upper()
    if placa in carros:
        modelo, valor = carros[placa]
        print(f"Carro encontrado! Modelo: {modelo}, Valor: {valor}")
    else:
        print("Carro não encontrado!")

def caminho(opt):
    if opt == '1':
        add()
    elif opt == '2':
        remover()
    elif opt == '3':
        listar()
    elif opt == '4':
        buscar()
    elif opt == "0":
        return False
    else:
        print("Opção inválida!")
    return True

if __name__ == '__main__':
    while True:
        opt = menu()
        if not caminho(opt):
            break
    print("Programa encerrado.")