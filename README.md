
# 🚀 Flask RAG Support — Meu micro-sistema de RAG com Flask

Esse projetinho aqui é meu **playground de IA aplicada**: um app Flask que lê PDF, gera embeddings, cria a vectorstore e responde perguntas estilo “suporte inteligente”.
Tudo em **um único arquivo** — enxuto, direto e funcional.

Perfeito pra testar, aprender e construir RAG rapidinho.

---

## 🧠 O que ele faz

* 📄 Lê o PDF enviado
* ✂️ Divide em chunks com RecursiveCharacterTextSplitter
* 🧠 Gera embeddings com OpenAI
* 📚 Armazena tudo num **FAISS local**
* 🤖 Usa LangChain para responder perguntas com RAG
* 🔁 Permite recriar a base quando você quiser

Simples, prático e *total Karol vibes*: focado em IA e sem complicar a vida.

---

## 🛠️ Stack usada

* **Python 3.11**
* **Flask**
* **LangChain (0.1.x)**
* **langchain-community**
* **FAISS**
* **pypdf**
* **OpenAI API**

---

## 📂 Estrutura real do projeto

```
flask-rag-support/
│── app.py
│── vectorstore/   # gerado automaticamente
│── requirements.txt
│── README.md
```

É isso. Slim, clean e funcionando.

---

## ⚙️ Como rodar

Criar o ambiente (Python 3.11):

```bash
uv venv -p 3.11 .venv
uv pip install -r requirements.txt
```

Rodar o Flask:

```bash
flask run
```

---

## 🔥 Rotas disponíveis

### ▶️ /upload

Recebe PDF e recria a vectorstore.

### ▶️ /ask

Recebe a pergunta e retorna a resposta com RAG.

---

## 💡 Exemplo de uso

```
curl -X POST http://localhost:5000/ask \
    -H "Content-Type: application/json" \
    -d '{"question": "O que fala o documento?"}'
```

---

## ❤️ Sobre mim

Eu sou a Karoline, **AI Developer** focada em IA aplicada, automações inteligentes e integrações.
Trabalho com LangChain, OpenAI, Python e n8n pra criar soluções reais — desde RAG simples até agentes e pipelines mais complexos.

Esse projeto é um dos meus laboratórios pessoais pra treinar RAG na prática.

---

## ⭐ Se curtir, deixa uma star pra fortalecer ✨

Mais projetinhos vindo aí 👀🔥

---

