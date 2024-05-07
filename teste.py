def adicionar_receita():
    nome = input("Digite o nome da receita: ") # Adiciona o nome da receita
    pais_origem = input("Digite o país de origem da receita: ") # Adiciona o país de origem
    ingredientes = input("Digite os ingredientes da receita (separados por vírgula): ") # Adiciona os Ingredientes
    modo_preparo = input("Digite o modo de preparo da receita: ") # Adiciona o passo a passo
    # Formatação da receita
    receita = f"Nome: {nome}\nPaís de origem: {pais_origem}\nIngredientes: {ingredientes}\nModo de preparo: {modo_preparo}\n------------------------------------------"
    # Adicionando a receita ao arquivo
    with open("receitas.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(receita)
        arquivo.write("\n")
    print("Receita adicionada com sucesso!") # Retorna ao usuario uma mensagem de sucesso

# Menu Interativo   
while True: # Loop While para o usuario ter a possibilidade de realizar outra função
    opcao = input("Opções de Entrada:\n1 - Adicionar \n2 - Remover\n3 - Atualizar\n4 - Visualizar\n5 - Filtrar para o país\n")

    if opcao == '1':
        adicionar_receita() # Chama a função de 'Adicionar Receita'
   
