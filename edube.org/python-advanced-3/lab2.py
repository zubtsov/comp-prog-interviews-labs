# https://edube.org/learn/pcpp1-5/lab-sqlite3-lab-2
import sqlite3

DATABASE_NAME = 'todo.db'

import sqlite3


class Todo:
    @staticmethod
    def __validate_priority(priority):
        assert priority >= 1, "A task priority can't be less than 1"

    def __enter__(self):
        self.conn = sqlite3.connect('todo.db')
        self.conn.__enter__()
        self.create_task_table()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.__exit__(exc_type, exc_val, exc_tb)

    def create_task_table(self):
        self.conn.cursor().execute('''CREATE TABLE IF NOT EXISTS tasks (
                     id INTEGER PRIMARY KEY,
                     name TEXT NOT NULL,
                     priority INTEGER NOT NULL
                     );''')

    def add_task(self):
        name = input('Enter task name: ')
        assert len(name.strip()) != 0, "A task name can't be an empty string"
        assert self.find_task(name) is None, "Can't use the same task name again"
        priority = int(input('Enter priority: '))
        self.__validate_priority(priority)

        self.conn.cursor().execute('INSERT INTO tasks (name, priority) VALUES (?,?)', (name, priority))
        self.conn.commit()

    def change_priority(self):
        task_id = int(input('Enter task id: '))
        new_priority = int(input('Enter the new priority for the task: '))
        self.__validate_priority(new_priority)
        self.conn.cursor().execute('''UPDATE tasks SET priority = ? WHERE id = ?''', (new_priority, task_id))
        self.conn.commit()

    def delete_task(self):
        task_id = int(input('Enter task id: '))
        self.conn.cursor().execute('''DELETE FROM tasks WHERE id = ?''', (task_id,))
        self.conn.commit()

    def find_task(self, task_name):
        return self.conn.cursor().execute('''
        SELECT id, name, priority
        FROM tasks
        WHERE name = ?
        ''', (task_name,)).fetchone()

    def show_tasks(self):
        print('id'.ljust(5), 'name'.ljust(15), 'priority'.ljust(5), sep='|')
        print('-' * 27)
        for id, name, priority in self.conn.cursor().execute('''SELECT id, name, priority FROM tasks'''):
            print(str(id).ljust(5), name.ljust(15), str(priority).ljust(5), sep='|')

    def show_menu(self):
        return input('''
1. Show Tasks 
2. Add Task 
3. Change Priority 
4. Delete Task
5. Exit
Choose your option: ''')


if __name__ == '__main__':
    with Todo() as app:
        while True:
            choice = app.show_menu().strip()
            if choice == "1":
                app.show_tasks()
            elif choice == "2":
                app.add_task()
            elif choice == "3":
                app.change_priority()
            elif choice == "4":
                app.delete_task()
            elif choice == "5":
                break
            else:
                print('Unknown option, try again please')
