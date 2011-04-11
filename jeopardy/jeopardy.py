from pysqlite2 import dbapi2 as sqlite

connection = sqlite.connect('jeopardy.db')
cursor = connection.cursor()

cursor.execute("SELECT name FROM category LIMIT 10")
results = cursor.fetchall()

print "Example categories:\n"
for category in results:
    print category[0]

cursor.execute("SELECT text, answer, value FROM clue LIMIT 10")
results = cursor.fetchall()

print "\nExample clues:\n"
for clue in results:
    text, answer, value = clue
    print "[$%s]" % (value,)
    print "A: %s" % (text,)
    print "Q: What is '%s'" % (answer,)
    print ""

cursor.execute("SELECT category.name, clue.text, clue.answer \
FROM clue, category WHERE clue.category=category.id \
AND category.name LIKE '%MYTHOLOGY%' LIMIT 10")
results = cursor.fetchall()

print "\nExample MYTHOLOGY clues:\n"
for clue in results:
    name, text, answer = clue
    print "In the category of %s" % (name,)
    print "A: %s" % (text,)
    print "Q: What is '%s'" % (answer,)
    print ""
