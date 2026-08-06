from flask import Flask, render_template, request, redirect, url_for
from main import cad_chamado, classificar_ugencia, chamados
app = Flask(__name__)
@app.route("/")
def pagina_inicial():
    return render_template("index.html", chamados=chamados)
@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    nome = request.form["nome"]
    setor = request.form["setor"]
    titulo = request.form["titulo"]
    descricao = request.form["descricao"]
    urgencia = classificar_ugencia(descricao)
    cad_chamado(nome, setor, titulo, descricao,urgencia)
    return redirect(url_for("pagina_inicial"))


if __name__ == "__main__":
    app.run(debug=True)