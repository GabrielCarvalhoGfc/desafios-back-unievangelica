from flask import Flask, request, jsonify

app = Flask(__name__)

pessoas = []

class Pessoa:
    def __init__(self, nome, descricao, cpf):
        self.nome = nome
        self.descricao = descricao
        self.cpf = cpf


@app.route("/characters/", methods=['POST'])                             
def criar_pessoa():
    data = request.get_json()
    nome = data.get('nome')
    descricao = data.get('descricao')
    cpf = data.get('cpf')

    nova_pessoa = Pessoa(nome,descricao, cpf)
    pessoas.append(nova_pessoa)    

    return jsonify({'message': 'Pessoa criada com sucesso'}), 201


@app.route("/characters/")
def listar_pessoas():
    pessoas_data = [{'nome': pessoa.nome, 'descricao': pessoa.descricao, 'cpf': pessoa.cpf} for pessoa in pessoas]
    return jsonify(pessoas_data)


if __name__ == "__main__":
    app.run(debug=True)
