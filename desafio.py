##### DESAFIO #####

# Tarefas:

# Ler o arquivo CSV e carregar os dados.
# Processar os dados em um dicionário, onde a chave é a categoria, e o valor é uma lista de dicionários, cada um contendo informações do produto (Produto, Quantidade, Venda).
# Calcular o total de vendas (Quantidade * Venda) por categoria.
# Funções
# Ler CSV:

# Função: ler_csv
# Entrada: Nome do arquivo CSV
# Saída: Lista de dicionários com dados lidos
# Processar Dados:

# Função: processar_dados
# Entrada: Lista de dicionários
# Saída: Dicionário processado conforme descrito
# Calcular Vendas por Categoria:

# Função: calcular_vendas_categoria
# Entrada: Dicionário processado
# Saída: Dicionário com total de vendas por categoria
file_name = "desafio07.csv"
def ler_e_carregar_dados(file_name: str)->str:
    import csv
    with open(file_name, mode='r', encoding='utf-8') as csvfile:
        read = csv.DictReader(csvfile)
        lista:list[dict] = []
        for i in read:
            lista.append(i)
        return lista
    
lista = ler_e_carregar_dados(file_name)


def calcula_valor_por_categoria(list:list[dict]) ->list[dict]:
    nova2 =[]
    for i in list:
        nova = {}
        nova[i["CATEGORIA"]] = round(int(i["QUANTIDADE"]) * float(i["VALOR"]),2)
        nova2.append(nova)
    somas = {}
    for i in nova2:
        for c, v in i.items():
            if c in somas:
                somas[c] += v
            else:
                somas[c] = v
    return somas

resultado = calcula_valor_por_categoria(lista)
print(resultado)