from pysqlite2 import dbapi2 as sqlite

connection = sqlite.connect('jeopardy.db')
cursor = connection.cursor()

cursor.execute("SELECT id, name FROM category ORDER BY RANDOM() LIMIT 1")
results = cursor.fetchall()
category_id, name = results[0]
print name

cursor.execute("SELECT value, text FROM clue WHERE category=%s \
ORDER BY value" % (category_id,))
results = cursor.fetchall()
for result in results:
    value, text = result
    print "[$%s] %s" % (value, text)
