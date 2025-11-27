import psycopg2

connection = psycopg2.connect(
    dbname='postgres',
    user='dgmr2',
    # password='your_password',
    host='localhost',
    port='5432'
)

connection.autocommit = True

cursor = connection.cursor()

sql = '''CREATE database test_db;'''

cursor.execute(sql)
# connection.commit()
cursor.close()