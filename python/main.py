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
    
    
cad_chamado("luis","financeiro","impressora nao funciona","gostaria de fazer uma reclamação a empressora do predio nao esta funcionando")
cad_chamado("emilien beaugrand","financeiro","eu quero cafe", "meu cafe nao chegou na minha sala")
lista_de_chamados()
editar_chamado(1,"madona")
lista_de_chamados()
deletar_chamado(1)
lista_de_chamados()
