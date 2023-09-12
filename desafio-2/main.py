# classificar o personagem
class Characters:
    def __init__(self, nome,descricao,programa,animador,imagem):
        self.nome = nome
        self.descricao = descricao
        self.programa = programa
        self.animador = animador
        self.imagem = imagem

#executar a classe
if __name__ == "__main__":
    Characters1= Characters("GABRIEL","MASCULINO","FILME,DISNEY,imagem")
    print(pessoa1.nome,Characters1.descricao,Characters1.program,Characters1.animador,Characters1.imagem)
