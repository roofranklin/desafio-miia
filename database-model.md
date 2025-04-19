# 📘 Modelo de Banco de Dados — Plataforma MIIA

Abaixo está o modelo relacional de banco de dados para a plataforma de estudos MIIA.

---

## 👤 Aluno

| Campo     | Tipo      | Descrição              |
|-----------|-----------|------------------------|
| id        | int (PK)  | Identificador único    |
| nome      | string    | Nome completo do aluno |
| email     | string    | E-mail do aluno        |
| senha     | string    | Senha (hash)           |

---

## 📝 Atividade

| Campo          | Tipo       | Descrição                          |
|----------------|------------|------------------------------------|
| id             | int (PK)   | Identificador da atividade         |
| aluno_id       | int (FK)   | ID do aluno                        |
| data_inicio    | datetime   | Data e hora de início da atividade |
| duracao_minutos| int        | Duração total da atividade (min)   |
| concluida      | boolean    | Mostra se o aluno concluiu         |
| descricao      | string     | Nome ou titulo da atividade        |

---

## ❓ Questão

| Campo        | Tipo       | Descrição                            |
|--------------|------------|--------------------------------------|
| id           | int (PK)   | Identificador da questão             |
| atividade_id | int (FK)   | ID da Atividade                      |
| tipo         | string     | 'objetiva', 'redação ou 'discursiva' |
| enunciado    | text       | Enunciado da questão                 |

---

## 🔘 Alternativa (para questões objetivas)

| Campo          | Tipo     | Descrição                        |
|----------------|----------|----------------------------------|
| id             | int (PK) | Identificador da alternativa     |
| questao_id     | int (FK) | Questão à qual pertence          |
| alternativa    | string   | Texto da alternativa             |
| gabarito       | boolean  | Se é a alternativa correta       |
| resposta_aluno | boolean  | O que o aluno escolheu / null    |

---

## 📄 ItemDiscursivo (para questões discursivas)

| Campo       | Tipo     | Descrição                          |
|-------------|----------|------------------------------------|
| id          | int (PK) | Identificador do item              |
| questao_id  | int (FK) | Questão à qual pertence            |
| pergunta    | text     | Texto da pergunta (subitem)        |
| resposta    | text     | Resposta do aluno (subitem) / null |
| nota        | float    | Nota do aluno / null               |

---

## 🧠 TemaRedacao

| Campo        | Tipo     | Descrição                          |
|--------------|----------|------------------------------------|
| id           | int (PK) | Identificador do tema              |
| titulo       | string   | Nome do tema                       |
| enunciado    | text     | Texto motivador ou introdutório    |
| resposta     | text     | Resposta do aluno (subitem) / null |
| nota         | float    | Nota do aluno / null               |

---


## 🔄 Relacionamentos Principais

| Entidade                         | Relacionamento               |
|----------------------------------|------------------------------|
| `alunos` => `atividades`         | 1:N                          |
| `atividades` => `questoes`       | 1:N                          |
| `questoes` => `alternativa`      | 1:N (se tipo = 'objetiva')   |
| `questoes` => `discursiva`       | 1:N (se tipo = 'discursiva') |
| `questoes` => `redacao`          | 1:N (se tipo = 'redacao')    |     
                
