def adicionar_receita():
    nome = input("Digite o nome da receita: ") # Adiciona o nome da receita
    pais_origem = input("Digite o país de origem da receita: ") # Adiciona o país de origem
    ingredientes = input("Digite os ingredientes da receita (separados por vírgula): ") # Adiciona os Ingredientes
    modo_preparo = input("Digite o modo de preparo da receita: ") # Adiciona o passo a passo
    separador = "----------"
    # Formatação da receita
    receita = f"Nome: {nome}\nPaís de origem: {pais_origem}\nIngredientes: {ingredientes}\nModo de preparo: {modo_preparo}\n{separador}"
    # Adicionando a receita ao arquivo
    with open("receitas.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(receita)
        arquivo.write("\n")
    print("Receita adicionada com sucesso!") # Retorna ao usuario uma mensagem de sucesso

def remover_receita():
    nome_receita = input("Digite o nome da receita que deseja remover: ")
    with open("receitas.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

    removido = False
    with open("receitas.txt", "w", encoding="utf-8") as arquivo:
        i = 0
        while i < len(linhas):
            if nome_receita in linhas[i]:
                removido = True
                # Pular as próximas linhas que contêm informações da receita
                i += 5
                print(f"A receita '{nome_receita}' foi removida.")
            else:
                arquivo.write(linhas[i])
                i += 1
                
    if not removido:
        print(f"A receita '{nome_receita}' não foi encontrada.")
   
def atualizar_receita():
    ...

def visualizar_receita():
    ...
    
def filtrar_pais():
    ...
    
def lista_favoritos():
    ...
    
def receitas_aleatorias():
    ...
    
def filtrar_prato():
    ...
    
# Menu Interativo   
while True: # Loop While para o usuario ter a possibilidade de realizar outra função
    opcao = input("Opções de Entrada:\n1 - Funções Básicas (Adicionar, Remover, Visualizar e Atualizar)\n2 - Funções especiais (Filtrar por país, Lista de favoritos, Receitas aleatórias e Filtrar por tipo de prato)\n3 - Finalizar\n\nDigite o numero referente a operação desejada:")

    if opcao == '1':
        opcao = input("Opções de Entrada:\n1 - Adicionar \n2 - Remover\n3 - Atualizar\n4 - Visualizar\n5 - Voltar para início\n\nDigite o numero referente a operação desejada: ")
        if opcao == '1':
            adicionar_receita()
        elif opcao == '2':
            remover_receita()
        elif opcao == '3':
            atualizar_receita()
        elif opcao == '4':
            visualizar_receita()
        elif opcao == '5':
            continue
    elif opcao == '2':
        opcao = input("Opções de Entrada:\n1 - Filtrar por país \n2 - Lista de favoritos\n3 - Receitas aleatórias\n4 - Filtrar por tipo de prato\n5 - Voltar para início\n\nDigite o numero referente a operação desejada: ")
        if opcao == '1':
            filtrar_pais()
        elif opcao == '2':
            lista_favoritos()
        elif opcao == '3':
            receitas_aleatorias()
        elif opcao == '4':
            filtrar_prato()
        elif opcao == '5':
            continue
    elif opcao == '3':
        break