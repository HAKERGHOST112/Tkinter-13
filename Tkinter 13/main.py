from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb


def insert_text():

    try:
        file_name = fd.askopenfilename()
        if not file_name:
            raise FileNotFoundError("Файл не выбран.")
        with open(file_name, 'r') as f:
            s = f.read()
            text.insert(1.0, s)
    except FileNotFoundError:
        mb.showinfo("Информация", "Файл не загружен.")
    except Exception as e:
        mb.showerror("Ошибка", f"Произошла ошибка: {e}")


def extract_text():

    try:
        file_name = fd.asksaveasfilename(
            filetypes=(("TXT files", "*.txt"),
                       ("HTML files", "*.html;*.htm"),
                       ("All files", "*.*")))
        if not file_name:
            raise FileNotFoundError("Имя файла не указано.")
        with open(file_name, 'w') as f:
            s = text.get(1.0, END)
            f.write(s.strip())
    except FileNotFoundError:
        mb.showinfo("Информация", "Файл не сохранён.")
    except Exception as e:
        mb.showerror("Ошибка", f"Произошла ошибка: {e}")


def clear_text():

    answer = mb.askyesno("Подтвердите", "Вы  хотите очистить текст?")
    if answer:
        text.delete(1.0, END)



root = Tk()
root.title("Файловый менеджер")
root.geometry("500x400")

# Текстовое поле
text = Text(root, width=60, height=20)
text.grid(columnspan=3, pady=10)


b1 = Button(root, text="Открыть", command=insert_text)
b1.grid(row=1, column=0, padx=10, sticky=W)

b2 = Button(root, text="Сохранить", command=extract_text)
b2.grid(row=1, column=1, padx=10)

b3 = Button(root, text="Очистить", command=clear_text)
b3.grid(row=1, column=2, padx=10, sticky=E)


root.mainloop()
