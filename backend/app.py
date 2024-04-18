import os
from flask import Flask, request, jsonify, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///academia.db'  # Caminho para o banco de dados
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)

# Modelo de usuário
class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)

    def __repr__(self):
        return f"Aluno(nome='{self.nome}', email='{self.email}')"

# Função para criar o banco de dados, se ainda não existir
def create_database():
    with app.app_context():
        if not os.path.exists('academia.db'):
            db.create_all()
            print("Banco de dados criado com sucesso!")
        else:
            print("Banco de dados já existe, não é necessário criar novamente.")

@app.route('/')
def homepage():
    return 'Gerenciamento de Alunos'

# Rota para listar todos os usuários
@app.route('/alunos', methods=['GET'])
def get_alunos():
    alunos = Aluno.query.all()
    return jsonify([{'id': aluno.id, 'nome': aluno.nome, 'email': aluno.email} for aluno in alunos])

# Rota para criar um novo usuário
@app.route('/criar_aluno', methods=['POST'])
def criar_aluno():
    data = request.get_json()
    nome = data.get('nome')
    email = data.get('email')
    if nome and email:
        novo_aluno = Aluno(nome=nome, email=email)
        db.session.add(novo_aluno)
        db.session.commit()
        return jsonify({'id': novo_aluno.id, 'nome': novo_aluno.nome, 'email': novo_aluno.email}), 201
    else:
        return 'Nome e email são obrigatórios', 400
    
# Rota para atualizar um usuário existente
@app.route('/alunos/<int:aluno_id>', methods=['PUT'])
def update_user(aluno_id):
    data = request.get_json()
    nome = data.get('nome')
    email = data.get('email')
    if nome and email:
        aluno = Aluno.query.get(aluno_id)
        if aluno:
            aluno.nome = nome
            aluno.email = email
            db.session.commit()
            return jsonify({'id': aluno.id, 'nome': aluno.nome, 'email': aluno.email}), 200
        else:
            return 'Aluno não encontrado', 404
    else:
        return 'Nome e email são obrigatórios', 400

# Rota para deletar um usuário existente
@app.route('/alunos/<int:aluno_id>', methods=['DELETE'])
def deletar_aluno(aluno_id):
    aluno = Aluno.query.get(aluno_id)
    if aluno:
        db.session.delete(aluno)
        db.session.commit()
        return 'Aluno deletado com sucesso', 200
    else:
        return 'Aluno não encontrado', 404

# Rota para carregar o arquivo YAML do Swagger
@app.route('/swagger.yaml')
def swagger_yaml():
    return send_file('swagger.yaml')

# Configuração do Swagger UI
SWAGGER_URL = '/api/docs'
API_URL = '/swagger.yaml'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "Gerenciamento de Alunos API"}
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    create_database()
    app.run(debug=True)
