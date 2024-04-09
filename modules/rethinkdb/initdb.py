# RETHINKDB
# from rethinkdb import RethinkDB


# @staticmethod
# def init_database(database, table):
#   try:
#     r = RethinkDB()
#     r.connect('rethinkdb', 28015).repl()
#     r.db(database).table_create(table).run()
#     print('Table %s created successfully'%(table))
#   except:
#     pass
#   finally:
#     return r
#     # if conn:
#     #   conn.close()


from rethinkdb import r

@staticmethod
def init_database(host, port, database, password, table):
  try:
    connection = connect(host, port, database, password)
    r.table_create(table).run(connection)
    print('Table %s created successfully'%(table))
  except:
    pass
  finally:
    return r
    # if conn:
    #   conn.close()

@staticmethod
def connect(host, port, database, password):
  return r.connect(host=host, port=port, db=database, password=password)