from flask import Flask, request, jsonify

app = Flask(__name__)

Characters = []

class Characters:
    def __init__(self, nome,descricao,programa,animador,imagem):
        self.nome = nome
        self.descricao = descricao
        self.programa = programa
        self.animador = animador
        self.imagem = imagem


@app.route("/characters/", methods=['POST'])                                                        
def create_Characters():
    data = crequest.get_json()
    nome = data.get('nome')
    descricao = data.get('descricao')
    programa = data.get('programa')
    animador = data.get('animador')
    imagem = data.get('imagem')

    new_characters = Pessoa(nome,descricao,programa,animador,imagem)
    Characters.append(nova_pessoa)    

    return jsonify({'message': 'Pessoa criada com sucesso'}), 201


@app.route("/characters/")
def listar_pessoas():
    data_Characters = [{'nome': pessoa.nome, 'descricao': pessoa.descricao,'programa':pessoa.programa,'animador':pessoa.animador,'imagem':pessoa.imagem} for pessoa in pessoas]
    return jsonify(pessoas_data)


if __name__ == "__main__":
    app.run(debug=True)
