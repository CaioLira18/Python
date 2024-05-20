import os  # Importa o módulo os, que permite interagir com o sistema operacional.
import random  # Importa o módulo random, que fornece funções para geração de números aleatórios.

def adicionar_receita():
    os.system('cls')  # Limpa a tela do console.
    nome = input("Digite o nome da receita: ").lower()  # Solicita o nome da receita e converte para minúsculas.
    if nome in nomes:  # Verifica se a receita já está na lista de nomes.
        os.system('cls')  # Limpa a tela do console.
        print("A receita já foi adicionada.\n")  # Informa que a receita já foi adicionada.
        input("Pressione ENTER para continuar")  # Espera o usuário pressionar ENTER.
        return  # Sai da função.
    tipo_prato = input("Digite o tipo do prato (Sobremesa, Salada, Aperitivo etc): ").lower()  # Solicita o tipo de prato e converte para minúsculas.
    pais_origem = input("Digite o país de origem da receita: ").lower()  # Solicita o país de origem e converte para minúsculas.
    ingredientes = input("Digite os ingredientes da receita (separados por vírgula): ").lower()  # Solicita os ingredientes e converte para minúsculas.
    modo_preparo = input("Digite o modo de preparo da receita: ").lower()  # Solicita o modo de preparo e converte para minúsculas.
    separador = "----------"  # Define um separador.

    os.system('cls')  # Limpa a tela do console.

    receita = f"Nome: {nome}\nTipo de prato: {tipo_prato}\nPaís de origem: {pais_origem}\nIngredientes: {ingredientes}\nModo de preparo: {modo_preparo}\n{separador}"  # Cria a string da receita formatada.

    nomes.append(nome)  # Adiciona o nome da receita à lista de nomes.

    with open("receitas.txt", "a", encoding="utf-8") as arquivo:  # Abre o arquivo receitas.txt para escrita (modo append).
        arquivo.write(receita)  # Escreve a receita no arquivo.
        arquivo.write("\n")  # Adiciona uma nova linha ao arquivo.
    print("Receita adicionada com sucesso!\n")  # Informa que a receita foi adicionada com sucesso.
    input("Pressione ENTER para continuar")  # Espera o usuário pressionar ENTER.

def remover_receita():
    os.system('cls')  # Limpa a tela do console.

    nome_receita = input("Digite o nome da receita que deseja remover: ").lower()  # Solicita o nome da receita a ser removida e converte para minúsculas.

    if nome_receita in nomes:  # Verifica se a receita está na lista de nomes.
        nomes.remove(nome_receita)  # Remove a receita da lista de nomes.
        if nome_receita in favoritos:  # Verifica se a receita está na lista de favoritos.
            favoritos.remove(nome_receita)  # Remove a receita da lista de favoritos.

    with open("receitas.txt", "r", encoding="utf-8") as arquivo:  # Abre o arquivo receitas.txt para leitura.
        linhas = arquivo.readlines()  # Lê todas as linhas do arquivo.

    removido = False  # Define uma variável para indicar se a receita foi removida.

    with open("receitas.txt", "w", encoding="utf-8") as arquivo:  # Abre o arquivo receitas.txt para escrita.
        i = 0
        while i < len(linhas):  # Itera sobre as linhas do arquivo.
            if nome_receita in linhas[i]:  # Verifica se o nome da receita está na linha atual.
                removido = True  # Define a variável removido como True.
                i += 6  # Pula as próximas 6 linhas (presumivelmente a receita inteira).
                print(f"\nA receita '{nome_receita}' foi removida.\n")  # Informa que a receita foi removida.
            else:
                arquivo.write(linhas[i])  # Escreve a linha no arquivo.
                i += 1
    if not removido:  # Se a receita não foi encontrada.
        print(f"\nA receita '{nome_receita}' não foi encontrada.\n")  # Informa que a receita não foi encontrada.
    input("Pressione ENTER para continuar")  # Espera o usuário pressionar ENTER.

def visualizar_receita():
    os.system('cls')  # Limpa a tela do console.
    resposta = input("Opções de Entrada:\n\n1 - visualizar todas as receitas\n2 - visualizar uma receita específica\n\nDigite o numero referente a operação desejada: ")  # Solicita uma opção do usuário.

    if resposta == '1':  # Se o usuário escolheu visualizar todas as receitas.
        os.system('cls')  # Limpa a tela do console.
        with open("receitas.txt", "r", encoding="utf-8") as arquivo:  # Abre o arquivo receitas.txt para leitura.
            for linha in arquivo:  # Itera sobre as linhas do arquivo.
                print(linha.strip())  # Imprime a linha sem espaços extras.

    elif resposta == '2':  # Se o usuário escolheu visualizar uma receita específica.
        os.system('cls')  # Limpa a tela do console.
        nome_receita = input("Qual receita você deseja visualizar: ").lower()  # Solicita o nome da receita e converte para minúsculas.
        with open("receitas.txt", "r", encoding="utf-8") as arquivo:  # Abre o arquivo receitas.txt para leitura.
            print()
            linhas = arquivo.readlines()  # Lê todas as linhas do arquivo.
            i = 0
            while i < len(linhas):  # Itera sobre as linhas do arquivo.
                if nome_receita in linhas[i]:  # Verifica se o nome da receita está na linha atual.
                    os.system("cls")  # Limpa a tela do console.
                    print(f"Receita encontrada!\n\nNome: {nome_receita}")
                    for j in range(i + 1, min(i + 6, len(linhas))):  # Imprime as próximas 5 linhas (presumivelmente a receita inteira).
                        print(linhas[j], end='')
                    break
                i += 1
            else:
                print(f"\nA receita '{nome_receita}' não foi encontrada.")  # Informa que a receita não foi encontrada.
    input("\nPressione ENTER para continuar")  # Espera o usuário pressionar ENTER.

def filtrar_pais():
    os.system('cls')  # Limpa a tela do console.
    pais = input("Digite o país que você deseja filtar: ").lower()  # Solicita o nome do país e converte para minúsculas.
    with open("receitas.txt", "r", encoding="utf-8") as arquivo:  # Abre o arquivo receitas.txt para leitura.
        linhas = arquivo.readlines()  # Lê todas as linhas do arquivo.
        i = 0
        encontrou_pais = False  # Define uma variável para indicar se o país foi encontrado.
        while i < len(linhas):  # Itera sobre as linhas do arquivo.
            if pais in linhas[i]:  # Verifica se o nome do país está na linha atual.
                encontrou_pais = True  # Define a variável encontrou_pais como True.
                print(f"\nPaís encontrado!\n")
                for j in range(i - 2, i + 4):  # Imprime as linhas relevantes ao país encontrado.
                    print(linhas[j], end='')
            i += 1
        if not encontrou_pais:  # Se o país não foi encontrado.
            print(f"\nO {pais} não foi encontrado.")  # Informa que o país não foi encontrado.
    input("\nPressione ENTER para continuar")  # Espera o usuário pressionar ENTER.

def filtar_prato():
    os.system('cls')  # Limpa a tela do console.
    tipos_prato = input("Digite o tipo de prato que você deseja filtrar: ").lower()  # Solicita o tipo de prato e converte para minúsculas.
    with open("receitas.txt", "r", encoding="utf-8") as arquivo:  # Abre o arquivo receitas.txt para leitura.
        linhas = arquivo.readlines()  # Lê todas as linhas do arquivo.
        i = 0
        encontrou_prato = False  # Define uma variável para indicar se o tipo de prato foi encontrado.
        while i < len(linhas):  # Itera sobre as linhas do arquivo.
            if tipos_prato in linhas[i]:  # Verifica se o tipo de prato está na linha atual.
                encontrou_prato = True  # Define a variável encontrou_prato como True.
                print(f"\nTipo de prato encontrado!\n")
                for j in range(i - 1, i + 5):  # Imprime as linhas relevantes ao tipo de prato encontrado.
                    print(linhas[j], end='')
            i += 1
        if not encontrou_prato:  # Se o tipo de prato não foi encontrado.
            print(f"\nO {tipos_prato} não foi encontrado.")  # Informa que o tipo de prato não foi encontrado.
    input("\nPressione ENTER para continuar")

def atualizar_receita():
    os.system('cls')  # Limpa a tela do console
    nome_atualizar = input("Digite o nome da receita que deseja atualizar: ").lower()  # Pede ao usuário o nome da receita a ser atualizada e converte para minúsculas

    if nome_atualizar not in nomes:  # Verifica se o nome não está na lista de receitas
        print(f"\nA receita '{nome_atualizar}' não foi encontrada.")  # Informa que a receita não foi encontrada
        return  # Sai da função

    # Pede ao usuário os novos dados da receita e converte para minúsculas
    tipo_prato_novo = input("\nDigite o novo tipo do prato (Sobremesa, Salada, Aperitivo etc): ").lower()
    pais_origem_novo = input("Digite o novo país de origem da receita: ").lower()
    ingredientes_novos = input("Digite os novos ingredientes da receita (separados por vírgula): ").lower()
    modo_preparo_novo = input("Digite o novo modo de preparo da receita: ").lower()
    separador = "----------"  # Define um separador para a receita

    os.system('cls')  # Limpa a tela do console novamente

    indice_receita = nomes.index(nome_atualizar)  # Obtém o índice da receita na lista de nomes
    nomes[indice_receita] = nome_atualizar  # Atualiza o nome da receita na lista de nomes

    # Cria uma string formatada com os novos dados da receita
    nova_receita = f"Nome: {nome_atualizar}\nTipo de prato: {tipo_prato_novo}\nPaís de origem: {pais_origem_novo}\nIngredientes: {ingredientes_novos}\nModo de preparo: {modo_preparo_novo}\n{separador}"

    # Abre o arquivo de receitas para leitura e armazena as linhas em uma lista
    with open("receitas.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
    # Abre o arquivo de receitas para escrita, sobrescrevendo o conteúdo anterior
    with open("receitas.txt", "w", encoding="utf-8") as arquivo:
        i = 0
        while i < len(linhas):
            if nome_atualizar in linhas[i]:  # Verifica se a linha contém o nome da receita a ser atualizada
                i += 6  # Pula as próximas 6 linhas (que contêm a receita antiga)
            else:
                arquivo.write(linhas[i])  # Escreve a linha no arquivo
                i += 1
    # Abre o arquivo de receitas novamente para leitura e armazena as linhas atualizadas
    with open("receitas.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
    # Abre o arquivo de receitas para adicionar a nova receita
    with open("receitas.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(nova_receita)  # Escreve a nova receita no arquivo
        arquivo.write("\n")  # Adiciona uma nova linha

    print(f"A receita '{nome_atualizar}' foi atualizada com sucesso.\n")  # Informa que a receita foi atualizada com sucesso
    input("Pressione ENTER para continuar")  # Espera o usuário pressionar ENTER para continuar

def lista_favoritos():
    os.system('cls')  # Limpa a tela do console
    while True:
        os.system('cls')  # Limpa a tela do console novamente
        resposta = input("Opções de Entrada:\n\n1 - Adicionar uma receita aos favoritos\n2 - Remover uma receita dos favoritos\n3 - Visualizar lista de favoritos\n4 - Voltar pro menu\n\nDigite o numero referente a operação desejada: ")  # Pede ao usuário uma opção

        if resposta == '1':  # Se a opção for adicionar uma receita aos favoritos
            os.system('cls')  # Limpa a tela do console
            nome_favoritar = input("Digite receita que deseja favoritar: ").lower()  # Pede o nome da receita e converte para minúsculas
            if nome_favoritar not in nomes:  # Verifica se o nome da receita não está na lista de nomes
                print("\nReceita inexistente.")  # Informa que a receita não existe
                input("\nPressione ENTER para continuar")  # Espera o usuário pressionar ENTER para continuar
                continue  # Continua o loop
            favoritos.append(nome_favoritar)  # Adiciona a receita aos favoritos
            print("\nReceita adicionada aos favoritos com sucesso!\n")  # Informa que a receita foi adicionada aos favoritos
            input("Pressione ENTER para continuar")  # Espera o usuário pressionar ENTER para continuar

        if resposta == '2':  # Se a opção for remover uma receita dos favoritos
            os.system('cls')  # Limpa a tela do console
            nome_remover = input("Digite receita que deseja remover dos favoritos: ").lower()  # Pede o nome da receita e converte para minúsculas
            if nome_remover not in nomes:  # Verifica se o nome da receita não está na lista de nomes
                print("\nReceita inexistente.")  # Informa que a receita não existe
                input("\nPressione ENTER para continuar")  # Espera o usuário pressionar ENTER para continuar
                continue  # Continua o loop
            favoritos.remove(nome_remover)  # Remove a receita dos favoritos
            print("\nReceita removida dos favoritos com sucesso!\n")  # Informa que a receita foi removida dos favoritos
            input("Pressione ENTER para continuar")  # Espera o usuário pressionar ENTER para continuar

        if resposta == '3':  # Se a opção for visualizar a lista de favoritos
            with open("receitas.txt", "r", encoding="utf-8") as arquivo:  # Abre o arquivo de receitas para leitura
                print()  # Imprime uma linha em branco
                linhas = arquivo.readlines()  # Lê todas as linhas do arquivo
            for favorito in favoritos:  # Para cada receita nos favoritos
                i = 0
                while i < len(linhas):
                    if favorito in linhas[i]:  # Verifica se a linha contém o nome da receita favorita
                        print(f"Nome: {favorito}")  # Imprime o nome da receita favorita
                        for j in range(i + 1, min(i + 6, len(linhas))):  # Imprime as próximas 5 linhas (dados da receita)
                            print(linhas[j], end='')
                        break  # Sai do loop
                    i += 1
            input("\nPressione ENTER para continuar")  # Espera o usuário pressionar ENTER para continuar

        if resposta == '4':  # Se a opção for voltar para o menu
            break  # Sai do loop

def receitas_aleatorias():
    os.system('cls')  # Limpa a tela do console
    recipe_random = aleatorias[random.randint(0, len(aleatorias) - 1)]  # Seleciona uma receita aleatória da lista
    with open("aleatorias.txt", "r", encoding="utf-8") as arquivo:  # Abre o arquivo de receitas aleatórias para leitura
        print()  # Imprime uma linha em branco
        linhas = arquivo.readlines()  # Lê todas as linhas do arquivo
        i = 0
        while i < len(linhas):
            if recipe_random in linhas[i]:  # Verifica se a linha contém o nome da receita aleatória
                os.system("cls")  # Limpa a tela do console
                print(f"Receita aleatoria:\n\nNome: {recipe_random}")  # Imprime o nome da receita aleatória
                for j in range(i + 1, min(i + 6, len(linhas))):  # Imprime as próximas 5 linhas (dados da receita)
                    print(linhas[j], end='')
                break  # Sai do loop
            i += 1
    input("\nPressione ENTER para continuar")  # Espera o usuário pressionar ENTER para continuar

def linha_para_lista(linha):
    lista_str = linha.strip()  # Remove espaços em branco no início e no fim da linha
    if lista_str == "[]":  # Verifica se a linha é uma lista vazia
        return []  # Retorna uma lista vazia
    else:
        return lista_str.strip('[]').replace("'", "").split(', ')  # Remove colchetes, apóstrofos e divide a string em uma lista

# Lista de receitas aleatórias
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
    linhas = file.readlines()  # Lê todas as linhas do arquivo e armazena na lista 'linhas'

# Converte a primeira linha do arquivo em uma lista de nomes
nomes = linha_para_lista(linhas[0])
# Converte a segunda linha do arquivo em uma lista de favoritos
favoritos = linha_para_lista(linhas[1])

# Inicia um loop infinito para o menu principal
while True:
    os.system('cls')  # Limpa a tela do console
    # Exibe o menu principal e solicita a opção do usuário
    opcao = input("Opções de Entrada:\n\n1 - Funções Básicas (Adicionar, Remover, Visualizar e Atualizar)\n2 - Funções especiais (Filtrar por país, Lista de favoritos, Receitas aleatórias e Filtrar por tipo de prato)\n3 - Finalizar\n\nDigite o numero referente a operação desejada: ")

    if opcao == '1':  # Se o usuário escolheu Funções Básicas
        os.system('cls')  # Limpa a tela do console
        # Exibe o sub-menu de Funções Básicas e solicita a opção do usuário
        opcao = input("Opções de Entrada:\n\n1 - Adicionar \n2 - Remover\n3 - Atualizar\n4 - Visualizar\n5 - Voltar para início\n\nDigite o numero referente a operação desejada: ")
        if opcao == '1':  # Se o usuário escolheu Adicionar
            adicionar_receita()  # Chama a função para adicionar receita
        elif opcao == '2':  # Se o usuário escolheu Remover
            remover_receita()  # Chama a função para remover receita
        elif opcao == '3':  # Se o usuário escolheu Atualizar
            atualizar_receita()  # Chama a função para atualizar receita
        elif opcao == '4':  # Se o usuário escolheu Visualizar
            visualizar_receita()  # Chama a função para visualizar receita
        elif opcao == '5':  # Se o usuário escolheu Voltar para início
            continue  # Retorna ao menu principal

    elif opcao == '2':  # Se o usuário escolheu Funções Especiais
        os.system('cls')  # Limpa a tela do console
        # Exibe o sub-menu de Funções Especiais e solicita a opção do usuário
        opcao = input("Opções de Entrada:\n\n1 - Filtrar por país \n2 - Favoritos\n3 - Receitas aleatórias\n4 - Filtrar por tipo de prato\n5 - Voltar para início\n\nDigite o numero referente a operação desejada: ")
        if opcao == '1':  # Se o usuário escolheu Filtrar por país
            filtrar_pais()  # Chama a função para filtrar receitas por país
        elif opcao == '2':  # Se o usuário escolheu Favoritos
            lista_favoritos()  # Chama a função para listar os favoritos
        elif opcao == '3':  # Se o usuário escolheu Receitas aleatórias
            receitas_aleatorias()  # Chama a função para exibir receitas aleatórias
        elif opcao == '4':  # Se o usuário escolheu Filtrar por tipo de prato
            filtar_prato()  # Chama a função para filtrar receitas por tipo de prato
        elif opcao == '5':  # Se o usuário escolheu Voltar para início
            continue  # Retorna ao menu principal

    elif opcao == '3':  # Se o usuário escolheu Finalizar
        nomesstr = str(nomes)  # Converte a lista de nomes em uma string
        favoritosstr = str(favoritos)  # Converte a lista de favoritos em uma string
        with open("listas.txt", "w") as file:  # Abre o arquivo "listas.txt" em modo de escrita (sobrescreve o conteúdo)
            file.writelines(linhas[2:])  # Escreve as linhas restantes (a partir da terceira linha)
        with open("listas.txt", "a") as file:  # Abre o arquivo "listas.txt" em modo de adição
            file.write(nomesstr)  # Adiciona a lista de nomes
            file.write("\n")  # Adiciona uma nova linha
            file.write(favoritosstr)  # Adiciona a lista de favoritos
            file.write("\n")  # Adiciona uma nova linha
        break  # Encerra o loop e finaliza o programa
