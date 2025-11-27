import uuid
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
    INSERT INTO users 
    (id, name, birthday) values (%s, %s, %s)
'''

cursor.execute(sql, (str(uuid.uuid4()), 'ogo-ashy17', '2002-11-29'))
cursor.execute(sql, (str(uuid.uuid4()), 'Xiáng', '1990-08-06'))

# connection.commit()
cursor.close()