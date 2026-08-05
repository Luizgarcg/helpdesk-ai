from google import genai
import os
from dotenv import load_dotenv
load_dotenv()
chave = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=chave)
chamados = []
class Chamado:
   def __init__ (self,nome,setor,titulo,descricao,):
       self.nome = nome
       self.setor = setor
       self.titulo = titulo
       self.descricao = descricao
def cad_chamado(nome,setor,titulo,descricao):
    novo = Chamado(nome,setor,titulo,descricao)
    chamados.append(novo)
def lista_de_chamados():
   for i in chamados:
       print(i.nome,i.titulo)
       
def editar_chamado(indice,novo_titulo):
    chamados[indice].titulo = novo_titulo

def deletar_chamado(indice):
    chamados.pop(indice)

def classificar_ugencia(descricao):
    prompt = f"classifique a urgencia desse chamado de suporte como baixa media ou alta. responda-me com apenas uma unica palavra descrição: {descricao}"
    resposta = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )
    return resposta.text
