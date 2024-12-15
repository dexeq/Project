import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        # Получаем значения из полей ввода
        labor_cost = float(labor_entry.get())
        material_cost = float(material_entry.get())
        additional_cost = float(additional_entry.get())

        # Подсчитываем общую стоимость
        total_cost = labor_cost + material_cost + additional_cost
        
        # Выводим результат
        result_label.config(text=f"Общая стоимость: {total_cost} руб.")
        
    except ValueError:
        messagebox.showerror("Ошибка ввода", "Пожалуйста, введите числовые значения.")

# Создаём главное окно
root = tk.Tk()
root.title("Калькулятор ремонта")

# Создаём элементы интерфейса
tk.Label(root, text="Стоимость труда (руб.):").pack()
labor_entry = tk.Entry(root)
labor_entry.pack()

tk.Label(root, text="Стоимость материалов (руб.):").pack()
material_entry = tk.Entry(root)
material_entry.pack()

tk.Label(root, text="Дополнительные расходы (руб.):").pack()
additional_entry = tk.Entry(root)
additional_entry.pack()

calculate_button = tk.Button(root, text="Рассчитать", command=calculate)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Запускаем главный цикл приложения
root.mainloop()
