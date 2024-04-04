# -*- coding: utf-8 -*-
import os
from web.settings import *
from modules.databases.initdb import init_database
from flask_bootstrap import Bootstrap
from flask import Flask, render_template, request, flash, redirect, url_for
# from flask_wtf import CSRFProtect
from web import app
from datetime import datetime
from progs.militar import Militar
from progs.patente import Patente
from packages.militar_form import MilitarForm
# from web.empty_form import EmptyForm
# from werkzeug.utils import secure_filename
# COSMOS DB
import modules.cosmosdb.db_read as CosmosBbRead
import modules.cosmosdb.db_write as CosmosBbWrite
import modules.cosmosdb.db_delete as CosmosBbDelete
# BlobContainer Azure
from packages.blobs import Blobs

if __name__=="__main__":
  app.run(host="0.0.0.0", debug=True)

# Database Init
# variables from settings
TABLE_OBJECTS =  [FLOWER_TABLE, USER_TABLE]
init_database(SQLITECONNECTIONSTRING,TABLE_OBJECTS)

app = Flask(__name__)
# Bootstrap-Flask requires this line
bootstrap = Bootstrap(app)

# Flask-WTF requires this line
# csrf = CSRFProtect(app)

UPLOAD_FOLDER = './static/img'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
SUBMIT_METHODS = {"POST", "PUT", "PATCH", "DELETE"}

@app.route('/')
@app.route('/home')
def home():
  return render_template("index.html",title="Home Page",year=datetime.now().year)

@app.route('/about')
def about():
  return render_template("about.html",title="About Page",year=datetime.now().year)

# Militar Routes
@app.route('/militares')
def militares():
  militares = Militar.Militares()
  return render_template("militares/militares.html",titulo="Militares",year=datetime.now().year,militares=militares)

@app.route('/inserirmilitar', methods=['GET', 'POST'])
def inserirmilitar():
  # you must tell the variable 'form' what you named the class, above
  # 'form' is the variable name used in this template: index.html
  form = request.form
  message = ""
  patentes = Patente.Patentes()

  if is_submitted(request):
    file = request.files['fupload']
    filename = file.filename
    if filename:
      if allowed_file(filename):
        file.save(os.path.join(UPLOAD_FOLDER, filename))
      else:
        flash("Invalid: File extension.", "danger")
        return render_template('404.html', message=message), 404

    ID, FOTO, NIM, CC, NOME, APELIDO, PATENTE, IDADE = MilitarForm.form_fields(form, id = '', filename = filename)

    obj = Militar(ID,FOTO,NIM,PATENTE,CC,NOME,APELIDO,IDADE)
    militar = Militar.Inserir(obj)

    if militar:
      flash("Success: Info added successfully.", "success")
      return redirect( url_for('militares') )
    else:
      flash("Invalid: Every field is required.", "danger")
      return render_template('404.html', message=message), 404

  return render_template('militares/inserir_militar.html',title="Inserir Militar Page",year=datetime.now().year, patentes=patentes, message=message)

@app.route('/vermilitar/<id>')
def vermilitar(id):
  # run function to get militar data based on the id in the path
  militar = Militar()
  result, obj = militar.Get(id=id)

  patente = Patente()
  result, obj_patente = patente.Get(id=obj.militarpatente)
  if result:
    # pass all the data for the selected militar to the template
    return render_template('militares/ver_militar.html', title = "Ver Militar Page", year = datetime.now().year, militar=obj, patente=obj_patente)
  else:
    # redirect the browser to the error template
    return render_template('404.html'), 404

@app.route('/editarmilitar/<id>', methods=['GET', 'POST'])
def editarmilitar(id):
  # return render_template("index.html",title="Home Page",year=datetime.now().year)
  patentes = Patente.Patentes()
  militar = Militar()
  result, obj = militar.Get(id)

  if result:
    form = request.form
    message = ""
    if is_submitted(request):
      file = request.files['fupload']
      filename = file.filename

      if filename:
        if allowed_file(filename):
          file.save(os.path.join(UPLOAD_FOLDER, filename))
        else:
          flash("Invalid: File extension.", "danger")
          return render_template('404.html', message=message), 404

      ID = id
      FOTO = filename if filename else obj.Foto
      NIM = form.get('txtNIM')
      CC = form.get('txtCC')
      NOME = form.get('txtNome')
      APELIDO =form.get('txtApelido')
      PATENTE = form.get('txtPatente')
      IDADE = form.get('txtIdade')

      militar = Militar(ID,FOTO,NIM,PATENTE,CC,NOME,APELIDO,IDADE)
      result = militar.Update()

      if result:
        flash("Success: Info updated successfully.", "success")
        return redirect( url_for('militares') )
      else:
        flash("Invalid: Every field is required.", "danger")
        return render_template('404.html', message=message), 404

  return render_template('militares/editar_militar.html',title="Editar Militar Page",year=datetime.now().year, militar=obj, patentes=patentes, message=message)

@app.route('/eliminarmilitar/<id>', methods=['GET', 'POST'])
def eliminarmilitar(id):
  if is_submitted(request):
    if request.method == 'POST' :
      if bool(Militar.Delete('ID', id)):
        flash("Militar %s: eliminado com sucesso."%(id), "danger")
      else:
        flash("Invalid: Every field is required.", "danger")

  return redirect(url_for('militares'))


# Patente Routes
@app.route('/patentes')
def patentes():
  patentes = Patente.Patentes()
  return render_template("patentes/patentes.html",titulo="Patentes",year=datetime.now().year,patentes=patentes)

@app.route('/inserirpatente', methods=['GET', 'POST'])
def inserirpatente():
  # you must tell the variable 'form' what you named the class, above
  # 'form' is the variable name used in this template: index.html
  form = request.form
  message = ""

  if is_submitted(request):
    ID = form.get('txtID')
    NOME = form.get('txtNome')
    INICIAIS = form.get('txtIniciais')

    obj = Patente(ID,NOME,INICIAIS)
    patente = Patente.Inserir(obj)
    if patente:
      flash("Success: Info added successfully.", "success")
      return redirect( url_for('patentes') )
    else:
      flash("Invalid: Every field is required.", "danger")
      return render_template('404.html', message=message), 404

  return render_template('patentes/inserir_patente.html',title="Inserir Patente Page",year=datetime.now().year, message=message)

@app.route('/verpatente/<id>')
def verpatente(id):
  # run function to get patente data based on the id in the path
  patente = Patente()
  result, obj = patente.Get(id=id)

  if result:
    # pass all the data for the selected patente to the template
    return render_template('patentes/ver_patente.html', title = "Ver Patente Page", year = datetime.now().year, patente=obj)
  else:
    # redirect the browser to the error template
    return render_template('404.html'), 404

@app.route('/editarpatente/<id>', methods=['GET', 'POST'])
def editarpatente(id):
  # return render_template("index.html",title="Home Page",year=datetime.now().year)
  patente = Patente()
  result, obj = patente.Get(id)

  if result:
    form = request.form
    message = ""
    if is_submitted(request):
      ID = id
      NOME = form.get('txtNome')
      INICIAIS = form.get('txtIniciais')

      patente = Patente(ID,NOME,INICIAIS)
      result = patente.Update()
      if result:
        flash("Success: Info updated successfully.", "success")
        return redirect( url_for('patentes') )
      else:
        flash("Invalid: Every field is required.", "danger")
        return render_template('404.html', message=message), 404

  return render_template('patentes/editar_patente.html',title="Editar Patente Page",year=datetime.now().year, patente=obj, message=message)

@app.route('/eliminarpatente/<id>', methods=['GET', 'POST'])
def eliminarpatente(id):
  if is_submitted(request):
    if request.method == 'POST' :
      if bool(Patente.Delete(id)):
        flash("Patente %s: eliminado com sucesso."%(id), "danger")
      else:
        flash("Invalid: Every field is required.", "danger")

  return redirect(url_for('patentes'))

@staticmethod
def is_submitted(request):
  """Consider the form submitted if there is an active request and
  the method is ``POST``, ``PUT``, ``PATCH``, or ``DELETE``.
  """
  return bool(request) and request.method in SUBMIT_METHODS


# Cosmos DB
# Militar Routes
@app.route('/cosmosmilitares')
def cosmosmilitares():
  militares = []
  cosmos_militares = CosmosBbRead.GetAll(COSMOSDBENDPOINT, COSMOSDBKEY, 'dbmilitar','cmilitar')
  for cosmos_militar in cosmos_militares:
    militares.append(parse_cosmos_militar_to_militar(cosmos_militar))

  return render_template('cosmos/militares/militares.html',titulo='Militares',year=datetime.now().year,militares=militares,accountstorage=ACCOUNTSTORAGE,blobcontainer=BLOBCONTAINER)

@app.route('/inserircosmosmilitar', methods=['GET', 'POST'])
def inserircosmosmilitar():
  # you must tell the variable 'form' what you named the class, above
  # 'form' is the variable name used in this template: index.html
  form = request.form
  message = ""
  patentes = Patente.Patentes()

  if is_submitted(request):
    file = request.files['fupload']
    filename = file.filename
    if filename:
      if allowed_file(filename):
        file.stream.seek(0)
        file_data = file.read()
        Blobs.blobupload(BLOBCONNECTIONSTRING, BLOBCONTAINER, filename, file_data)
      else:
        flash("Invalid: File extension.", "danger")
        return render_template('404.html', message=message), 404

    ID = ''
    FOTO = filename
    NIM = form.get('txtNIM')
    CC = form.get('txtCC')
    NOME = form.get('txtNome')
    APELIDO =form.get('txtApelido')
    PATENTE = form.get('txtPatente')
    IDADE = form.get('txtIdade')

    obj = Militar(ID,FOTO,NIM,PATENTE,CC,NOME,APELIDO,IDADE, IsCosmos=True)
    send_obj = obj.ToCosmosDicionario()
    print('#############################################################################################')
    print(send_obj)

    result = CosmosBbWrite.Upsert(COSMOSDBENDPOINT, COSMOSDBKEY, 'dbmilitar', 'cmilitar', send_obj)

    if result:
      flash("Success: Info added successfully.", "success")
      return redirect( url_for('cosmosmilitares') )
    else:
      flash("Invalid: Every field is required.", "danger")
      return render_template('404.html', message=message), 404

  return render_template('cosmos/militares/inserir_militar.html',title="Inserir Militar Page",year=datetime.now().year, patentes=patentes, message=message)

@app.route('/vercosmosmilitar/<id>')
def vercosmosmilitar(id):
  # run function to get militar data based on the id in the path
  result, cosmos_militar = CosmosBbRead.Get(COSMOSDBENDPOINT, COSMOSDBKEY, 'dbmilitar','cmilitar','id', id)

  if result:
    militar = parse_cosmos_militar_to_militar(cosmos_militar)
    # pass all the data for the selected militar to the template
    return render_template('cosmos/militares/ver_militar.html', title = "Ver Militar Page", year = datetime.now().year, militar=militar)
  else:
    # redirect the browser to the error template
    return render_template('404.html'), 404

@app.route('/editarcosmosmilitar/<id>', methods=['GET', 'POST'])
def editarcosmosmilitar(id):
  # return render_template("index.html",title="Home Page",year=datetime.now().year)
  patentes = Patente.Patentes()
  militar = Militar()
  result, militar = CosmosBbRead.Get(COSMOSDBENDPOINT, COSMOSDBKEY, 'dbmilitar','cmilitar','id', id)

  if result:
    form = request.form
    message = ""
    if is_submitted(request):
      file = request.files['fupload']
      filename = file.filename
      if filename:
        if allowed_file(filename):
          Blobs.blobupload(BLOBCONNECTIONSTRING, BLOBCONTAINER)
        else:
          flash("Invalid: File extension.", "danger")
          return render_template('404.html', message=message), 404

      ID = id
      FOTO = ''
      NIM = form.get('txtNIM')
      CC = form.get('txtCC')
      NOME = form.get('txtNome')
      APELIDO =form.get('txtApelido')
      PATENTE = form.get('txtPatente')
      IDADE = form.get('txtIdade')

      obj = Militar(ID,FOTO,NIM,PATENTE,CC,NOME,APELIDO,IDADE)
      send_obj = obj.ToCosmosDicionario()

      print('#############################################################################################')
      print(send_obj)

      result = CosmosBbWrite.Upsert(COSMOSDBENDPOINT, COSMOSDBKEY, 'dbmilitar', 'cmilitar', send_obj)

      if result:
        flash("Success: Info updated successfully.", "success")
        return redirect( url_for('cosmosmilitares') )
      else:
        flash("Invalid: Every field is required.", "danger")
        return render_template('404.html', message=message), 404

  return render_template('cosmos/militares/editar_militar.html',title="Editar Cosmos Militar Page",year=datetime.now().year, militar=militar, patentes=patentes, message=message)

@app.route('/eliminarcosmosmilitar/<id>', methods=['GET', 'POST'])
def eliminarcosmosmilitar(id):
  if is_submitted(request):
    if request.method == 'POST' :
      result, militar = CosmosBbRead.Get(COSMOSDBENDPOINT, COSMOSDBKEY, 'dbmilitar','cmilitar','id', id)
      result = CosmosBbDelete.Delete(COSMOSDBENDPOINT, COSMOSDBKEY, 'dbmilitar', 'cmilitar', 'id', militar)

      if bool(result):
        flash("Militar %s: eliminado com sucesso."%(id), "danger")
      else:
        flash("Invalid: Every field is required.", "danger")

  return redirect(url_for('cosmosmilitares'))

def allowed_file(filename):
  return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def parse_cosmos_militar_to_militar(cosmos_militar):
  ID = cosmos_militar['id']
  FOTO = cosmos_militar.get('Foto')
  NIM = cosmos_militar['NIM']
  CC = cosmos_militar['CC']
  NOME = cosmos_militar['Nome']
  APELIDO = cosmos_militar['Apelido']
  PATENTE = cosmos_militar['Patente']
  IDADE = cosmos_militar['Idade']

  return Militar(ID, FOTO, NIM, PATENTE, CC, NOME, APELIDO, IDADE, IsCosmos=True)