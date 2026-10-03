import json

if __name__ == "__main__":

    with open("desafio-1/data.json", "r", encoding="utf-8") as f:
        dados = json.load(f)

    metricas = {}

    for venda in dados['vendas']:

        valor = venda['valor']

        if venda["vendedor"] not in metricas:
            metricas[venda["vendedor"]] = {"comissao": 0}

        if 100 <= valor < 500:
            metricas[venda["vendedor"]]['comissao'] += valor * 0.10
        
        elif valor >= 500:
            metricas[venda["vendedor"]]['comissao'] += valor * 0.50

    print("A comissão de cada vendedor foi:")
    for dados in metricas:
        print(f"{dados}: R${metricas[dados]['comissao']:.2f}")

            
    