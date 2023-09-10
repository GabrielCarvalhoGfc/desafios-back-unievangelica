API de gerenciamento de personagens
Esta é uma API básica para gerenciar personagens de uma empresa de animação. A API permite criar novos personagens ,listar os personagens existentes, atualizar as informações e deletar dados.

Pacotes Para rodar a API os seguintes pacotes são necessários:

Python 3.x
Flask
Flask-RESTX
Flask SQLAlchemy
SQLAlchemy
PyMySQL
Para executar a instação basta rodar o código a seguir:

$py pip install Flask Flask-RESTX Flask-SQLAlchemy PyMySQL
Além destes pacotes se faz necessário do uso do MySQL com um banco de dados nomeado "characters". Após isso altere a linha referente a URI do banco de dados com os atributos solicitados:

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bancodados.db'
Endpoints
POST /characters
Cria um novo personagem com as informações fornecidas no corpo da requisição.

Parâmetros:

nome: Nome do personagem (string, obrigatório)
descricao: Descrição do personagem (string, obrigatório)
imagem: Link para a imagem do personagem (string, obrigatório)
programa: Nome do programa em que o personagem aparece (string, obrigatório)
animador: Nome do animador responsável pelo personagem (string, obrigatório)
Exemplo de requisição json

 {
  "nome": "The_KID",
  "descricao": "Um grande programador back ",
  "imagem": "[https://prnt.sc/2XYEKXlpuufo]"
  "programa": "Aluno",
  "animador": "Gabriel de Carvalho"
  }
Resposta json

{
  "msg": "The_KID criado com sucesso!"
}
GET /characters
Lista todos os personagens existentes.

Resposta json

[
  {
    "id": 1,
    "nome": "The_KID",
    "descricao": "Um grande programador back ",
    "imagem": "https://prnt.sc/2XYEKXlpuufo"
    "programa": "Aluno",
    "animador": "Gabriel de Carvalho"
  }

  {
    "id": 2,
    "nome": "Aluno estudioso",
    "descricao": "Figura lendária e de difícil visualização nos tempos atuais!",
    "imagem": "noimage",
    "programa": "Aluno",
    "animador": "Gabriel de Carvalho"
  }
]
GET /characters/$id
Lista o personsagem referente ao ID solicitado

Resposta json

[
  {
    "id": 1,
    "nome": "The_KID",
    "descricao": "Um grande programador back ",
    "imagem": "https://prnt.sc/2XYEKXlpuufo",
    "programa": "Aluno",
    "animador": "Gabriel de Carvalho"
  }
]
PUT /characters/$id
Atualiza um personagem com as informações fornecidas no corpo da requisição.

Parâmetros:

ID: ID de identificação do personagem a ser atualizado
nome: Nome do personagem
descricao: Descrição do personagem
imagem: Link para a imagem do personagem
programa: Nome do programa em que o personagem aparece
animador: Nome do animador responsável pelo personagem
Exemplo de requisição json

{
  "nome": "The_KIDS",
  "descricao": "Um grande programador back ",
  "imagem": "[https://prnt.sc/2XYEKXlpuufo]",
  "programa": "Aluno",
  "animador": "Gabriel de Carvalho"
}
Resposta json

{
  'msg': 'personagem atualizado com sucesso'
}
DELETE /characters/$id
Deleta o personsagem referente ao ID solicitado

{
  'msg': 'personagem deletado com sucesso'
}
Executando a aplicação
Para executar a aplicação utilize o seguinte comando no terminal:

$ py -m flask run
A aplicação estará disponível em "http://127.0.0.1:5000".
