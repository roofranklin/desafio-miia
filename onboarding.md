### 🎯 Objetivo

Delegar a implementação de novos endpoints RESTful da API para um desenvolvedor júnior, garantindo clareza nas prioridades, acompanhamento contínuo e autonomia técnica com suporte.

---

### ✅ Passo a Passo para o Desenvolvedor

Olá,

Estamos dando continuidade no desenvolvimento da nossa API FastAPI da plataforma MIIA. Abaixo está o direcionamento para você assumir parte da tarefa:

---

#### 🔹 Contexto Geral

- Utilizamos **FastAPI** com **PostgreSQL**, **SQLAlchemy** como ORM e testes com **Pytest**.
- A arquitetura está organizada por domínio:
  - `models/`, `schemas/`, `routers/`, `tests/`, `database.py`, `main.py`
- Estrutura em containers com Docker já funcional.

---

#### 🔧 O que já está pronto

- Endpoint `/activity` (GET, PATCH, POST)
- Base de testes automatizados
- Estrutura de schemas de atividades

---

#### 📌 Suas próximas tarefas

1. **Endpoints a implementar:**
   - `POST /auth`: autenticação de aluno
   - `GET /questions/{activity_id}`: retorna questões de uma atividade
   - `GET/POST /question/{id}`: obter e responder questão

2. **Schemas Pydantic:**
   - Criar e validar:
     - `QuestionResponseSchema`
     - `AlternativeSchema`
     - `EssayAnswerSchema`
     - `RedacaoSchema`
   - Lembre-se: campos podem ser `null` (usar `Optional[...]`)

3. **Testes com Pytest:**
   - Cobrir rotas criadas com cenários válidos e inválidos
   - Reutilizar estrutura de `test_activity.py`

---

#### 🧭 Prioridades

| Ordem | Tarefa |
|-------|--------|
| 1️⃣ | Criar schemas (`schemas/question.py`) |
| 2️⃣ | Implementar rotas `GET` |
| 3️⃣ | Implementar rotas `POST/PATCH` |
| 4️⃣ | Escrever testes automatizados |

---

### 🧑‍💼 Acompanhamento

- Me envie **updates ao finalizar cada etapa**.
- Se ficar mais de 30min travado, **me chama no inbox ou marca 1:1 rápido**.
- Suba PRs para cada rota nova. Farei code review **no fim de cada dia útil**.
- Use sempre o template de PR e checklist de testes.

---
