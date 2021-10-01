import datetime
import sqlite3
import plotly.express as px

from sqlite3 import Error


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful\n")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


con = create_connection('expense_tracker.sqlite')


def execute_query(connection, query, variable=''):
    cur = con.cursor()
    try:
        cur.execute(query, variable)
        connection.commit()
        print('Query executed successful\n')
    except Error as e:
        print(f'The error {e} occured')


create_entry_table = '''CREATE TABLE IF NOT EXISTS entry (
    entry_id INTEGER PRIMARY KEY,
    amount REAL NOT NULL,
    category TEXT NOT NULL,
    date REAL NOT NULL,
    description TEXT NOT NULL
);
'''

execute_query(con, create_entry_table)


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f'Error {e} occured')


select_entry = "SELECT * from entry"
print('Datubāzē esošie izdevumu ieraksti:\n')
entries = execute_read_query(con, select_entry)
for entry in entries:
    print(entry)

categories = ['Pārtika', 'Saimniecības izdevumi', 'Izglītība', 'Auto izdevumi']


def addCategorie(categorie):
    categories.append(categorie)
    return categories


def addExpense():

    expense = float(input('Lūdzu ievadiet naudas summu: '))

    print('Izdevumu kategorijas: ')
    for l in range(len(categories)):
        print(f"{l}: {categories[l]}")
    selectCategory = categories[int(input(f"Lūdzu izvēlaties kategoriju: "))]
    date = datetime.date.today().strftime("%d.%m.%Y")
    description_1 = input('Lūdzu ievadiet tēriņa aprakstu: ')

    add_expense_query = '''INSERT INTO entry
            (amount, category, date, description)
            VALUES (?, ?, ?, ?);'''

    execute_query(con, add_expense_query,
                  (expense, selectCategory, date, description_1))
    entries = execute_read_query(con, select_entry)
    for entry in entries:
        print(entry)
    return expense, selectCategory, date, description_1


def readQueries():
    query = "SELECT * from entry"
    expenses = execute_read_query(con, query)
    for entry in expenses:
        print(entry)
    return expenses


def deleteEntry():
    print('Datubāzē mums ir sekojoši ieraksti: ')
    readQueries()
    id = input('Lūdzu izvēlieties ieraksta numuru pēc kārtas: ')
    delQuery = 'DELETE FROM entry WHERE entry_id = ?'
    execute_query(con, delQuery, (id,))


def showExpense():
    expenses = readQueries()
    expensesNew = []
    valuesNew = []
    for i in expenses:
        expensesNew.append(i[1])
    for i in expenses:
        valuesNew.append(i[2])

    fig = px.pie(values=expensesNew, names=valuesNew, title='Izmaksu uzskaite')
    fig.show()


def chooseMenu():
    print('\nVeicamās darbības: \n 1: Ievadīt tēriņus \n 2: Attēlot tēriņus \n 3: Dzēst ierakstu \n 4: Uzstādījumi \nLai izietu spiediet Ctrl+C')
    userInput = int(input('Lūdzu ievadiet darbības numuru: '))
    if userInput == 1:
        addExpense()
    if userInput == 2:
        showExpense()
    if userInput == 3:
        deleteEntry()
    if userInput == 4:
        print('Piejamās darbības: \n 1: Pievienot kategoriju')
        actInput = int(input('Lūdzu ievadiet darbības numuru: '))
        if actInput == 1:
            catInput = input('Lūdzu ievadiet kategorijas nosaukumu: ')
            addCategorie(catInput)


while True:
    chooseMenu()
