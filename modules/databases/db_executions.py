import sqlite3
from sqlite3 import Error

# class DbExecutions:
@staticmethod
def SQLLiteExecute(database, sql, isSelect=True):
  result = False
  lista = []
  try:
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute(sql)

    if isSelect:
      for linha in c.fetchall():
        lista.append(linha)
    else:
      conn.commit()
    result = True
  except:
    pass
  finally:
    if conn:
      conn.close()

  return result,lista

def SQLLiteGetTableCols(database, table):
  result = False
  colnames = []
  try:
    conn = sqlite3.connect(database)
    c = conn.execute("select * from %s"%(table))
    sqlcolnames = c.description
    for row in sqlcolnames:
      colnames.append(row[0])
    result = True
  except:
    pass
  finally:
    if conn:
      conn.close()

  return result,colnames

def SQLLiteColsTypes(database, table):
  result = False
  sqlcoltypes = []
  try:
    conn = sqlite3.connect(database)
    c = conn.execute("SELECT name, type FROM pragma_table_info('%s') "%(table))
    for linha in c.fetchall():
      sqlcoltypes.append(linha)
    result = True
  except:
    pass
  finally:
    if conn:
      conn.close()
  return result,sqlcoltypes

def SQLLiteGetLastId(database, table):
  last_id = 1
  result = False
  try:
    conn = sqlite3.connect(database)
    c = conn.cursor()
    last_id = c.lastrowid
    # last_id = c.rowcount
    # last_id = c.execute('SELECT LAST_INSERT_ROWID() FROM %s'%(table))
    result = True
  except:
    pass
  finally:
    if conn:
      conn.close()

  return result,last_id