import sqlite3
answer = "0"

def menu():
    print("")
    print("1. Display All Contacts")
    print("2. Add New Contact")
    print("3. Edit Existing Contact")
    print("4. Display SQLite Database Verion")
    print("")

    answer=input("What do you want to do?  ")
    while (answer != "1") and (answer != "2") and (answer != "3") and (answer != "4"):
        print("Invalid Options Selected: " + answer)
        answer=input("What do you want to do?  ")
    if int(answer) == 1:
        display_all_contacts()
    elif int(answer) == 2:
        print("You Selected Option 2")
    elif int(answer) == 3:
        print("You Selected Option 3")
    else:
        connect_to_database()

def display_all_contacts():
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * from contacts''')
    result = cursor.fetchall();
    print(result)

def connect_to_database():
    try:
        sqliteConnection = sqlite3.connect('contacts.db')
        cursor = sqliteConnection.cursor()
        print("Database created and Successfully Connected to SQLite")
        sqlite_select_Query = "select sqlite_version();"
        cursor.execute(sqlite_select_Query)
        record = cursor.fetchall()
        print("SQLite Database Version is: ", record)
        cursor.close()
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

menu()
