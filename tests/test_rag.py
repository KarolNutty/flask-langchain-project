import pytest
import os
from app import app
from rag_service import clear_vectorstore, create_vectorstore, answer_question

@pytest.fixture
def client():
    clear_vectorstore()
    with app.test_client() as client:
        yield client


def test_pdf_upload(client, tmp_path):
    # cria PDF fake
    pdf_path = tmp_path / "test.pdf"
    pdf_path.write_bytes(b"%PDF-1.4 test")

    data = {"file": (open(pdf_path, "rb"), "test.pdf")}
    res = client.post("/upload", data=data, content_type="multipart/form-data")

    assert res.status_code == 200


def test_ask_mocked(monkeypatch, client, tmp_path):
    # cria vetor fake
    vector_path = tmp_path / "fake.pdf"
    vector_path.write_bytes(b"%PDF-1.4 fake")
    create_vectorstore = lambda x: True

    # mock do answer_question
    monkeypatch.setattr(
        "rag_service.answer_question",
        lambda q: "Resposta mockada"
    )

    res = client.post("/ask", json={"question": "Qualquer coisa?"})
    assert res.status_code == 200
    assert res.get_json()["answer"] == "Resposta mockada"
