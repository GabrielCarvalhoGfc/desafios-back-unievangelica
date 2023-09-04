class Pessoa:
    def __init__(self, nome, sexo, cpf):
        self.nome = nome
        self.sexo = sexo
        self.cpf = cpf

if __name__ == "__main__":
    pessoa1= Pessoa("GABRIEL","MASCULINO","123456")
    print(pessoa1.nome,pessoa1.sexo,pessoa1.cpf)
