import sqlite3

connection = sqlite3.connect('todo.db')

def create_table(connection):
    try:
        cur = connection.cursor()
        cur.execute('''CREATE TABLE task(task text)''')
    except:
        pass

def show_task(connection):
    cur = connection.cursor()
    cur.execute('''SELECT rowid, task FROM task''')
    result = cur.fetchall()

    for row in result:
        print(str(row[0]) + ' - ' + row[1])

def add_task(connection):
    print('dodaj zadanie')
    task = input('Wpisz treść zadania: ')
    if task == '0':
        print('Powrót do menu')
    else:
        cur = connection.cursor()
        cur.execute('''INSERT INTO task(task) VALUES(?)''', (task,))
        connection.commit()
        print('Dodano zadanie')

def delete_task(connection):
    task_index = int(input('Podaj numer zadania do usunięcia: '))

    cur = connection.cursor()
    rows_deleted = cur.execute('''DELETE FROM task WHERE rowid=?''', (task_index,)).rowcount

    connection.commit()
    if rows_deleted == 0:
        print('takie zadanie nie istnieje')
    else:
        print('Usunięto zadanie')

create_table(connection)

while True:
    print()
    print('1. Pokaż zadania')
    print('2. Dodaj zadanie')
    print('3. Usuń zadanie')
    print('4. Zakończ program')

    user_choice = int(input('Wybierz opcję: '))
    print()

    if user_choice == 1:
        show_task(connection)

    if user_choice == 2:
        add_task(connection)

    if user_choice == 3:
        delete_task(connection)

    if user_choice == 4:
        break

connection.close()