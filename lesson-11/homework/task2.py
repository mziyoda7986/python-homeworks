import sqlite3

sql = """
DROP TABLE IF EXISTS Books;

CREATE TABLE Books(Title TEXT, Author TEXT, Year_Published INT, Genre TEXT);

INSERT INTO Books VALUES
('To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction'),
('1984', 'George Orwell', 1949, 'Dystopian'),
('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Classic');

UPDATE Books SET Year_Published = 1950 WHERE Title = '1984';
"""

with sqlite3.connect("library.db") as con:
    cursor = con.cursor()
    cursor.executescript(sql)
    cursor.execute("SELECT Title, Author FROM Books Where Genre = 'Dystopian'")
    for row in cursor.fetchall():
        print(row)
    cursor.execute("DELETE FROM Books WHERE Year_Published < 1950")
    cursor.execute("ALTER TABLE Books ADD COLUMN Rating REAL")
    rating = {
        'To Kill a Mockingbird' : 4.8,
        '1984' : 4.7,
        'The Great Gatsby' : 4.5
    }
    for title, rate in rating.items():
        cursor.execute("UPDATE Books SET Rating = ? WHERE Title = ?", (rate, title))
    cursor.execute("SELECT Title, Author, Year_Published, Genre, Rating FROM Books ORDER BY Year_Published ASC")
    for row in cursor.fetchall():
        print(row)