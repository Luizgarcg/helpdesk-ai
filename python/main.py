import os
from dotenv import load_dotenv
load_dotenv()
chave = os.getenv("GEMINI_API_KEY")
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
    
    
cad_chamado("luis","financeiro","impressora nao funciona","gostaria de fazer uma reclamação a empressora do predio nao esta funcionando")
cad_chamado("emilien beaugrand","financeiro","eu quero cafe", "meu cafe nao chegou na minha sala")
lista_de_chamados()
editar_chamado(1,"madona")
lista_de_chamados()
deletar_chamado(1)
lista_de_chamados()
