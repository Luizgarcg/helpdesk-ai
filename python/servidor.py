from main import cad_chamado, classificar_ugencia, chamados
from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/")
def pagina_inicial():
    return render_template("index.html")
@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    nome = request.form["nome"]
    setor = request.form["setor"]
    titulo = request.form["titulo"]
    descricao = request.form["descricao"]
    cad_chamado(nome, setor, titulo, descricao)
    urgencia = classificar_ugencia(descricao)
    return f"Chamado cadastrado! Urgência: {urgencia}"


if __name__ == "__main__":
    app.run(debug=True)