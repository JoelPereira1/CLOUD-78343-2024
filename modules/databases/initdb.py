import sqlite3
from sqlite3 import Error

@staticmethod
def init_database(database, table_objects=[]):
  # For each table object [{table_name: [columns and definitions]},.....]
  for table_object in table_objects:
    # For each table object {table_name: [columns and definitions]}
    for table in table_object:
      # get table and check is existence
      check_sql = """
        SELECT name FROM sqlite_master WHERE type='table' AND name='%s';
      """%(table)

      # buils the sql to cerate table, tansform the value [columns and definitions] into sql string create table
      delimiter = '\n,'
      cols = delimiter.join(table_object[table])
      sql= """
      CREATE TABLE %s (
        %s
        );
      """%(table, cols)

      try:
        conn = sqlite3.connect(database)
        cur = conn.cursor()
        cur.execute(check_sql)
        exists = bool(cur.fetchone())
        if not exists:
          c = conn.cursor()
          c.execute(sql)
          conn.commit()
          print('Table %s created successfully'%(table))
      except:
        pass
      finally:
        if conn:
          conn.close()
