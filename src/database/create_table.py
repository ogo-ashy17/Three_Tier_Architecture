import psycopg2

connection = psycopg2.connect(
    dbname='test_db',
    user='dgmr2',
    # password='your_password',
    host='localhost',
    port='5432'
)

connection.autocommit = True

cursor = connection.cursor()

sql = '''
    CREATE TABLE users (
        id uuid,
        name text,
        birthday date
    );
'''

cursor.execute(sql)
# connection.commit()
cursor.close()