from modules.cosmosdb.initcosmosdb import CosmosDBContext
# from modules.databases.db_executions import DbExecutio

# class BbWrite:
def Upsert(endpoint, key, database, table, obj):
  db = CosmosDBContext(endpoint, key, database, table)

  database=db.Client.get_database_client(db.Database)
  container=database.get_container_client(db.Container)

  container.upsert_item(obj)
  return True

