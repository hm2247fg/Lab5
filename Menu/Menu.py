"""
A menu - you need to add the database and fill in the functions.
"""

# imports the SQLite3 module, establishes a connection to a SQLite database file named
# 'chainsaw_juggling_records.db', and creates a cursor object for executing SQL commands
import sqlite3

conn = sqlite3.connect('chainsaw_juggling_records.db')
cursor = conn.cursor()

# Create a database table to store chainsaw juggling records
# NOT NULL means that the column must always contain a value and cannot have a NULL
cursor.execute('''
    CREATE TABLE IF NOT EXISTS chainsaw_juggling_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,  
        country TEXT NOT NULL,
        catches INTEGER NOT NULL
    )
''')

# Commit the changes and close the connection
# conn.commit()
# conn.close()

example_data = [
    ('Janne Mustonen', 'Finland', 98),
    ('Ian Stewart', 'Canada', 94),
    ('Aaron Greg', 'Canada', 88),
    ('Chad Taylor', 'USA', 78)
]

cursor.executemany('''
    INSERT INTO chainsaw_juggling_records (name, country, catches)
    VALUES (?, ?, ?)''', example_data)

conn.commit()
# conn.close()


def main():
    menu_text = """
    1. Display all records
    2. Search by name
    3. Add new record
    4. Edit existing record
    5. Delete record 
    6. Quit
    """

    while True:
        print(menu_text)
        choice = input('Enter your choice: ')
        if choice == '1':
            display_all_records()
        elif choice == '2':
            search_by_name()
        elif choice == '3':
            add_new_record()
        elif choice == '4':
            edit_existing_record()
        elif choice == '5':
            delete_record()
        elif choice == '6':
            break
        else:
            print('Not a valid selection, please try again')


def display_all_records():
    cursor.execute('SELECT * FROM chainsaw_juggling_records')
    records = cursor.fetchall()

    for record in records:
        print(record)

    # conn.commit()
    # conn.close()


# ask user for a name, and print the matching record if found
# What should the program do if the name is not found?
def search_by_name():
    name = input('Enter the name to search: ')
    cursor.execute('SELECT * FROM chainsaw_juggling_records '
                   'WHERE name = ?', (name,))
    record = cursor.fetchall()

    if record:
        print(record)
    else:
        print(f"No record found for {name}")

    # conn.commit()
    # conn.close()


# add new record
# What if user wants to add a record that already exists
def add_new_record():
    name = input('Enter the name: ')
    country = input('Enter the country: ')
    catches = int(input('Enter the number of catches: '))

    # Check if the record already exists
    cursor.execute('SELECT * FROM chainsaw_juggling_records WHERE name = ?',
                   (name, ))
    existing_record = cursor.fetchall()

    if existing_record:
        print(f"Record for {name} already exists.")
    else:
        cursor.execute('INSERT INTO chainsaw_juggling_records (name, country, catches) VALUES (?, ?, ?)', (name, country, catches))
        print(f"Record for {name} added successfully.")

    # conn.commit()
    # conn.close()


# edit existing record
# What if user wants to edit record that does not exist?
def edit_existing_record():
    name = input('Enter the name to edit: ')
    existing_record = cursor.fetchall()

    if existing_record:
        new_catches = int(input('Enter the new number of catches: '))
        cursor.execute('UPDATE chainsaw_juggling_records SET catches = ? WHERE name = ?', (new_catches, name))
        print(f"Record for {name} updated successfully.")
    else:
        print(f"No record found for {name}")

    # conn.commit()
    # conn.close()


# delete existing record
# What if user wants to delete record that does not exist
def delete_record():
    name = input('Enter the name to delete: ')

    # Execute SELECT query to check if the record exists
    cursor.execute('SELECT * FROM chainsaw_juggling_records WHERE name = ?', (name,))
    existing_record = cursor.fetchall()

    # If the record exists, execute DELETE query
    if existing_record:
        cursor.execute('DELETE FROM chainsaw_juggling_records WHERE name = ?', (name,))
        print(f"Record for {name} deleted successfully.")
    else:
        print(f"No record found for {name}")

    # Uncomment the following lines if you want to close the connection:
    # conn.commit()
    # conn.close()


if __name__ == '__main__':
    main()