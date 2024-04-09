from rethinkdb import r
import modules.rethinkdb.initdb as InitDatabase

# Module DbRead
@staticmethod
def GetAll(database, table, ref_col, ref_id, order_col, limit = False, limit_num = 3, limit_col = None):
  connection = InitDatabase.connect('rethinkdb', 28015, database, 'Passw0rd!')
  if limit:
    return print() if limit_col == None else r.table(table).filter(r.row['%s'%(ref_col)] > ref_id).order_by(order_col).limit(limit_num).changes() #r.table(table).orderBy(order_col).limit(limit_num).changes()
  elif ref_col:
    r.table(table).filter(r.row['%s'%(ref_col)] > ref_id).order_by(order_col).changes()
  else:
    r.table(table).order_by(order_col).changes()

    # r.db("Test").table('Users').getAll(r.args(r.db('Test').table('Users').get("0ab43d81-b883-424a-be56-32f9ff98f7d2")('friends'))).changes()