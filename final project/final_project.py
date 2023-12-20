import tkinter as tk
import ttkbootstrap as ttk
from PIL import Image, ImageTk

window = ttk.Window()
window.title("Final Project")
window.geometry("500x500")
window.resizable(True, True)

# icon setting
img = Image.open("icon.ico")
p1 = ImageTk.PhotoImage(img)
window.iconphoto(False, p1)


# Calculator function
def calculator():
    temp_var = tk.StringVar()
    temp_var.set("")

    # update while inputing
    def update_temp(digit):
        if digit == "=":
            try:
                expression_result = eval(input_text.get("1.0", tk.END))
                input_text.delete("1.0", tk.END)  # Clear the current text
                input_text.insert(tk.END, str(expression_result))

            except Exception as e:
                input_text.delete("1.0", tk.END)  # Clear the current text
                input_text.insert(tk.END, "Error")

        elif digit == "clear":  # Clear the current text
            input_text.delete("1.0", tk.END)

        else:
            current_value = temp_var.get()
            temp_var.set(current_value + str(digit))
            input_text.insert(tk.END, str(digit))

    # calculate_window
    calculator_window = tk.Toplevel(window)
    calculator_window.geometry("500x510")

    # input_text
    input_text = ttk.Text(calculator_window, width=30, height=2)
    input_text.grid(row=0, column=1, columnspan=4, padx=10, pady=10)

    # buttons
    # 7
    button_num_7 = ttk.Button(
        calculator_window,
        text="7",
        style="DARK.Outline.TButton",
        command=lambda: update_temp(7),
    )
    button_num_7.grid(row=1, column=1, ipady=30, ipadx=30)

    # 8
    button_num_8 = ttk.Button(
        calculator_window,
        text="8",
        style="DARK.Outline.TButton",
        command=lambda: update_temp(8),
    )
    button_num_8.grid(row=1, column=2, ipady=30, ipadx=30)

    # 9
    button_num_9 = ttk.Button(
        calculator_window,
        text="9",
        style="DARK.Outline.TButton",
        command=lambda: update_temp(9),
    )
    button_num_9.grid(row=1, column=3, ipady=30, ipadx=30)

    # 4
    button_num_4 = ttk.Button(
        calculator_window,
        text="4",
        style="DARK.Outline.TButton",
        command=lambda: update_temp(4),
    )
    button_num_4.grid(row=2, column=1, ipady=30, ipadx=30)

    # 5
    button_num_5 = ttk.Button(
        calculator_window,
        text="5",
        style="DARK.Outline.TButton",
        command=lambda: update_temp(5),
    )
    button_num_5.grid(row=2, column=2, ipady=30, ipadx=30)

    # 6
    button_num_6 = ttk.Button(
        calculator_window,
        text="6",
        style="DARK.Outline.TButton",
        command=lambda: update_temp(6),
    )
    button_num_6.grid(row=2, column=3, ipady=30, ipadx=30)

    # 1
    button_num_1 = ttk.Button(
        calculator_window,
        text="1",
        style="DARK.Outline.TButton",
        command=lambda: update_temp(1),
    )
    button_num_1.grid(row=3, column=1, ipady=30, ipadx=30)

    # 2
    button_num_2 = ttk.Button(
        calculator_window,
        text="2",
        style="DARK.Outline.TButton",
        command=lambda: update_temp(2),
    )
    button_num_2.grid(row=3, column=2, ipady=30, ipadx=30)

    # 3
    button_num_3 = ttk.Button(
        calculator_window,
        text="3",
        style="DARK.Outline.TButton",
        command=lambda: update_temp(3),
    )
    button_num_3.grid(row=3, column=3, ipady=30, ipadx=30)

    # .
    button_dot = ttk.Button(
        calculator_window,
        text=".",
        style="DARK.Outline.TButton",
        command=lambda: update_temp("."),
    )
    button_dot.grid(row=4, column=1, ipady=30, ipadx=30)

    # 0
    button_num_0 = ttk.Button(
        calculator_window,
        text="0",
        style="DARK.Outline.TButton",
        command=lambda: update_temp(0),
    )
    button_num_0.grid(row=4, column=2, ipady=30, ipadx=30)

    # =
    button_equal = ttk.Button(
        calculator_window,
        text="=",
        style="DARK.Outline.TButton",
        command=lambda: update_temp("="),
    )
    button_equal.grid(row=4, column=3, ipady=30, ipadx=30)

    # +
    button_plus = ttk.Button(
        calculator_window,
        text="+",
        style="DARK.Outline.TButton",
        command=lambda: update_temp("+"),
    )
    button_plus.grid(row=1, column=4, ipady=30, ipadx=30)

    # -
    button_minus = ttk.Button(
        calculator_window,
        text="-",
        style="DARK.Outline.TButton",
        command=lambda: update_temp("-"),
    )
    button_minus.grid(row=2, column=4, ipady=30, ipadx=30)

    # *
    button_multiply = ttk.Button(
        calculator_window,
        text="*",
        style="DARK.Outline.TButton",
        command=lambda: update_temp("*"),
    )
    button_multiply.grid(row=3, column=4, ipady=30, ipadx=30)

    # /
    button_divide = ttk.Button(
        calculator_window,
        text="/",
        style="DARK.Outline.TButton",
        command=lambda: update_temp("/"),
    )
    button_divide.grid(row=4, column=4, ipady=30, ipadx=30)

    # clear
    button_clear = ttk.Button(
        calculator_window,
        text="clear",
        style="DARK.Outline.TButton",
        command=lambda: update_temp("clear"),
    )
    button_clear.grid(row=4, column=5, ipady=30, ipadx=30)


# Main function

# button_calculator
button_calculator = ttk.Button(
    window, text="calculator", style="INFO.Outline.TButton", command=calculator
)
button_calculator.pack(ipady=20, ipadx=20)


# Remain function
window.mainloop()
