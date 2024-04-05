from azure.cosmos import CosmosClient

class CosmosDBContext():
  def __init__(self, endpoint, key, database, container):
    self.Client=CosmosClient(endpoint, key)
    self.Database=database
    self.Container=container

