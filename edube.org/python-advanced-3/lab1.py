# https://edube.org/learn/pcpp1-5/lab-sqlite3-lab-1
import sqlite3

DATABASE_NAME = 'todo.db'

import sqlite3


class Todo:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.c = self.conn.cursor()
        self.create_task_table()

    def create_task_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                     id INTEGER PRIMARY KEY,
                     name TEXT NOT NULL,
                     priority INTEGER NOT NULL
                     );''')

    def add_task(self):
        name = input('Enter task name: ')
        assert len(name.strip()) != 0, "A task name can't be an empty string"
        assert self.find_task(name) is None, "Can't use the same task name again"
        priority = int(input('Enter priority: '))
        assert priority >= 1, "A task priority can't be less than 1"

        self.c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', (name, priority))
        self.conn.commit()

    def find_task(self, task_name):
        return self.c.execute('''
        SELECT id, name, priority
        FROM tasks
        WHERE name = ?
        ''', (task_name,)).fetchone()

    def show_tasks(self):
        print('id'.ljust(5), 'name'.ljust(15), 'priority'.ljust(5), sep='|')
        print('-' * 27)
        for id, name, priority in self.c.execute('''SELECT id, name, priority FROM tasks'''):
            print(str(id).ljust(5), name.ljust(15), str(priority).ljust(5), sep='|')


if __name__ == '__main__':
    app = Todo()
    app.add_task()
    app.show_tasks()
