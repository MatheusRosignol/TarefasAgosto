class Estudante:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def apresentar(self):
        mensagem = f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."
        print(mensagem)

# Exemplo de uso da classe Estudante
estudante1 = Estudante("João", 20)
estudante1.apresentar()

estudante2 = Estudante("Maria", 22)
estudante2.apresentar()