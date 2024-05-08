resposta = input("Digite 1 para visualizar todas as receitas e 2 para visualizar uma receita específica: ")
if resposta == '2':
    nome_receita = input("Qual receita você deseja visualizar: ")
    if nome_receita in nomes:
        for tipo, receitas in tipos_prato.items():
            if nome_receita in receitas:
                print(f"A receita escolhida foi {nome_receita}")
elif resposta == '1':
    with open("receitas.txt", "r", encoding="utf-8") as file:
        conteudo = file.read()
        print(conteudo)