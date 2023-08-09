class Estudante:
    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso
        
    def apresentar(self):
        mensagem = f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e estou cursando {self.curso}."
        print(mensagem)


estudante1 = Estudante("João", 20, "Engenharia")
estudante2 = Estudante("Maria", 22, "Medicina")
estudante3 = Estudante("Pedro", 19, "Direito")


estudante1.apresentar()
estudante2.apresentar()
estudante3.apresentar()