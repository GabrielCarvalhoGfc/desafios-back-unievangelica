class Pessoa:
    def __init__(self, nome,descricao,programa,animador,imagem):
        self.nome = nome
        self.descricao = descricao
        self.programa = programa
        self.animador = animador
        self.imagem = imagem

if __name__ == "__main__":
    pessoa1= Pessoa("GABRIEL","MASCULINO","FILME,DISNEY,imagem")
    print(pessoa1.nome,pessoa1.descricao,pessoa1.programa,pessoa1.animador,pessoa1.imagem)
