#Голомоза Інна Андріївна
from tkinter import *
from tkinter import ttk

def calculate_mark():
    mark = 0

    # Перевірка відповідей на питання
    if v1.get() == 1 and v2.get() == 1 and v3.get() == 0 and v4.get() == 0:
        mark += 2
    elif v1.get() == 1 and v2.get() == 0 and v3.get() == 0 and v4.get() == 0:
        mark += 1
    elif v1.get() == 0 and v2.get() == 1 and v3.get() == 0 and v4.get() == 0:
        mark += 1

    if v5.get() == 1:
        mark += 2

    if v6.get().lower() == "інтернет":
        mark += 2

    if v7.get() == "Так":
        mark += 2

    if v8.get() == "Пікселів":
        mark += 2

    if v9.get():
        mark += 2

    if mark > 6:
        lbl_result["fg"] = "green"
    else:
        lbl_result["fg"] = "red"
    v10.set("Ваша оцінка: " + str(mark))


# Створення головного вікна
tk = Tk()
tk.title("Тест з інформатики")
tk.configure(bg="lightblue")
font_title = ("Arial", 14, "bold")
font_question = ("Arial", 12, "bold")

# Перше питання
lbl1 = Label(tk, text="Питання №1", font=font_title)
lbl2 = Label(tk, text="Які існують пристрої введення?", font=font_question)
v1 = IntVar()
v2 = IntVar()
v3 = IntVar()
v4 = IntVar()
chb1 = Checkbutton(tk, text="Клавіатура", variable=v1, onvalue=1, offvalue=0)
chb2 = Checkbutton(tk, text="Миша", variable=v2, onvalue=1, offvalue=0)
chb3 = Checkbutton(tk, text="Монітор", variable=v3, onvalue=1, offvalue=0)
chb4 = Checkbutton(tk, text="Принтер", variable=v4, onvalue=1, offvalue=0)

# Друге питання
lbl3 = Label(tk, text="Питання №2", font=font_title)
lbl4 = Label(tk, text="Скільки Мб у Гб?", font=font_question)
v5 = IntVar()
rbt1 = Radiobutton(tk, text="1024", variable=v5, value=1)
rbt2 = Radiobutton(tk, text="1000", variable=v5, value=2)
rbt3 = Radiobutton(tk, text="8", variable=v5, value=3)
rbt4 = Radiobutton(tk, text="1000000", variable=v5, value=4)

# Третє питання
lbl5 = Label(tk, text="Питання №3", font=font_title)
lbl6 = Label(tk, text="Як називається велика мережа, яка з'єднує мільйони \n комп'ютерів та пристроїв по всьому світу?", font=font_question)
v6 = StringVar()
entry1 = Entry(tk, textvariable=v6)

# Четверте питання
lbl7 = Label(tk, text="Питання №4", font=font_title)
lbl8 = Label(tk, text="Python - це мова програмування?", font=font_question)
v7 = StringVar()
cmb1 = ttk.Combobox(tk, textvariable=v7, values=["Так", "Ні"])
cmb1.set("")

# П'яте питання
lbl9 = Label(tk, text="Питання №5", font=font_title)
lbl10 = Label(tk, text="Якість зображення на екрані визначається кількістю ...", font=font_question)
v8 = StringVar()
cmb2 = ttk.Combobox(tk, textvariable=v8, values=["Пікселів", "Бітів", "Кілобайтів", " Герців"])
cmb2.set("")

# Шосте питання
lbl11 = Label(tk, text="Питання №6", font=font_title)
lbl12 = Label(tk, text="Як ви оцінюєте свій рівень знань в області програмування?", font=font_question)
v9 = IntVar()
scl = Scale(tk, orient=HORIZONTAL, variable=v9, from_=1, to=5, tickinterval=1, resolution=1)

# Кнопка для обчислення оцінки
btn = Button(tk, text="Відповісти", command=calculate_mark, font=font_question)
v10 = StringVar()
lbl_result = Label(tk, text='', textvariable=v10, font=font_title)

# Розміщення віджетів на вікні
lbl1.pack()
lbl2.pack()
chb1.pack()
chb2.pack()
chb3.pack()
chb4.pack()

lbl3.pack()
lbl4.pack()
rbt1.pack()
rbt2.pack()
rbt3.pack()
rbt4.pack()

lbl5.pack()
lbl6.pack()
entry1.pack()

lbl7.pack()
lbl8.pack()
cmb1.pack()

lbl9.pack()
lbl10.pack()
cmb2.pack()

lbl11.pack()
lbl12.pack()
scl.pack()

btn.pack()
lbl_result.pack()

tk.mainloop()
