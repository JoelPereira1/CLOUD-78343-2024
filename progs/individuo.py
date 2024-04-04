class Individuo:
  # função construtora
  def __init__(self, cc, nome, apelido, idade, foto):
    self.CC = cc
    self.Nome = nome
    self.Apelido = apelido
    self.Idade = idade
    self.Foto = foto

  def __str__(self):
    return f"{self.Nome} {self.Apelido}"

  def NomeCompleto(self):
    return self.Nome + " " + self.Apelido

  def FotoUrl(self, accountstorage = '', blobcontainer = '', IsCosmos = False):
    if IsCosmos:
      return "https://{0}.blob.core.windows.net/{1}/{2}".format(accountstorage,blobcontainer,self.Foto)
    else:
      return "/static/img/%s"%(self.Foto)