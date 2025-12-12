# 🚀 Flask RAG Support — IA na prática, do jeitinho que eu gosto

Esse projeto aqui é meu mini-laboratório de **IA aplicada**, onde eu junto Flask + LangChain + RAG + embeddings pra criar um sistema de suporte baseado em documentos.
Tradução: *eu pego um PDF, fatio, indexo, jogo numa vectorstore e deixo a IA responder tudo em cima dele bonitinho.*

Projeto simples, direto e com cheiro de **dev que manja de automação inteligente**.

---

## 🧠 O que esse projeto faz?

* 📄 Lê PDFs automaticamente
* ✂️ Divide o conteúdo em chunks
* 💾 Gera embeddings com OpenAI
* 🔍 Cria uma base vetorial com FAISS
* 🤖 Responde perguntas usando RAG + LangChain
* 🧪 Já preparado pra testes com Pytest
* 🔑 Backend seguro e estruturado

É literalmente um mini-chat de suporte baseado no seu PDF, só que feito com carinho e boas práticas.

---

## 🛠️ Tecnologias que uso aqui

* **Python 3.11**
* **Flask 3**
* **LangChain**
* **FAISS**
* **pypdf**
* **OpenAI API**
* **Pytest**

Tudo leve, realista e focado em IA aplicada — exatamente como eu trabalho.

---

## ⚙️ Como rodar

Crie o ambiente:

```bash
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.\.venv\Scripts\activate    # Windows
```

Instale dependências:

```bash
pip install -r requirements.txt
```

Suba a aplicação:

```bash
flask run
```

---

## 🧩 Estrutura do projeto

```
flask-rag-support/
│── app.py
│── rag/
│   ├── vectorstore/
│   ├── loader.py
│   ├── retriever.py
│   ├── pipeline.py
│── tests/
│── requirements.txt
│── README.md
```

---

## 💬 Exemplos de uso

```
POST /api/upload
POST /api/ask { "question": "Qual é o resumo do documento?" }
```

---

## ❤️ Sobre mim

Eu sou a Karoline, **AI Developer** focada em IA aplicada, automações inteligentes e orquestração de sistemas usando n8n + Python + LangChain.
Gosto de construir soluções enxutas, práticas e que resolvem problemas de verdade.

---

## ⭐ Se curtir, deixa uma star pra fortalecer ✨

*(Eu prometo que continuo postando mais projetinhos de IA brabos.)*

---

Se quiser, faço também uma **versão estética com emojis coloridos**, outra **mais clean**, ou uma **versão premium estilo startup chique** — só falar o vibe que você quer.
