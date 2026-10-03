from datetime import datetime, date

valor = float(input("Digite o valor: "))
data_vencimento_str = input("Digite a data de vencimento (DD/MM/AAAA): ")

data_vencimento = datetime.strptime(data_vencimento_str, "%d/%m/%Y").date()
hoje = date.today()

dias_atraso = (hoje - data_vencimento).days

if dias_atraso > 0:
    juros = valor * 0.025 * dias_atraso
    valor_total = valor + juros
    print(f"Dias em atraso: {dias_atraso}")
    print(f"Valor dos juros: R$ {juros:.2f}")
    print(f"Valor total com juros: R$ {valor_total:.2f}")
else:
    print("O título não está em atraso.")
    print(f"Valor dos juros: R$ 0.00")
    print(f"Valor total: R$ {valor:.2f}")
