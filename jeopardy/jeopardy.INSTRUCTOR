1. Make sure everyone is familiar with Jeopardy and how clues work.

2. Run jeopardy.py. Open jeopardy.py and get a general sense of where
in the code the three examples are getting printed.

3. Talk about databases, including: why they are useful, how data is
often structured in a relational database, the notion of declarative
versus imperative programming. Relate the utility of database to what
can be accomplished in a spreadsheet.

4. Start sqlite and look at the schema for the category and clue
tables:

sqlite> .table
category  clue
sqlite> .schema category
CREATE TABLE "category" (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    game INTEGER NOT NULL,
    boardPosition INTEGER
    );
sqlite> .schema clue
CREATE TABLE "clue" (
    id INTEGER PRIMARY KEY,
    text VARCHAR(255) NOT NULL,
    category_id INTEGER NOT NULL,
    value INTEGER NOT NULL,
    answer VARCHAR(255) NOT NULL,
    round INTEGER
);

Explain what a schema is, and what kinds of data types SQLite
has. Explain what a primary key is and why they are useful.

5. EXERCISE: Make some simple SELECT queries from the sqlite prompt.

SELECT * FROM category;
SELECT NAME FROM category;
SELECT * FROM clue;
SELECT text, answer, value FROM clue;
SELECT text, answer, value FROM clue LIMIT 10;

Give people time to explore simple SELECTs.

6. Walk through setting up the database connection, executing the
first SELECT query, and retrieving and printing the results.

7. Walk through executing the second SELECT query and retrieving and
printing the results. Review how string formatting works.

8. Explain JOINs and why they are useful. Explain WHERE clauses. Walk
through the third SELECT query, which uses a JOIN.
