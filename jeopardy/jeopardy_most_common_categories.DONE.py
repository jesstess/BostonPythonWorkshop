from pysqlite2 import dbapi2 as sqlite

connection = sqlite.connect('jeopardy.db')
cursor = connection.cursor()

cursor.execute("SELECT name, COUNT(name) AS count FROM category \
GROUP BY name ORDER BY count DESC LIMIT 20")
results = cursor.fetchall()

for name, count in results:
    print count, name
