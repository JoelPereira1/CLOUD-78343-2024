from web.settings import *
import modules.databases.db_read as BbRead
import modules.databases.db_write as BbWrite
import modules.databases.db_delete as BbDelete

TABLENAME = 'tblPatente'

class Patente():
  def __init__(self,id='',nome='',iniciais=''):
    self.ID = id
    self.Nome = nome
    self.Iniciais = iniciais

  def ToDicionario(self):
    return { 'ID': self.ID, 'Nome': self.Nome, 'Iniciais': self.Iniciais }

  def ToSqlDicionario(self):
    return { 'ID': self.ID, 'Nome': self.Nome, 'Iniciais': self.Iniciais }

  # DB GetMethods
  def Get(self,id):
    result,values = BbRead.Get(SQLITECONNECTIONSTRING,TABLENAME, 'ID', id)
    if result:
      for row in values:
        self.ID=row[0]
        self.Nome=row[1]
        self.Iniciais=row[2]
      return result,self

  @staticmethod
  def Patentes():
    result,values = BbRead.GetAll(SQLITECONNECTIONSTRING,TABLENAME)
    lista=[]
    if result:
      for row in values:
        p = Patente(row[0],row[1],row[2])
        lista.append(p)
    return lista

  # DB WriteMethods
  def Inserir(self):
    result = BbWrite.Inserir(SQLITECONNECTIONSTRING, TABLENAME, self)
    return result

  def Update(self):
    result = BbRead.Get(SQLITECONNECTIONSTRING,TABLENAME, 'ID', self.ID)
    if result:
      result = BbWrite.Update(SQLITECONNECTIONSTRING, TABLENAME,'ID', self)
      return result
    else:
      return print('Patente not fund')

  @staticmethod
  def Delete(id):
    result = BbDelete.Delete(SQLITECONNECTIONSTRING, TABLENAME,'ID', id)
    return result