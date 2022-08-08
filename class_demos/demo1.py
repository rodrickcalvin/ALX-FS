import psycopg2

connection = psycopg2.connect('dbname=alx')

# Open a cursor to perform database operations
cur = connection.cursor()


cur.execute('DROP TABLE IF EXISTS table2;')


# create table2 using the execute method
cur.execute('''
  CREATE TABLE table2 (
    id INTEGER PRIMARY KEY,
    completed BOOLEAN NOT NULL DEFAULT False
  );
''')


# Add a record to the table2
cur.execute('INSERT INTO table2 (id, completed) VALUES (1, True);')


# Add another record
cur.execute('INSERT INTO table2 (id, completed) VALUES (%s, %s);', (2, True))

# declare variables SQL & data
SQL = 'INSERT INTO table2 (id, completed) VALUES (%(id)s, %(completed)s);'

data = {
  'id': 3,
  'completed': False
}

# Add a record using declared variables
cur.execute(SQL, data)

cur.execute('SELECT * from table2;')

table_2 = cur.fetchall()

# cur.fetchmany(5)  -- Fetches first 5 items
# cur.fetchone()  -- Fetches first item

# The fetch methods all work depending on the SELECT statement

print(table_2)

connection.commit()
connection.close()
cur.close()


