def listar_favoritos():
    if favoritos:
        print("Receitas Favoritas:")
        for receita in favoritos:
            print(receita)
    else:
        print("Nenhuma receita favorita encontrada.")

# Menu Interativo
while True:
    opcao = input("Opções de Entrada:\n\n1 - Funções Básicas (Adicionar, Remover, Visualizar e Atualizar)\n2 - Funções especiais (Filtrar por país, Lista de favoritos, Receitas aleatórias e Filtrar por tipo de prato)\n3 - Finalizar\n\nDigite o número referente à operação desejada: ")
    if opcao == '1':
        opcao = input("Opções de Entrada:\n\n1 - Adicionar\n2 - Remover\n3 - Atualizar\n4 - Visualizar\n5 - Voltar para início\n\nDigite o número referente à operação desejada: ")
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
        opcao = input("Opções de Entrada:\n\n1 - Filtrar por país \n2 - Lista de favoritos\n3 - Receitas aleatórias\n4 - Filtrar por tipo de prato\n5 - Voltar para início\n\nDigite o número referente à operação desejada: ")
        if opcao == '1':
            filtrar_pais()
        elif opcao == '2':
            listar_favoritos()
        elif opcao == '3':
            receitas_aleatorias()
        elif opcao == '4':
            filtar_prato()
        elif opcao == '5':
            continue
    elif opcao == '3':
        break