import datetime

class Log:

    data_atual = datetime.datetime.now()
    data_formatada = data_atual.strftime("%d-%m-%Y_%H-%M-%S")

    def __init__(self):
        self.caminho_arquivo = f"desafio-2/{self.data_formatada}-log.txt"
        self.counter = 0

    def registrar_acao(self, acao):
        with open(self.caminho_arquivo, "a", encoding="utf-8") as f:
            f.write(f"{self.counter} - {acao}\n")
            self.counter += 1
        



    