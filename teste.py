nomes = [ ]
tipos_prato = { }
paises_origem = { }


def adicionar_receita():
    nome = input("Digite o nome da receita: ") # Adiciona o nome da receita
    if nome in nomes:
        print("A receita já foi adicionada.")
        return
    tipo_prato = input("Digite o tipo do prato (Sobremesa, Salada, Aperitivo etc): ")
    pais_origem = input("Digite o país de origem da receita: ") # Adiciona o país de origem
    ingredientes = input("Digite os ingredientes da receita (separados por vírgula): ") # Adiciona os Ingredientes
    modo_preparo = input("Digite o modo de preparo da receita: ") # Adiciona o passo a passo
    separador = "----------"
    # Formatação da receita
    receita = f"Nome: {nome}\nTipo de prato: {tipo_prato}\nPaís de origem: {pais_origem}\nIngredientes: {ingredientes}\nModo de preparo: {modo_preparo}\n{separador}"
    # lista para armazenar nomes
    nomes.append(nome)
    # dic pratos
    if tipo_prato not in tipos_prato:
        print(f"Nova categoria de pratos foi adicionada: {tipo_prato}")
        tipos_prato[tipo_prato] = [ ]
        tipos_prato[tipo_prato].append(nome)
    elif tipo_prato in tipos_prato:
        print(f"{nome} foi adicionado na categoria: {tipo_prato}")
        tipos_prato[tipo_prato].append(nome)
    # dic paises
    if pais_origem not in paises_origem:
        print(f"Novo paìs de origem foi adicionado: {pais_origem}")
        paises_origem[pais_origem] = [ ]
        paises_origem[pais_origem].append(nome)
    elif pais_origem in paises_origem:
        print(f"{nome} origina do país: {tipo_prato}")
        paises_origem[pais_origem].append(nome)
    # Adicionando a receita ao arquivo
    with open("receitas.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(receita)
        arquivo.write("\n")
    print("Receita adicionada com sucesso!") # Retorna ao usuario uma mensagem de sucesso

def remover_receita():
    nome_receita = input("Digite o nome da receita que deseja remover: ")
    # remover os dados adicionados previamente
    if nome_receita in nomes:
        nomes.remove(nome_receita)
        for tipo, receitas in tipos_prato.items():
            if nome_receita in receitas:
                receitas.remove(nome_receita)
                print(f"A receita '{nome_receita}' foi removida da categoria '{tipo}'.")
        for pais, receitas in paises_origem.items():
            if nome_receita in receitas:
                receitas.remove(nome_receita)
                print(f"A receita '{nome_receita}' foi removida do país '{pais}'.")
    with open("receitas.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
    removido = False
    with open("receitas.txt", "w", encoding="utf-8") as arquivo:
        i = 0
        while i < len(linhas):
            if nome_receita in linhas[i]:
                removido = True
                # Pular as próximas linhas que contêm informações da receita
                i += 6
                print(f"A receita '{nome_receita}' foi removida.")
            else:
                arquivo.write(linhas[i])
                i += 1
    if not removido:
        print(f"A receita '{nome_receita}' não foi encontrada.")
# Menu Interativo   
while True: # Loop While para o usuario ter a possibilidade de realizar outra função
    opcao = input("Opções de Entrada:\n\n1 - Funções Básicas (Adicionar, Remover, Visualizar e Atualizar)\n2 - Funções especiais (Filtrar por país, Lista de favoritos, Receitas aleatórias e Filtrar por tipo de prato)\n3 - Finalizar\n\nDigite o numero referente a operação desejada:")
    if opcao == '1':
        opcao = input("Opções de Entrada:\n\n1 - Adicionar \n2 - Remover\n3 - Atualizar\n4 - Visualizar\n5 - Voltar para início\n\nDigite o numero referente a operação desejada: ")
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
        opcao = input("Opções de Entrada:\n\n1 - Filtrar por país \n2 - Lista de favoritos\n3 - Receitas aleatórias\n4 - Filtrar por tipo de prato\n5 - Voltar para início\n\nDigite o numero referente a operação desejada: ")
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