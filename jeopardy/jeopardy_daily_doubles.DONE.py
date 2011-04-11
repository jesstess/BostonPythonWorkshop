from pysqlite2 import dbapi2 as sqlite

connection = sqlite.connect('jeopardy.db')
cursor = connection.cursor()

# Simplest is
#     SELECT text, answer FROM clue WHERE isDD=1 LIMIT 10
# but it's nice to have the category:

cursor.execute("SELECT ca.name, cl.text, cl.answer \
FROM clue cl, category ca WHERE cl.category=ca.id AND cl.isDD=1 LIMIT 10")
results = cursor.fetchall()

for result in results:
    category_name, text, answer = result
    print category_name
    print text
    print answer
    print "==="
