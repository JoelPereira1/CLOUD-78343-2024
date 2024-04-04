import modules.databases.db_executions as DbExecutions

# Module DbRead
def Get(database, table, column, id):
  sql="SELECT * FROM %s WHERE %s =%s"%(table,column,id)
  sql=sql.format(table,column,id)
  result,values = DbExecutions.SQLLiteExecute(database, sql)
  if result:
    return result,values

@staticmethod
def GetAll(database, table):
    sql="SELECT * FROM %s"%(table)
    result,values = DbExecutions.SQLLiteExecute(database, sql)
    return result,values