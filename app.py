import os
from flask import Flask, request, jsonify
from rag_service import create_vectorstore, answer_question, clear_vectorstore

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)


@app.post("/upload")
def upload_pdf():
    if "file" not in request.files:
        return jsonify({"error": "Nenhum arquivo enviado"}), 400

    file = request.files["file"]
    if not file.filename.endswith(".pdf"):
        return jsonify({"error": "Envie um PDF válido"}), 400

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    clear_vectorstore()
    create_vectorstore(filepath)

    return jsonify({"message": "PDF indexado com sucesso!"})


@app.post("/ask")
def ask_question():
    data = request.json
    question = data.get("question")

    if not question:
        return jsonify({"error": "Pergunta não enviada"}), 400

    answer = answer_question(question)
    return jsonify({"answer": answer})


if __name__ == "__main__":
    app.run(debug=True)
