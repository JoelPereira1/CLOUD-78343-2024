import csv
import json

# module FileUtils:
@staticmethod
def ExportToCSV(path,header,lista,separador,quoting):
  try:
    with open(path,"w") as csvfile:
      obj = csv.DictWriter(csvfile,header,delimiter=separador,quoting=quoting)
      obj.writeheader()
      obj.writerows(lista)
  except:
    pass

@staticmethod
def ImportFromCSV(path,separador):
  lista=[]
  try:
    with open(path,"r") as csvfile:
      obj = csv.DictReader(csvfile,delimiter=separador)
      for linha in obj:
        lista.append()
      return True,lista,""
  except Exception as e:
    return False,[],e

@staticmethod
def ExportToJson(object):
  return json.dumps(object)

@staticmethod
def ImportFromJson(value):
  return json.loads(value)

@staticmethod
def SaveInFile(path,data):
  with open(path,"w") as outputfile:
    outputfile.write(data)

@staticmethod
def ReadFromFile(path):
  output=""
  with open(path) as inputfile:
    output = inputfile.read()
  return output

def allowed_file(filename, ALLOWED_EXTENSIONS):
  return '.' in filename and \
          filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# # @app.route('/', methods=['GET', 'POST'])
# def upload_file():
#   if request.method == 'POST':
#       # check if the post request has the file part
#       if 'file' not in request.files:
#           flash('No file part')
#           return redirect(request.url)
#       file = request.files['file']
#       # If the user does not select a file, the browser submits an
#       # empty file without a filename.
#       if file.filename == '':
#           flash('No selected file')
#           return redirect(request.url)
#       if file and allowed_file(file.filename):
#           filename = secure_filename(file.filename)
#           file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#           return redirect(url_for('download_file', name=filename))