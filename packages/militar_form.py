# from packages.form import *
# from packages.form import _required

class MilitarForm:

  def form_fields(form, id = '', filename = ''):
    ID = id
    FOTO = filename
    NIM = form.get('txtNIM')
    CC = form.get('txtCC')
    NOME = form.get('txtNome')
    APELIDO =form.get('txtApelido')
    PATENTE = form.get('txtPatente')
    IDADE = form.get('txtIdade')

    # MilitarForm.validation(form)

    return ID, FOTO, NIM, CC, NOME, APELIDO, PATENTE, IDADE

  def validation(form):
    breakpoint()
    return Exception.__init__('aa')
