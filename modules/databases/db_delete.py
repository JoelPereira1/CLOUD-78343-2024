import modules.databases.db_executions as DbExecutions

# Module DbDelete
@staticmethod
def Delete(database, table, col, id):
  sql="DELETE FROM {table} WHERE {1}={0}"
  sql=sql.format(id,col,table=table)
  result,values = DbExecutions.SQLLiteExecute(database, sql, False)
  return result