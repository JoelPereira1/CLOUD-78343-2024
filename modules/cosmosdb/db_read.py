#To use the % operator for string interpolation, the following syntax is used:
#string % values
# user = "Abrar"
# age = "20"
# print("Hello %s. Your age is %s "%(user,age))
# %s: when we want the placeholder value to be a string
# %f: when we want the placeholder value to be a floating point decimal like 2.415
# %r: when we want to replace the placeholder with the raw data of a variable
# %x: when the value replacing the placeholder has to be a hexadecimal value
# %o: when the value replacing the placeholder has to be an octal value
# %c: when we want to replace the placeholder with special characters
from modules.cosmosdb.initcosmosdb import CosmosDBContext

# class BbRead:
def Get(endpoint, key, database, table, column, id):
  db = CosmosDBContext(endpoint, key, database,table)
  database=db.Client.get_database_client(db.Database)
  container=database.get_container_client(db.Container)

  for item in container.query_items(
    query="SELECT * FROM %s AS i WHERE i.%s='%s'"%(db.Container,column,id),
    enable_cross_partition_query=True
  ):
    return True, item
  return False, None

@staticmethod
def GetAll(endpoint, key, database, table):
  db = CosmosDBContext(endpoint, key, database,table)
  database=db.Client.get_database_client(db.Database)
  container=database.get_container_client(db.Container)
  lista = []
  for item in container.query_items(
    query="SELECT * FROM %s"%(db.Container),
    enable_cross_partition_query=True
  ):
    lista.append(item)

  return lista