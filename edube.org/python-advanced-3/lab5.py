# https://edube.org/learn/pcpp1-4-gui-programming/lab-tic-tac-toe

import tkinter as tk
from tkinter import font, messagebox
import random


# TODO: handle draw/tie
class TikTakToe:
    FONT_SIZE = 60

    HORIZONTAL_SIZE = 3
    VERTICAL_SIZE = 3

    BUTTON_WIDTH = 5
    BUTTON_HEIGHT = 2

    COMPUTER_MARK = 'x'
    USER_MARK = 'o'

    def __init__(self):
        self._main_window = tk.Tk()
        self._buttons = []

        for i in range(self.VERTICAL_SIZE):
            current_line_buttons = []
            for j in range(self.HORIZONTAL_SIZE):
                btn = tk.Button(self._main_window, width=self.BUTTON_WIDTH, height=self.BUTTON_HEIGHT,
                                font=font.Font(family="Helvetica", size=self.FONT_SIZE, weight="bold"))
                btn.bind('<Button-1>', self._button_click_handler)
                btn.grid(row=i, column=j)
                current_line_buttons.append(btn)
            self._buttons.append(current_line_buttons)

    def _button_click_handler(self, event):
        self._mark(event.widget, self.USER_MARK)

        clickable_buttons = []
        for i in range(self.VERTICAL_SIZE):
            for j in range(self.HORIZONTAL_SIZE):
                btn = self._buttons[i][j]
                if btn.cget('state') != tk.DISABLED:
                    clickable_buttons.append(btn)

        if clickable_buttons:
            self._mark(random.choice(clickable_buttons), self.COMPUTER_MARK)

    def _mark(self, button, character):
        button.config(text=character, state=tk.DISABLED)
        if character == self.COMPUTER_MARK:
            button.config(disabledforeground='red')
        else:
            button.config(disabledforeground='green')
        button.unbind('<Button-1>')

        self._check_winner(character)

    def _check_winner(self, character):
        bs = self._buttons
        have_main_diagonal = all([bs[i][j].cget('text') == character for i, j in
                                  zip(range(self.VERTICAL_SIZE), range(self.HORIZONTAL_SIZE))])

        have_second_diagonal = all([bs[i][j].cget('text') == character for i, j in
                                    zip(range(self.VERTICAL_SIZE), range(self.HORIZONTAL_SIZE - 1, -1, -1))])

        have_vertical = any(
            [all([bs[i][j].cget('text') == character for i in range(self.VERTICAL_SIZE)]) for j in
             range(self.HORIZONTAL_SIZE)]
        )

        have_horizontal = any(
            [all([bs[i][j].cget('text') == character for j in range(self.HORIZONTAL_SIZE)]) for i in
             range(self.VERTICAL_SIZE)]
        )

        winner = have_main_diagonal or have_second_diagonal or have_vertical or have_horizontal

        if winner:
            for i in range(self.VERTICAL_SIZE):
                for j in range(self.HORIZONTAL_SIZE):
                    btn = self._buttons[i][j]
                    btn.unbind('<Button-1>')
                    btn.config(state=tk.DISABLED)

            if character == self.COMPUTER_MARK:
                messagebox.showinfo('You lost', 'Computer won! :(')
            else:
                messagebox.showinfo('You won', 'You are The Winner!!!')

    def run(self):
        middle_button = self._buttons[1][1]
        self._mark(middle_button, self.COMPUTER_MARK)
        self._main_window.mainloop()


if __name__ == '__main__':
    TikTakToe().run()
