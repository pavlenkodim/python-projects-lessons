from tkinter import *

# функция для нажатия кнопки (может быть любой)
def clicked():
    # label.destroy()
    # Для получения текста из переменной используй get()
    label.configure(text=f"{username.get()} - You logged in my app")

# инициализация окна
window = Tk()
# заголовок окна
window.title("Welcome to the PythonRu application")
# размеры окна
window.geometry("800x600")

# текст
# первый аргумент - родитель (где будет располагаться элемент)
# след аргументы парметры
label = Label(window, text="Welcome to the PythonRu application", font=("Arial", 25))
# раположение по сетке
label.grid(column=0, row=0)

# создаем переменную для того чтобы хранить в ней написанный в Input текст
username = StringVar(window, value = "")
# создаем Input
input_username = Entry(window, textvariable=username)
# указываем его размеры после создания
input_username["width"] = 80
input_username.grid(column=0, row=1)
# создаем кнопку
# command= указываем функцию которая будет выполняться после нажатия на кнопку
btn = Button(window, text="Don't touch me", command=clicked)
btn.grid(column=1, row=1)

# для того чтобы окно не закрывалось
window.mainloop()
