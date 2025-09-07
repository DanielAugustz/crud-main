# CRUD com FastAPI e MongoDB

Esse projeto é um exemplo simples de como usar o **FastAPI** junto com o **MongoDB** para criar uma API que faz as operações básicas de banco de dados:  
**Criar, Ler, Atualizar e Deletar (CRUD)**.

Foi desenvolvido como atividade prática da disciplina de Banco de Dados.

---

O que foi usado
- **Python 3.11**
- **FastAPI** (framework web)
- **Uvicorn** (servidor ASGI)
- **MongoDB** (banco NoSQL)
- **PyMongo** (driver para conectar no Mongo)

Tudo isso rodando dentro de containers **Docker**.

---

Estrutura do projeto
crud-main/
│── app/
│ ├── main.py # Ponto de entrada da aplicação
│ ├── database.py # Conexão com o MongoDB
│ ├── models.py # Modelos de dados (Aluno)
│ └── routers/
│ └── alunos.py # Rotas CRUD de alunos
│
│── docker-compose.yml # Orquestra os containers
│── Dockerfile # Cria a imagem da aplicação
│── requirements.txt # Dependências do Python
│── README.md # Este arquivo :)

Como rodar o projeto
clone
git clone https://github.com/DanielAugustz/crud-main.git
cd crud-main

Subir containers
docker-compose up --build

Acesse a API
API rodando em: http://localhost:8000
Documentação Swagger: http://localhost:8000/docs

Criados / Disponiveis
POST /alunos/ → cria um aluno
GET /alunos/ → lista todos os alunos
PUT /alunos/{id} → atualiza os dados de um aluno
DELETE /alunos/{id} → remove um aluno
