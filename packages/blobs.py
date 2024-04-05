from azure.storage.blob import BlobServiceClient, BlobClient

class Blobs:
  @staticmethod
  def blobupload(blob_connection_string, blob_container, filename, data):
    bsc = BlobServiceClient.from_connection_string(blob_connection_string)
    bc = bsc.get_blob_client(blob_container, filename)
    bc.upload_blob(data,overwrite=True)

  @staticmethod
  def bloblist(blob_connection_string, blob_container):
    bsc = BlobServiceClient.from_connection_string(blob_connection_string)
    cnc = bsc.get_container_client(blob_container)
    lista = []
    for b in  cnc.list_blobs():
        lista.append(b.name)

  @staticmethod
  def blobdownload(blob_connection_string, blob_container, filename):
    bsc = BlobServiceClient.from_connection_string(blob_connection_string)
    bc = bsc.get_blob_client(blob_container, filename)
    bc.download_blob()
