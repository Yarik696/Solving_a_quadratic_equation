import tkinter as tk
from tkinter import messagebox

def solve_equation():    #Эта функция, предназначенная для решения квадратных уравнений в форме ax^2 + bx + c = 0, где a, b и c - коэффициенты.
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        if a == 0:
            raise ValueError("Коэффициент 'a' не может быть равен нулю")

        x1 = float(0.00)
        x2 = float(0.00)
        
        if a == 0 and b == 0 and c == 0:
            solution_text.set("Множество решений")
        elif a == 0 and b != 0 and c != 0:
            x1 = -(c / b)
            solution_text.set(f"x = {x1:.2f}")
        elif a == 0 and b == 0 and c != 0:
            solution_text.set("Нет решения")
        elif a == 0 and b != 0 and c == 0:
            x1 = 0
            solution_text.set(f"x = {x1:.2f}")
        elif b == 0 and c == 0 and a != 0:
            x1 = 0
            solution_text.set(f"x = {x1:.2f}")
        elif c == 0 and b != 0 and a != 0:
            x1 = 0
            x2 = -(b / a)
            solution_text.set(f"x1 = {min(x1, x2):.2f}, x2 = {max(x1, x2):.2f}")
        elif b == 0 and a != 0 and c != 0:
            if (-(c / a)) < 0:
                solution_text.set("Нет решения")
            else:
                x1 = (-c / a) ** 0.5
                x2 = -((-c / a) ** 0.5)
                solution_text.set(f"x1 = {min(x1, x2):.2f}, x2 = {max(x1, x2):.2f}")
        elif a != 0 and b != 0 and c != 0:
            disc = (b ** 2) - (4 * a * c)  # дискрімінант
            if disc < 0:
                solution_text.set("Нет решения")
            elif disc == 0:
                x1 = (-b / (2 * a))
                solution_text.set(f"x = {x1:.2f}")
            elif disc > 0:
                x1 = (-b - (disc ** 0.5)) / (2 * a)
                x2 = (-b + (disc ** 0.5)) / (2 * a)
                solution_text.set(f"x1 = {min(x1, x2):.2f}, x2 = {max(x1, x2):.2f}")
            disc_label.config(text=f"D= {disc:.0f}", fg="black")
    except ValueError as e:
        messagebox.showerror("Ошибка", str(e))

def validate_entry(entry):    #Эта функция проверяет содержимое текстового поля entry. Если поле пустое или содержит нечисловые символы (кроме точки для десятичного числа), текстовый цвет устанавливается красным; иначе цвет остается черным.
    if entry.get() == '' or not entry.get().replace('.', '', 1).isdigit():
        entry.config(fg="black")
    else:
        entry.config(fg="green")
        
def validate_entry_content(entry):    #Эта функция проверяет, является ли содержимое текстового поля entry пустым. Если да, то рамка вокруг поля подсвечивается красным; в противном случае рамка остается стандартного цвета.
    if not entry.get():
        entry.config(highlightbackground="red")
    else:
        entry.config(highlightbackground="SystemButtonFace")

def change_color(event):    #Эта функция изменяет цвет текста в текстовом поле в соответствии с введенным символом. Если введенный символ является цифрой или точкой, цвет текста остается черным; в противном случае цвет текста меняется на красный.
    if event.char.isdigit():
        event.widget.config(fg="green")
    else:
        event.widget.config(fg="black")

# Создание главного окна
root = tk.Tk()
root.title("Рішення квадратного рівняння")

# Создание надписи «Решение квадратного уравнения» на синем фоне
title_label = tk.Label(root, text="Решение квадратного уравнения", fg="green", bg="light blue", font=("Arial", 13, "bold"))
title_label.pack(pady=10)

# Создание фрейма для ввода коэффициентов a, b и c
frame_coefficients = tk.Frame(root)
frame_coefficients.pack(pady=10)

# Создание элементов для ввода коэффициентов a, b и c
entry_a = tk.Entry(frame_coefficients, width=5, bg="light blue")
entry_a.grid(row=0, column=0, padx=5)
entry_a.bind('<FocusOut>', lambda e: validate_entry(entry_a))
entry_a.bind('<KeyRelease>', change_color)
entry_a.bind('<KeyRelease>', lambda e: validate_entry_content(entry_a)) 
tk.Label(frame_coefficients, text="x**2+").grid(row=0, column=1, padx=5)
entry_b = tk.Entry(frame_coefficients, width=5, bg="light blue")
entry_b.grid(row=0, column=2, padx=5)
entry_b.bind('<FocusOut>', lambda e: validate_entry(entry_b))
entry_b.bind('<KeyRelease>', change_color)
entry_b.bind('<KeyRelease>', lambda e: validate_entry_content(entry_b)) 
tk.Label(frame_coefficients, text="x+").grid(row=0, column=3, padx=5)
entry_c = tk.Entry(frame_coefficients, width=5, bg="light blue")
entry_c.grid(row=0, column=4, padx=5)
entry_c.bind('<FocusOut>', lambda e: validate_entry(entry_c))
entry_c.bind('<KeyRelease>', change_color)
entry_c.bind('<KeyRelease>', lambda e: validate_entry_content(entry_c)) 

# Создание кнопки для получения решения
button_solve = tk.Button(frame_coefficients, text="Решить", command=solve_equation, bg="green", fg="black", padx=10, pady=5)
button_solve.grid(row=0, column=5, padx=(0, 10), ipadx=10)  # Відступ від правого краю

# Создание фрейма для вывода результата
result_frame = tk.Frame(root, bg="yellow")
result_frame.pack(pady=(0, 10), padx=(50, 50), fill=tk.X)  # Зміна параметрів для розташування внизу з відступами від лівого і правого країв

# Этикет для вывода дискриминанта
disc_label = tk.Label(result_frame, text="", fg="black", font=("Arial", 12), bg="yellow")
disc_label.pack(pady=5)

# Создание этикета для вывода результата
solution_text = tk.StringVar()
result_label = tk.Label(result_frame, textvariable=solution_text, fg="black", font=("Arial", 12), bg="yellow")
result_label.pack()

# Запуск главного цикла программы
root.mainloop()
