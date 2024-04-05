from modules.cosmosdb.initcosmosdb import CosmosDBContext

# class BbDelete:
@staticmethod
def Delete(endpoint, key, database, table, col, obj):
  db = CosmosDBContext(endpoint, key, database, table)

  database=db.Client.get_database_client(db.Database)
  container=database.get_container_client(db.Container)
  container.delete_item(obj['id'], partition_key=obj['Patente'])
  return True