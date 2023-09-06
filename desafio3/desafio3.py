from flask import Flask, request, jsonify

app = Flask(__name__)

pessoas = []

class Pessoa:
    def __init__(self, nome,descricao, cpf,programa,animador,imagem):
        self.nome = nome
        self.descricao = descricao
        self.cpf = cpf
        self.programa = programa
        self.animador = animador
        self.imagem = imagem


@app.route("/characters/", methods=['POST'])                                                        
def criar_pessoa():
    data = request.get_json()
    nome = data.get('nome')
    descricao = data.get('descricao')
    cpf = data.get('cpf')
    programa = data.get('programa')
    animador = data.get('animador')
    imagem = data.get('imagem')

    nova_pessoa = Pessoa(nome,descricao, cpf,programa,animador,imagem)
    pessoas.append(nova_pessoa)    

    return jsonify({'message': 'Pessoa criada com sucesso'}), 201


@app.route("/characters/")
def listar_pessoas():
    pessoas_data = [{'nome': pessoa.nome, 'descricao': pessoa.descricao, 'cpf': pessoa.cpf,'programa':pessoa.programa,'animador':pessoa.animador,'imagem':pessoa.imagem} for pessoa in pessoas]
    return jsonify(pessoas_data)


if __name__ == "__main__":
    app.run(debug=True)
