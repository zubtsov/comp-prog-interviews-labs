import tkinter as tk
import random
import time
from tkinter import font


class ClickerGame:
    NUM_BUTTONS_HORIZONTAL = 5
    NUM_BUTTONS_VERTICAL = 5
    MIN_NUMBER = 1
    MAX_NUMBER = 999
    BUTTON_WIDTH = 10
    BUTTON_HEIGHT = 3
    TIMER_UPDATE_INTERVAL_MS = 100

    def __init__(self):
        self._random_numbers = set(random.sample(range(self.MIN_NUMBER, self.MAX_NUMBER + 1),
                                                 self.NUM_BUTTONS_HORIZONTAL * self.NUM_BUTTONS_VERTICAL))
        self._main_window = tk.Tk()
        self._main_window.title('Clicker')

        self._buttons_frame = tk.Frame(self._main_window)
        self._buttons = []

        random_numbers_iter = iter(self._random_numbers)
        for row_number in range(self.NUM_BUTTONS_VERTICAL):
            for column_number in range(self.NUM_BUTTONS_HORIZONTAL):
                button_font = font.Font(family="Helvetica", size=15, weight="bold")
                button = tk.Button(self._buttons_frame, text=next(random_numbers_iter),
                                   width=self.BUTTON_WIDTH,
                                   height=self.BUTTON_HEIGHT,
                                   font=button_font)
                button.grid(row=row_number, column=column_number)
                button.bind('<Button-1>', self._handle_button_click)
                self._buttons.append(button)

        self._buttons_frame.pack()

        self._timer_var = tk.DoubleVar(value=0.0)
        timer_font = font.Font(family="Helvetica", size=12, weight="bold")
        timer_label = tk.Label(self._main_window, textvariable=self._timer_var,
                               font=timer_font)
        timer_label.pack()

    def _update_timer(self):
        current_time = time.monotonic_ns()

        self._timer_var.set((current_time - self._start_timestamp) / (10 ** 9))
        self.__last_after_id = self._main_window.after(self.TIMER_UPDATE_INTERVAL_MS, self._update_timer)

    def _handle_button_click(self, event):
        if not hasattr(self, '_start_timestamp'):
            self._start_timestamp = time.monotonic_ns()
            self.__last_after_id = self._main_window.after(self.TIMER_UPDATE_INTERVAL_MS, self._update_timer)

        button_number = int(event.widget.cget('text'))
        if button_number == min(self._random_numbers):
            self._random_numbers.remove(button_number)
            event.widget.config(state=tk.DISABLED)

        if not self._random_numbers:
            self._main_window.after_cancel(self.__last_after_id)
            for button in self._buttons:
                button.unbind('<Button-1>')

    def run(self):
        self._main_window.mainloop()


if __name__ == '__main__':
    ClickerGame().run()
