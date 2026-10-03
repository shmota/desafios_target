from log_controller import Log
import json

class Estoque:

    def __init__(self, caminho_arquivo = ""):
        self.estoque = self.ler_estoque(caminho_arquivo)
        self.caminho_arquivo = caminho_arquivo
        self.logs = Log()

    def ler_estoque(self, caminho_arquivo):
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            dados = json.load(f)

        return dados["estoque"]

    def buscar_produto(self, codigoProduto):
        for produto in self.estoque:
            if produto["codigoProduto"] == codigoProduto:
                return produto
        
        return None

    def menu_dados(self):

        print("-" * 20)

        codigoProduto = int(input("Digite o codigo do produto: "))

        produto = self.buscar_produto(codigoProduto)

        if not produto:
            print("Produto não encontrado!")
            return

        print(f"Estoque atual: {produto["descricaoProduto"]} - {produto["estoque"]} unidades \n")
                
        quantidade = int(input("Digite a quantidade: "))

        return produto, quantidade

    def registrar_saida(self):

        produto, quantidade = self.menu_dados()
        
        if produto["estoque"] >= quantidade:
            produto["estoque"]  -= quantidade
            self.salvar_estoque()
            self.logs.registrar_acao(
                f"Descrição: saida de [{produto["codigoProduto"]}]{produto["descricaoProduto"]}, quantidade: {quantidade}"
            )
            print(f"Produto: {produto["descricaoProduto"]}, quantidade final: {produto["estoque"]}")
            
        else:
            print("Estoque insuficiente!")

    def registrar_entrada(self):

        produto, quantidade = self.menu_dados()
        
        produto["estoque"]  += quantidade
        self.salvar_estoque()
        self.logs.registrar_acao(
            f"Descrição: entrada de [{produto["codigoProduto"]}]{produto["descricaoProduto"]}, quantidade: {quantidade}"
        )

        print(f"Produto: {produto["descricaoProduto"]}, quantidade final: {produto["estoque"]}")


    def salvar_estoque(self):
        with open(self.caminho_arquivo, "w", encoding="utf-8") as f:
            json.dump({"estoque": self.estoque}, f, indent=4, ensure_ascii=False)