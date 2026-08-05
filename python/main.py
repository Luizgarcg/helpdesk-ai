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