# Documentação MIIA com modelagem de dados, documentação/implementação de API e casos/implementações de testes 

## Descrição do projeto

A MIIA é uma plataforma de estudos onde alunos fazem um conjunto de atividades para aprender e se preparar para exames. As questões podem ser de três tipos diferentes e são sorteadas a partir de um banco de questões da plataforma. 

A correção de questões discursivas e redações envolve o uso de modelos de IA que rodam em serviços de nuvem separados da aplicação devido a demandas de infraestrutura especializada. Em ambos os casos, a correção gera uma nota e um conjunto de comentários para o aluno indicando os pontos que ele acertou, errou ou não abordou, assim como sugestões de melhoria.

Toda atividade possui uma data e hora de início e uma duração, e está associada ao aluno que iniciou a atividade na plataforma. Após o término da atividade, o sistema deve fazer a correção das respostas do aluno e enviar por e-mail uma notificação da nota que foi tirada. O aluno também pode consultar no portal da MIIA o histórico de todas as atividades feitas e acessar as correções detalhadas por lá.

Este projeto é construído em **Python**, com a aplicação rodando em **FastAPI** e base de dados em **PostgreSQL**,

---

## É novo por aqui?
Entre [aqui](onboarding.md) e entenda quais os próximos passos em que você pode colaborar.

---

## Melhores práticas
Clicando [aqui](best-practices.md) você terá acesso aos nossos padrões de desenvolvimento para que a equipe tenha uma entrega fluida e de qualidade. 

---

## 🚀 Tecnologias Utilizadas

- [Docker](https://www.docker.com/)
- [Python 3.11+](https://www.python.org/downloads/release/python-3110/)
- [Framework: FastAPI](https://fastapi.tiangolo.com/)
- [Pytest](https://docs.pytest.org/en/stable/)
- [ORM: SQLAlchemy](https://www.sqlalchemy.org/)
- [Validações e Schemas: Pydantic](https://docs.pydantic.dev/latest/)

---

## 🖥️ Como Rodar Localmente

### 🔧 Requisitos mínimos

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

**Você pode verificar se já possui os requisitos com os comando abaixo:**
```bash
    docker -v
    docker compose version
```

### Passo a passo

1. **Clone o repositório**  
```bash
  git clone https://github.com/roofranklin/desafio-miia.git
  cd desafio-miia
```

2. **Rodar o projeto com Docker Compose**
```bash
  docker compose up --build
```
Esse comando vai:
- Construir a imagem da API com base no Dockerfile
- Subir o banco PostgreSQL
- Subir o serviço da API FastAPI em `http://localhost:8000`

3. **Acessar e testar a API**
Depois que o projeto estiver rodando:
- Acesse a documentação automática da API: 👉 http://localhost:8000/docs
- Você pode testar a rota de criação de atividade por lá.

4. **Testar com Pytest**
```bash
  docker compose exec web pytest
```

---

## Modelagem do banco de dados
Clique [aqui](database-model.md) para visualizar a modelagem completa.

---

## Especificação de API REST
| Método | Rota                            | Descrição                                             |
|--------|---------------------------------|-------------------------------------------------------|
| POST   | /auth                           | Aluno autenticar na plataforma                        |
| GET    | /student/{id}                   | Detalhes de um aluno                                  |
| GET    | /activity/{id}                  | Detalhes de uma atividade                             |
| PATCH  | /activity/{id}                  | Salva as alterações do andamento da atividade         |
| POST   | /activity/{id}                  | Envia todas as respostas e conclui a atividade        |
| GET    | /question/{id}                  | Detalhes de uma questão                               |
| POST   | /question/{id}                  | Envia a resposta de uma questão                       |

Conforme mencionado acima a documentação completa dos endpoints está em http://localhost:8000/docs

---

## Casos de Teste + Implementação (para 2 rotas)

### POST /auth
**Casos de teste:**

- ✅ Inserir e-mail e senha válidos.
- ❌ Inserir e-mail incorreto.
- ❌ Inserir senha incorreto.
- ❌ Submeter faltando preencher campo e-mail
- ❌ Submeter faltando preencher campo senha

### POST /activity/{id}    
**Casos de teste:**

- ✅ Enviar a requisição com todos os elementos preenchidos.
- ❌ Tentar submeter com objeto em branco.
- ❌ Tentar submeter com algum parâmetro em branco.
- ❌ Tentar submeter com usuário não-logado.

---

## Diagrama da Arquitetura
![Diagrama da arquitetura](./diagrama-miia.png)

---

## Estrutura de pastas simplificada
```bash
app/
├── main.py
├── database.py
├── models/
│   └── __init__.py
│   └── student.py
│   └── activity.py
│   └── question.py
│   └── answers.py
├── schemas/
│   └── student.py
│   └── activity.py
│   └── question.py
│   └── answers.py
├── routers/
│   └── auth.py
│   └── student.py
│   └── activity.py
│   └── question.py
└── tests/
│   └── test_student.py
│   └── test_activity.py
│   └── test_question.py
│   └── test_answers.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .env
```

---

### Desenvolvido por [Roosevelt Franklin](https://rcode.com.br)
