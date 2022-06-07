import sqlite3

def getUniversityInfo(id):
    try:
        sqliteConnection = sqlite3.connect('bot_db.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT * from UniversityDB where id = ?"""
        cursor.execute(sqlite_select_query, (id, ))
        records = cursor.fetchall()
        for row in records:
            print("Id: ", row[0])
            print("Name: ", row[1])
            print("Country: ", row[2])
            print("City: ", row[3])
            print("Tuition cost: ", row[4])
            print("\n")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

getUniversityInfo(2)