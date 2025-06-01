import sqlite3

sql = """
DROP TABLE IF EXISTS Roster;

CREATE TABLE Roster(Name TEXT, Species TEXT, Age INT);

INSERT INTO Roster VALUES
('Benjamin Sisko', 'Human', 40),
('Jadzia Dax', 'Trill', 300),
('Kira Nerys', 'Bajoran', 29);

UPDATE Roster SET Name = 'Ezri Dax' WHERE Name = 'Jadzia Dax';
"""

with sqlite3.connect("roster.db") as con:
    cursor = con.cursor()
    cursor.executescript(sql)
    cursor.execute("SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'")
    for row in cursor.fetchall():
        print(row)
    cursor.execute("DELETE FROM Roster WHERE Age > 100")
    cursor.execute("ALTER TABLE Roster ADD COLUMN Rank TEXT")
    ranks = {
        'Benjamin Sisko': 'Captain',
        'Ezri Dax': 'Lieutenant',
        'Kira Nerys': 'Major'
    }
    for name, rank in ranks.items():
        cursor.execute("UPDATE Roster SET Rank = ? WHERE Name = ?", (rank, name))
    cursor.execute("SELECT Name, Age, Rank FROM Roster ORDER BY Age DESC")
    for row in cursor.fetchall():
        print(row)