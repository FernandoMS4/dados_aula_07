
##### EXERCÍCIOS #####

#1: Calcular Média de Valores em uma Lista

lista: list = ["1","23",'34','12','40',30]
def media_de_listas(list: list) -> list:
    soma: int = 0
    for i in lista:
        if type(i) == str:
           soma += int(i)
        else:
            soma += i
    resultado = soma/len(list)
    return resultado

teste = media_de_listas(lista)
print(f"{teste:.2f}")

#2:Filtrar Dados Acima de um Limite

lista = [10,123,31,4,134,423,423,534,5665,33123,67,4433,12,331,4423,12345]
def filtra_dados_acima_num(listas: list,num:int):
    listas.sort()
    nova_lista: list = []
    for i in listas:
        if i >=num:
            nova_lista.append(i)
        else:
            pass
    return nova_lista

print(filtra_dados_acima_num(lista,200))

#3:Contar Valores Únicos em uma Lista
lista: list[int] = [1,23,1,1,1,23,34,12,40,30]
def filtrar_valores_unicos(list:list) -> list:
    return print(set(list))

print(filtrar_valores_unicos(lista))

#:Converter Celsius para Fahrenheit em uma Lista

lista:list[float] = [24.5,23.5,53.3,199.3,19,8]
def conversao_celsius_fh(listas:list[float]) -> list[float]:
    nl:list[float] = []
    for i in listas:
        valor:float = i*(9/5)+32
        #nl.append(f"{valor:.2f}")
        nl.append(round(valor,2))
    return nl

print(conversao_celsius_fh(lista))

#5: Calcular Desvio Padrão de uma Lista

lista: list[int] = [1,23,1,1,1,23,34,12,40,30]
def calcula_desvio_padrao(list:list[int])->float:
    avg = sum(list)/len(list)
    var = sum((x-avg) ** 2 for x in list) /len(list)
    return round(var **0.5,2)
print(calcula_desvio_padrao(lista))

#6: Encontrar Valores Ausentes em uma Sequência

lista: list[int] = [1,30]
def encontrar_valores_ausentes(sequencia: list[int]) -> list[int]:
    completo = set(range(min(sequencia), max(sequencia) + 1))
    return list(completo - set(sequencia))

print(encontrar_valores_ausentes(lista))