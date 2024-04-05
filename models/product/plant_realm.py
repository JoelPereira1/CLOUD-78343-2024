import uuid

class PlantRealm:
  # função construtora
  def __init__(self, id, name, botanical_name, category, photo, IsCosmos):
    self.id = id
    self.name = name
    self.botanical_name = botanical_name
    self.photo = photo
    self.category_id = category

    if id == '':
      if IsCosmos:
        self.id = str(uuid.uuid4())
      else:
        self.id = id
    else:
      self.id = id

  def __str__(self):
    return f"{self.botanical_name} / {self.name}"

  def PhotoUrl(self, accountstorage = '', blobcontainer = '', IsCosmos = False):
    if IsCosmos:
      return "https://{0}.blob.core.windows.net/{1}/{2}".format(accountstorage,blobcontainer,self.photo)
    else:
      return "/static/img/%s"%(self.photo)