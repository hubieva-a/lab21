from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb

def insert_text():
    file_name = fd.askopenfilename()
    if file_name== True:
        f = open(file_name)
        s = f.read()
        text.insert(1.0, s)
        f.close()
    else:
        mb.showerror("Нет файла", "Не выбран файл")

def extract_text():
    file_name = fd.asksaveasfilename(
    filetypes=(("TXT files", "*.txt"),
    ("HTML files", "*.html;*.htm"),
    ("All files", "*.*")))
    if file_name == True:
        f = open(file_name, 'w')
        s = text.get(1.0, END)
        f.write(s)
        f.close()
    else:
        mb.showerror("Нет файла", "Не выбран файл")

def delete_text():
    user_answer = mb.askyesno(
        title="Вопрос пользователю",
        message="Вы уверены, что хотите очистить поле?"
        )
    if user_answer:
        text.delete(1.0, "end")

root = Tk()

main_menu = Menu(root)
root.config(menu=main_menu)

text = Text(width=50, height=25)
text.grid(columnspan=2)

b3 = Button(text="Очистить", command=delete_text)
b3.grid(row=1, column=1, sticky=W)

main_menu.add_command(label='Открыть', command=insert_text)
main_menu.add_command(label='Сохранить', command=extract_text)

root.mainloop()