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
| data_fim       | datetime   | Calculado com base na duração      |
| nota_final     | float      | Nota final após correção           |

---

## ❓ Questão

| Campo     | Tipo       | Descrição                        |
|-----------|------------|----------------------------------|
| id        | int (PK)   | Identificador da questão         |
| tipo      | string     | 'objetiva' ou 'discursiva'       |
| enunciado | text       | Enunciado da questão             |

---

## 🔘 Alternativa (para questões objetivas)

| Campo         | Tipo     | Descrição                        |
|---------------|----------|----------------------------------|
| id            | int (PK) | Identificador da alternativa     |
| questao_id    | int (FK) | Questão à qual pertence          |
| texto         | string   | Texto da alternativa             |
| correta       | boolean  | Se é a alternativa correta       |

---

## 📄 ItemDiscursivo (para questões discursivas)

| Campo       | Tipo     | Descrição                         |
|-------------|----------|-----------------------------------|
| id          | int (PK) | Identificador do item             |
| questao_id  | int (FK) | Questão à qual pertence           |
| pergunta    | text     | Texto da pergunta (subitem)       |

---

## 🧠 TemaRedacao

| Campo        | Tipo      | Descrição                         |
|--------------|-----------|-----------------------------------|
| id           | int (PK)  | Identificador do tema             |
| titulo       | string    | Nome do tema                      |
| enunciado    | text      | Texto motivador ou introdutório   |
| estilo_texto | string    | Ex: "dissertativo-argumentativo"  |

---

## 🧾 RespostaAluno

| Campo              | Tipo      | Descrição                                |
|--------------------|-----------|------------------------------------------|
| id                 | int (PK)  | Identificador da resposta                |
| atividade_id       | int (FK)  | Atividade à qual pertence                |
| questao_id         | int (FK)  | Questão respondida (nullable)            |
| tema_redacao_id    | int (FK)  | Tema da redação (nullable)               |
| tipo               | string    | 'objetiva' | 'discursiva' | 'redacao'    |

---

## ✅ RespostaObjetiva

| Campo                   | Tipo     | Descrição                           |
|-------------------------|----------|-------------------------------------|
| id                      | int (PK) | ID da resposta objetiva             |
| resposta_aluno_id       | int (FK) | FK para RespostaAluno               |
| alternativa_escolhida_id| int (FK) | Alternativa marcada pelo aluno      |

---

## ✍️ RespostaDiscursiva

| Campo             | Tipo     | Descrição                         |
|-------------------|----------|-----------------------------------|
| id                | int (PK) | ID da resposta discursiva         |
| resposta_aluno_id | int (FK) | FK para RespostaAluno             |
| item_id           | int (FK) | Item discursivo respondido        |
| texto_resposta    | text     | Resposta textual do aluno         |

---

## ✏️ RespostaRedacao

| Campo             | Tipo     | Descrição                     |
|-------------------|----------|-------------------------------|
| id                | int (PK) | ID da redação respondida      |
| resposta_aluno_id | int (FK) | FK para RespostaAluno         |
| texto_redacao     | text     | Texto completo da redação     |

---

## 📊 Correcao

| Campo             | Tipo     | Descrição                                     |
|-------------------|----------|-----------------------------------------------|
| id                | int (PK) | ID da correção                                |
| resposta_aluno_id | int (FK) | FK para RespostaAluno                         |
| nota              | float    | Nota atribuída (0 a 10, por exemplo)          |
| comentarios       | text     | Comentários com sugestões e observações       |

---

## 🔄 Relacionamentos Principais

```plaintext
Aluno 1 ────< Atividade >──── 1 TemaRedacao
                  |
                  └────< RespostaAluno >──── 1 Questao
                               |
             ┌─────────────────┴──────────────┐
     (objetiva)                     (discursiva/redação)
RespostaObjetiva          RespostaDiscursiva / RespostaRedacao
                                |
                             Correcao
