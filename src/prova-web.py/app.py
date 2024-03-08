from flask import Flask, render_template, request, redirect, url_for
from tinydb import TinyDB

app = Flask(__name__)
db = TinyDB('caminhos.json')

@app.route("/novo", methods=['POST'])
def novo_caminho():
    if request.method == "POST":
        dados = request.json
    db.insert(dados)
    dados = request.json
    id = db.insert(dados)
    return render_template()

@app.route("/pegar_caminho", methods=['GET'])
def pegar_caminho():
    if request.method == "GET":
        dados = request.json
    db.insert(dados)
    dados = request.json
    id = db.insert(dados)
    return render_template()

@app.route("/listas_caminhos", methods=['GET'])
def listar_caminhos():
    if request.method == "GET":
        dados = request.json
    db.insert(dados)
    dados = request.json
    id = db.insert(dados)
    return render_template()

@app.route("/atualizar", methods=['POST'])
def atualizar_caminho(id):
    if request.method == "POST":
        dados = request.json
    db.insert(dados)
    dados = request.json
    id = db.insert(dados)
    return render_template()

@app.route("/deletar", methods=['DELETE'])
def deletar_caminho(id):
    if request.method == "DELTE":
        dados = request.json
    db.insert(dados)
    dados = request.json
    id = db.insert(dados)
    return render_template()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)