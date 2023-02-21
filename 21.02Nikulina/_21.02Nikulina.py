import tkinter as tk
from tkinter import messagebox

def solve_quadratic(a, b, c):
    """Функция для нахождения решений квадратного уравнения."""
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None, None
    elif discriminant == 0:      
        if a==0:
            messagebox.showerror("Ошибка", "Исправте 0.")
        else:
            return -b / (2*a), None
    else:
        if a==0:
            messagebox.showerror("Ошибка", "Исправте 0.")
        else:
            root1 = (-b + discriminant**0.5) / (2*a)
            root2 = (-b - discriminant**0.5) / (2*a)
            return root1, root2

def solve():
    """Функция, которая вызывается при нажатии кнопки 'Решить'."""
    a = a_entry.get()
    b = b_entry.get()
    c = c_entry.get()
    
    if not a or not b or not c:
        # Если какое-то поле не заполнено, изменяем цвет фона на красный.
        root.configure(background='red')
        messagebox.showerror("Ошибка", "Пожалуйста, заполните все поля.")
    else:
        # Если все поля заполнены, изменяем цвет фона на белый.
        root.configure(background='white')
        a = float(a)
        b = float(b)
        c = float(c)
        root1, root2 = solve_quadratic(a, b, c)
        if root1 is None and root2 is None:
            messagebox.showwarning("Предупреждение", "Уравнение не имеет решений.")
        else:
            solution_text = "Уравнение имеет следующие решения:\n"
            if root1 is not None:
                solution_text += f"Корень 1: {root1}\n"
            if root2 is not None:
                solution_text += f"Корень 2: {root2}\n"
            solution_label.configure(text=solution_text)

# Создаем окно.
root = tk.Tk()
root.title("Решение квадратного уравнения")

# Создаем виджеты.
a_label = tk.Label(root, text="a:")
a_entry = tk.Entry(root, bg="#b7ebe8") 
b_label = tk.Label(root, text="b:")
b_entry = tk.Entry(root, bg="#b7ebe8")
c_label = tk.Label(root, text="c:")
c_entry = tk.Entry(root,bg="#b7ebe8")
solve_button = tk.Button(root, text="Решить", command=solve,bg="#42ea2e")
solution_label = tk.Label(root, text="", bg="#f1f041")

# Размещаем виджеты в окне.
a_label.grid(row=0, column=0)
a_entry.grid(row=0, column=1)
b_label.grid(row=1, column=0)
b_entry.grid(row=1, column=1)
c_label.grid(row=2, column=0)
c_entry.grid(row=2, column=1)
solve_button.grid(row=10, column=0, columnspan=2, pady=10)
solution_label.grid(row=4, column=0, columnspan=2)

# Запускаем главный цикл обработки событий.     
root.mainloop()

