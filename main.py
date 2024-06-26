import os
import random

def adicionar_receita():
    os.system('cls')
    nome = input("Digite o nome da receita: ").lower() 
    if nome in nomes:
        os.system('cls')
        print("A receita já foi adicionada.\n")
        input("Pressione ENTER para continuar")
        return
    tipo_prato = input("Digite o tipo do prato (Sobremesa, Salada, Aperitivo etc): ").lower()
    pais_origem = input("Digite o país de origem da receita: ").lower() 
    ingredientes = input("Digite os ingredientes da receita (separados por vírgula): ").lower() 
    modo_preparo = input("Digite o modo de preparo da receita: ").lower() 
    separador = "----------"

    os.system('cls')
   
    receita = f"Nome: {nome}\nTipo de prato: {tipo_prato}\nPaís de origem: {pais_origem}\nIngredientes: {ingredientes}\nModo de preparo: {modo_preparo}\n{separador}"
   
    nomes.append(nome)
    
    with open("receitas.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(receita)
        arquivo.write("\n")
    print("Receita adicionada com sucesso!\n") 
    input("Pressione ENTER para continuar")

def remover_receita():
    os.system('cls')

    nome_receita = input("Digite o nome da receita que deseja remover: ").lower()

    if nome_receita in nomes:
        nomes.remove(nome_receita)
        if nome_receita in favoritos:
            favoritos.remove(nome_receita)

    with open("receitas.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

    removido = False

    with open("receitas.txt", "w", encoding="utf-8") as arquivo:
        i = 0
        while i < len(linhas):
            if nome_receita in linhas[i]:
                removido = True
                i += 6
                print(f"\nA receita '{nome_receita}' foi removida.\n")
            else:
                arquivo.write(linhas[i])
                i += 1
    if not removido:
        print(f"\nA receita '{nome_receita}' não foi encontrada.\n")
    input("Pressione ENTER para continuar")

def visualizar_receita():
    os.system('cls')
    resposta = input("Opções de Entrada:\n\n1 - visualizar todas as receitas\n2 - visualizar uma receita específica\n\nDigite o numero referente a operação desejada: ")

    if resposta == '1':
        os.system('cls')
        with open("receitas.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                print(linha.strip())

    elif resposta == '2':
        os.system('cls')
        nome_receita = input("Qual receita você deseja visualizar: ").lower()
        with open("receitas.txt", "r", encoding="utf-8") as arquivo:
            print()
            linhas = arquivo.readlines()
            i = 0
            while i < len(linhas):
                if nome_receita in linhas[i]:
                    os.system("cls")
                    print(f"Receita encontrada!\n\nNome: {nome_receita}")
                    for j in range(i + 1, min(i + 6, len(linhas))):  
                        print(linhas[j], end='')
                    break
                i += 1
            else:
                print(f"\nA receita '{nome_receita}' não foi encontrada.")
    input("\nPressione ENTER para continuar")

def filtrar_pais():
    os.system('cls')
    pais = input("Digite o país que você deseja filtar: ").lower()
    with open("receitas.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        i = 0
        encontrou_pais = False
        while i < len(linhas):
            if pais in linhas[i]:
                encontrou_pais = True
                print(f"\nPaís encontrado!\n")
                for j in range(i - 2, i + 4): 
                    print(linhas[j], end='')
            i += 1
        if not encontrou_pais:
            print(f"\nO {pais} não foi encontrado.")
    input("\nPressione ENTER para continuar")

def filtar_prato():
    os.system('cls')
    tipos_prato = input("Digite o tipo de prato que você deseja filtrar: ").lower()
    with open("receitas.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        i = 0
        encontrou_prato = False
        while i < len(linhas):
            if tipos_prato in linhas[i]:
                encontrou_prato = True
                print(f"\nTipo de prato encontrado!\n")
                for j in range(i - 1, i + 5):  
                    print(linhas[j], end='')
            i += 1
        if not encontrou_prato:
            print(f"\nO {tipos_prato} não foi encontrado.")
    input("\nPressione ENTER para continuar")

def atualizar_receita():
    os.system('cls')
    nome_atualizar = input("Digite o nome da receita que deseja atualizar: ").lower()

    if nome_atualizar not in nomes:
        print(f"\nA receita '{nome_atualizar}' não foi encontrada.")
        return

    tipo_prato_novo = input("\nDigite o novo tipo do prato (Sobremesa, Salada, Aperitivo etc): ").lower()
    pais_origem_novo = input("Digite o novo país de origem da receita: ").lower()
    ingredientes_novos = input("Digite os novos ingredientes da receita (separados por vírgula): ").lower()
    modo_preparo_novo = input("Digite o novo modo de preparo da receita: ").lower()
    separador = "----------"

    os.system('cls')

    indice_receita = nomes.index(nome_atualizar)
    nomes[indice_receita] = nome_atualizar

    nova_receita = f"Nome: {nome_atualizar}\nTipo de prato: {tipo_prato_novo}\nPaís de origem: {pais_origem_novo}\nIngredientes: {ingredientes_novos}\nModo de preparo: {modo_preparo_novo}\n{separador}"

    with open("receitas.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
    with open("receitas.txt", "w", encoding="utf-8") as arquivo:
        i = 0
        while i < len(linhas):
            if nome_atualizar in linhas[i]:
                i += 6
            else:
                arquivo.write(linhas[i])
                i += 1
    with open("receitas.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
    with open("receitas.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(nova_receita)
        arquivo.write("\n")

    print(f"A receita '{nome_atualizar}' foi atualizada com sucesso.\n")
    input("Pressione ENTER para continuar")

def lista_favoritos():
    os.system('cls')
    while True:
        os.system('cls')
        resposta = input("Opções de Entrada:\n\n1 - Adicionar uma receita aos favortios\n2 - Remover uma receita aos favortios\n3 - Visualizar lista de favoritos\n4 - Voltar pro menu\n\nDigite o numero referente a operação desejada: ")
        if resposta == '1':
            os.system('cls')
            nome_favoritar = input("Digite receita que deseja favoritar: ").lower()
            if nome_favoritar not in nomes:
                print("\nReceita inexistente.")
                input("\nPressione ENTER para continuar")
                continue
            favoritos.append(nome_favoritar)
            print("\nReceita adicionada aos favoritos com sucesso!\n")
            input("Pressione ENTER para continuar")
        if resposta == '2':
            os.system('cls')
            nome_remover = input("Digite receita que deseja remover dos favoritos: ").lower()
            if nome_remover not in nomes:
                print("\nReceita inexistente.")
                input("\nPressione ENTER para continuar")
                continue
            favoritos.remove(nome_remover)
            print("\nReceita removida dos favoritos com sucesso!\n")
            input("Pressione ENTER para continuar")
        if resposta == '3':
            with open("receitas.txt", "r", encoding="utf-8") as arquivo:
                print()
                linhas = arquivo.readlines()
            for favorito in favoritos:
                i = 0
                while i < len(linhas):
                    if favorito in linhas[i]:
                        print(f"Nome: {favorito}")
                        for j in range(i + 1, min(i + 6, len(linhas))):  
                            print(linhas[j], end='')
                        break
                    i += 1
            input("\nPressione ENTER para continuar")
        if resposta == '4':
            break

def receitas_aleatorias():
    os.system('cls')
    recipe_random = aleatorias[random.randint(0, len(aleatorias) - 1)]
    with open("aleatorias.txt", "r", encoding="utf-8") as arquivo:
            print()
            linhas = arquivo.readlines()
            i = 0
            while i < len(linhas):
                if recipe_random in linhas[i]:
                    os.system("cls")
                    print(f"Receita aleatoria:\n\nNome: {recipe_random}")
                    for j in range(i + 1, min(i + 6, len(linhas))):  
                        print(linhas[j], end='')
                    break
                i += 1
    input("\nPressione ENTER para continuar")

def linha_para_lista(linha):
    lista_str = linha.strip()
    if lista_str == "[]":
        return []
    else:
        return lista_str.strip('[]').replace("'", "").split(', ')

aleatorias = (
    "sopa de legumes colorida",
    "frango assado com limão e ervas",
    "risoto de cogumelos",
    "tacos de peixe com manga",
    "curry de grão de bico com espinafre",
    "salada grega com queijo feta",
    "panquecas americanas com mirtilos",
    "guacamole com chips de batata doce",
    "bolo de chocolate com cobertura de ganache",
    "smoothie de morango e banana"
)

with open("listas.txt", "r") as file:
    linhas = file.readlines()

nomes = linha_para_lista(linhas[0])
favoritos = linha_para_lista(linhas[1])

while True: 
    os.system('cls')
    opcao = input("Opções de Entrada:\n\n1 - Funções Básicas (Adicionar, Remover, Visualizar e Atualizar)\n2 - Funções especiais (Filtrar por país, Lista de favoritos, Receitas aleatórias e Filtrar por tipo de prato)\n3 - Finalizar\n\nDigite o numero referente a operação desejada: ")
    if opcao == '1':
        os.system('cls')
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
        os.system('cls')
        opcao = input("Opções de Entrada:\n\n1 - Filtrar por país \n2 - Favoritos\n3 - Receitas aleatórias\n4 - Filtrar por tipo de prato\n5 - Voltar para início\n\nDigite o numero referente a operação desejada: ")
        if opcao == '1':
            filtrar_pais()
        elif opcao == '2':
            lista_favoritos()
        elif opcao == '3':
            receitas_aleatorias()
        elif opcao == '4':
            filtar_prato()
        elif opcao == '5':
            continue
    elif opcao == '3':
        nomesstr = str(nomes)
        favoritosstr = str(favoritos)
        with open("listas.txt", "w") as file:
            file.writelines(linhas[2:])
        with open("listas.txt", "a") as file:
            file.write(nomesstr)
            file.write("\n")
            file.write(favoritosstr)
            file.write("\n")
        break