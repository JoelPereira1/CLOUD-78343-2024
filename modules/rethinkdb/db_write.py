from rethinkdb import r
import modules.rethinkdb.initdb as InitDatabase

# Module BbWrite:
def Insert(database, table, obj):
  connection = InitDatabase.connect('rethinkdb', 28015, database, 'Passw0rd!')
  result = r.table(table).insert(obj).run(connection)
  return result