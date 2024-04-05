import modules.databases.db_executions as DbExecutions

# Module BbWrite:
def Inserir(database, table, obj):
  result,coltypes = DbExecutions.SQLLiteColsTypes(database, table)
  insert_cols_string, insert_vals_string = format_sql_query(obj, coltypes, 'ID')

  sql = "INSERT INTO {table} ({insert_cols_string}) VALUES ({insert_vals_string})"
  sql=sql.format(table=table,insert_cols_string=insert_cols_string,insert_vals_string=insert_vals_string)

  result,values = DbExecutions.SQLLiteExecute(database, sql, False)
  return result

def Update(database, table, col, obj):
  # result,colnames = DbExecutions.SQLLiteGetTableCols(database, table)
  result,coltypes = DbExecutions.SQLLiteColsTypes(database, table)
  if result:
    update_string, where_string = format_sql_query(obj, coltypes, col, False)

    sql="UPDATE {table} SET {update_columns} WHERE {where_col}"
    sql=sql.format(table=table,update_columns=update_string,where_col=where_string)

    result,values = DbExecutions.SQLLiteExecute(database, sql, False)
    return result

# TODO| check if possible with autoincrement column
def Upsert(database, table, col, obj):
  # result,colnames = DbExecutions.SQLLiteGetTableCols(database, table)
  result,coltypes = DbExecutions.SQLLiteColsTypes(database, table)
  if result:
    update_string, where_string = format_sql_query(obj, coltypes, col, False)
    insert_cols_string, insert_vals_string = format_sql_query(obj, coltypes, col)

    sql="INSERT INTO {table} ({insert_cols_string}) VALUES ({insert_vals_string}) ON CONFLICT({col}) DO UPDATE SET {update_columns}"
    sql=sql.format(table=table,insert_cols_string=insert_cols_string,insert_vals_string=insert_vals_string,update_columns=update_string,where_col=where_string, col=col)
    print('############################################')
    print(sql)
    print('############################################')
    result,values = DbExecutions.SQLLiteExecute(database, sql, False)
    return result

def format_sql_query(obj, coltypes, col='', isInsert=True):
  obj_dict = obj.ToSqlDicionario()
  first_sql_block = ''
  second_sql_block = ''

  for db_col in obj_dict:
    if db_col != col:
      if isInsert:
        first_sql_block += '%s, '%(db_col)
      else:
        second_sql_block = '%s=%s'%(col,obj_dict[col])

      for col_type in coltypes:
        if col_type[0] == db_col:
            if col_type[1] == 'INTEGER':
              if isInsert:
                second_sql_block += '%s, '%(obj_dict[db_col])
              else:
                first_sql_block += '%s=%s, '%(db_col, obj_dict[db_col])
            else:
              if isInsert:
                second_sql_block += "'%s', "%(obj_dict[db_col])
              else:
                first_sql_block += "%s='%s', "%(db_col, obj_dict[db_col])

  first_sql_block = first_sql_block[:-2]
  if isInsert:
    second_sql_block = second_sql_block[:-2]
  return first_sql_block, second_sql_block