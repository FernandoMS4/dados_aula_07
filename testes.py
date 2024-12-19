import csv
with open("desafio07.csv", mode='r', encoding='utf-8') as csvfile:
    read = csv.DictReader(csvfile)
    lista:list[dict] = []
    for i in read:
        lista.append(i)

nova2 =[]
for i in lista:
    nova = {}
    nova[i["CATEGORIA"]] = round(int(i["QUANTIDADE"]) * float(i["VALOR"]),2)
    nova2.append(nova)
print(nova2)
somas = {}
for i in nova2:
    for c, v in i.items():
        if c in somas:
            somas[c] += v
        else:
            somas[c] = v

