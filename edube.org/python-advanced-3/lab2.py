# https://edube.org/learn/pcpp1-4-gui-programming/lab-catch-me-if-you-can

import tkinter as tk
from tkinter import messagebox
import random


class CatchMeApp:
    __WINDOW_WIDTH = 500
    __WINDOW_HEIGHT = 500

    def __init__(self):
        self.main_window = tk.Tk()

        self.main_window.minsize(self.__WINDOW_WIDTH, self.__WINDOW_WIDTH)
        self.main_window.maxsize(self.__WINDOW_HEIGHT, self.__WINDOW_HEIGHT)
        self.main_window.resizable = False

        self.catch_me_button = tk.Button(text='Catch me!',
                                         command=self._show_victory_message)
        self.catch_me_button.bind('<Enter>', func=lambda _: self._jump())
        self.catch_me_button.place(x=10, y=10)

    @staticmethod
    def _show_victory_message():
        messagebox.showinfo('Congratulations', 'You are The Winner!')

    def _jump(self):
        button_width = self.catch_me_button.winfo_width()
        button_height = self.catch_me_button.winfo_height()
        self.catch_me_button.place(x=random.randint(0, self.__WINDOW_WIDTH - button_width),
                                   y=random.randint(0, self.__WINDOW_HEIGHT - button_height))

    def run(self):
        self.main_window.mainloop()


if __name__ == '__main__':
    CatchMeApp().run()
