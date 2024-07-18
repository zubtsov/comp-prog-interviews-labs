# https://edube.org/learn/pcpp1-4-gui-programming/lab-a-very-simple-calculator

import tkinter as tk
from tkinter import messagebox


class UnknownOperatorException(ValueError):
    def __init__(self, operator_id, *args):
        super().__init__(*args)
        self.operator_id = operator_id

    def __str__(self):
        return f'Unknown operator with ID {self.operator_id}'


class OperandIsEmptyError(ValueError):
    def __init__(self, operand_entry, *args):
        super().__init__(*args)
        self.operand_entry = operand_entry


class SimpleCalculatorApp:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title('Calculator')

        self.left_operand_var = tk.StringVar()
        self.operator_var = tk.IntVar(value=-1)
        self.right_operand_var = tk.StringVar()

        top_frame = tk.Frame(self.main_window)

        self.left_operand_entry = tk.Entry(top_frame, textvariable=self.left_operand_var)
        self.left_operand_entry.grid(row=0, column=0)
        self.left_operand_entry.focus_set()

        self.operators_frame = tk.Frame(top_frame, takefocus=True)

        plus_radio = tk.Radiobutton(self.operators_frame, variable=self.operator_var, value=0)
        plus_radio.config(text='+')
        plus_radio.pack()

        minus_radio = tk.Radiobutton(self.operators_frame, variable=self.operator_var, value=1)
        minus_radio.config(text='-')
        minus_radio.pack()

        mult_radio = tk.Radiobutton(self.operators_frame, variable=self.operator_var, value=2)
        mult_radio.config(text='*')
        mult_radio.pack()

        div_radio = tk.Radiobutton(self.operators_frame, variable=self.operator_var, value=3)
        div_radio.config(text='/')
        div_radio.pack()

        self.operators_frame.grid(row=0, column=1)

        self.right_operand_entry = tk.Entry(top_frame, textvariable=self.right_operand_var)
        self.right_operand_entry.grid(row=0, column=2)

        bottom_frame = tk.Frame(self.main_window)
        evaluate_button = tk.Button(bottom_frame,
                                    command=self._display_operation_result)
        evaluate_button.config(text='Evaluate')
        evaluate_button.pack()

        top_frame.pack()
        bottom_frame.pack()

    def run(self):
        self.main_window.mainloop()

    def _display_operation_result(self):
        try:
            result = str(self._perform_operation())
            messagebox.showinfo('Result', result)
        except UnknownOperatorException as uoe:
            messagebox.showerror('Error', uoe)
            self.operators_frame.focus_set()
        except ZeroDivisionError as zde:
            messagebox.showerror('Error', str(zde))
            self.right_operand_entry.focus_set()
        except OperandIsEmptyError as oe:
            oe.operand_entry.focus_set()
            messagebox.showerror('Error', str(oe))
        except ValueError as ve:
            messagebox.showerror('Error', str(ve))

    def _perform_operation(self):
        left_operand_text = self.left_operand_var.get()
        if not left_operand_text.strip():
            raise OperandIsEmptyError(self.left_operand_entry, 'The left operand is an empty string')
        left_operand = int(left_operand_text)

        right_operand_text = self.right_operand_var.get()
        if not right_operand_text.strip():
            raise OperandIsEmptyError(self.right_operand_entry, 'The right operand is an empty string')
        right_operand = int(right_operand_text)

        operator_id = self.operator_var.get()

        if operator_id == 0:
            return left_operand + right_operand
        elif operator_id == 1:
            return left_operand - right_operand
        elif operator_id == 2:
            return left_operand * right_operand
        elif operator_id == 3:
            return left_operand / right_operand
        else:
            raise UnknownOperatorException(operator_id)


if __name__ == '__main__':
    SimpleCalculatorApp().run()
