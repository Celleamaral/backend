# Gerenciamento de Alunos

Este é um projeto de um sistema simples de gerenciamento de alunos usando Flask, SQLAlchemy e Flask-CORS e Swagger para documentação da API.

## Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/Celleamaral/backend.git
   ```

2. Navegue até o diretório do projeto:

   ```bash
   cd nome-do-repositorio
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

## Uso
O projeto utiliza um banco de dados SQLite. Ao iniciar pela primeira vez o servidor, o banco de dados será criado automaticamente.

Execute o seguinte comando para iniciar o servidor:

```bash
python app.py
```

ou execute o arquivo **start.bat** no Windows.

O servidor estará acessível em [http://localhost:5000](http://localhost:5000).

### Rotas Disponíveis

- `GET /alunos`: Retorna todos os alunos cadastrados.
- `POST /criar_aluno`: Cria um novo aluno.
- `PUT /alunos/<int:aluno_id>`: Atualiza as informações de um aluno existente.
- `DELETE /alunos/<int:aluno_id>`: Deleta um aluno existente.
- /api/docs/: Documentação interativa da API.

## Documentação da API

A documentação interativa da API pode ser acessada em [http://localhost:5000/api/docs/](http://localhost:5000/api/docs/).

## Contribuição

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões para melhorias, por favor, abra uma issue ou envie um pull request.
