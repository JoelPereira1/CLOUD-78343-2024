from plant_realm import PlantRealm
from flaskshop.settings import *
import modules.databases.db_read as BbRead
import modules.databases.db_write as BbWrite
import modules.databases.db_delete as BbDelete


TABLENAME = 'tblPlant'

class Plant(PlantRealm):
  def __init__(self, id='', name ='', botanical_name ='', category='', photo='', size='', color='', smell='', spikes='', IsCosmos = False):
    PlantRealm.__init__(self, id, name, botanical_name, category, photo, IsCosmos)
    self.size = size
    self.color = color
    self.smell = smell
    self.spikes = spikes

  def NomeCompleto(self):
    return self.Patente + " " + self.Apelido

  def ToDicionario(self):
    return { 'ID': self.ID, 'Foto': self.Foto, 'NIM': self.NIM, 'CC': self.CC, 'Patente': self.militarpatente, 'Nome': self.Nome, 'Apelido': self.Apelido , 'Idade': self.Idade }

  def ToSqlDicionario(self):
    return { 'ID': self.ID, 'Foto': self.Foto, 'NIM': self.NIM, 'CC': self.CC, 'militarpatente': self.militarpatente, 'Nome': self.Nome, 'Apelido': self.Apelido , 'Idade': self.Idade }

  def ToCosmosDicionario(self):
    return { 'id': self.ID, 'Foto': self.Foto ,'NIM': self.NIM, 'CC': self.CC, 'Patente': self.militarpatente, 'Nome': self.Nome, 'Apelido': self.Apelido , 'Idade': self.Idade }

  # DB GetMethods
  def Get(self, id):
    result,values = BbRead.Get(SQLITECONNECTIONSTRING, TABLENAME, 'ID', id)
    if result:
      for row in values:
        self.ID=row[0]
        self.Foto=row[1]
        self.NIM=row[2]
        self.militarpatente=row[3]
        self.CC=row[4]
        self.Nome=row[5]
        self.Apelido=row[6]
        self.Idade=row[7]
      return result,self

  # DB WriteMethods
  def Inserir(self):
    result = BbWrite.Inserir(SQLITECONNECTIONSTRING, TABLENAME, self)
    return result

  def Update(self):
    result = BbRead.Get(SQLITECONNECTIONSTRING, TABLENAME, 'ID', self.ID)
    if result:
      result = BbWrite.Update(SQLITECONNECTIONSTRING, TABLENAME, 'ID', self)
      return result
    else:
      return print('Militar not fund')

  # DB GetMethods
  @staticmethod
  def Militares():
    result,values = BbRead.GetAll(SQLITECONNECTIONSTRING, TABLENAME)
    lista=[]

    if result:
      for row in values:
        m = Militar(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
        lista.append(m)
    return lista

  # DB DeleteMethods
  @staticmethod
  def Delete(col, id):
    result = BbDelete.Delete(SQLITECONNECTIONSTRING, TABLENAME, col, id)
    return result

  @staticmethod
  def Header():
    return ["Patente","Nome","Apelido","Idade"]

  @staticmethod
  def ListaDePatentes():
    return ["Mancebo","Cabo","Sargento"]

  def fotoDownloadUrl(self):
    print("#######################################")
    print(self.Foto)
