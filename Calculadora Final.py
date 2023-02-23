from tkinter import *

root = Tk()
root.title("Calculadora")

# Interfaz
display = Entry(root)
display.grid(row=1, columnspan=6, sticky=W+E)
root.geometry('410x273')
root.resizable(False, False)

# Numeros a mostrar
i = 0


def get_numbers(n):
    global i
    display.insert(i, n)
    i += 1

def get_operation(operator):
    global i
    operator_length = len(operator)
    display.insert(i, operator)
    i+=operator_length

def calculate():
    display_state = display.get()
    try:
        math_expression =  compile(display_state, 'app.py', 'eval')
        result = eval(math_expression)
        clear_display()
        display.insert(0,result)
    except:
        clear_display()


def clear_display():
    display.delete(0, END)


def undo():
    display_state = display.get()
    if len(display_state):
        display_new_state = display_state[:-1]
        clear_display()
        display.insert(0, display_new_state)



# Botones de Numeros
Button(root, text="7", height=3, width=10, anchor="center", command=lambda: get_numbers(7)).grid(row=2, column=0)
Button(root, text="8", height=3, width=10, anchor="center", command=lambda: get_numbers(8)).grid(row=2, column=1)
Button(root, text="9", height=3, width=10, anchor="center", command=lambda: get_numbers(9)).grid(row=2, column=2)

Button(root, text="4", height=3, width=10, anchor="center", command=lambda: get_numbers(4)).grid(row=3, column=0)
Button(root, text="5", height=3, width=10, anchor="center", command=lambda: get_numbers(5)).grid(row=3, column=1)
Button(root, text="6", height=3, width=10, anchor="center", command=lambda: get_numbers(6)).grid(row=3, column=2)

Button(root, text="1", height=3, width=10, anchor="center", command=lambda: get_numbers(1)).grid(row=4, column=0)
Button(root, text="2", height=3, width=10, anchor="center", command=lambda: get_numbers(2)).grid(row=4, column=1)
Button(root, text="3", height=3, width=10, anchor="center", command=lambda: get_numbers(3)).grid(row=4, column=2)

# Botones de Operaciones
Button(root, text="AC", height=5, width=10, anchor="center", command=lambda: clear_display()).grid(row=5, column=0)
Button(root, text="0", height=5, width=10, anchor="center", command=lambda: get_numbers(0)).grid(row=5, column=1)
Button(root, text="%", height=5, width=10, anchor="center", command=lambda: get_operation("%")).grid(row=5, column=2)

Button(root, text="+", height=3, width=10, anchor="center", command=lambda: get_operation("+")).grid(row=2, column=3)
Button(root, text="-", height=3, width=10, anchor="center", command=lambda: get_operation("-")).grid(row=3, column=3, sticky=W+E)
Button(root, text="*", height=3, width=10, anchor="center", command=lambda: get_operation("*")).grid(row=4, column=3, sticky=W+E)
Button(root, text="/", height=5, width=10, anchor="center", command=lambda: get_operation("/")).grid(row=5, column=3, sticky=W+E)
Button(root, text="⟵", height=3, width=10, anchor="center", command=lambda: undo()).grid(row=2, column=4, sticky=W+E, columnspan=2)
Button(root, text="exp", height=3, width=5, anchor="center", command=lambda: get_operation("**")).grid(row=3, column=4)
Button(root, text="^2", height=3, width=5, anchor="center", command=lambda: get_operation("**2")).grid(row=3, column=5)
Button(root, text="(", height=3, width=5, anchor="center", command=lambda: get_operation("(")).grid(row=4, column=4,sticky=W+E)
Button(root, text=")", height=3, width=5, anchor="center", command=lambda:get_operation(")")).grid(row=4, column=5, sticky=W+E)
Button(root, text="=", height=5, width=10, anchor="center", command=lambda: calculate()).grid(row=5, column=4, sticky=W+E, columnspan=2)

root.mainloop()