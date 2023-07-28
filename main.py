#Imports
from tkinter import *
from tkinter import ttk
import re
from tkinter  import messagebox
import random
import os

#Window
root = Tk()
root.title("Виселица")
root.geometry()
root.option_add("*tearOff", FALSE)
root.resizable(width=False, height=False)

#Icon
icon = PhotoImage(file = "icon.png")
root.iconphoto(False, icon)

#Impotant vars
words = open('words.txt', 'r', encoding='utf-8').read()
words = words.split('\n')
stage = 0
word = random.choice(words)
unknown_word = ['_' for i in range(len(word))]
use_ords = []

#DEBUG Flag
DEBUG=False

#Function
def main():
    global unknown_word, use_ords
    ords=entry_ord.get()
    if not ords: return
    entry_ord.delete(0, END)
    use_ords.append(ords)
    ords_label['text']='Использованные буквы:\n' + ' '.join(use_ords)
    list_word=list(word)
    if DEBUG: print(unknown_word, list_word, ords)
    
    for i in range(len(list_word)):
        if ords == list_word[i]:
            unknown_word[i] = ords
            word_label["text"]=''.join(unknown_word)
            if unknown_word == list_word:
                messagebox.showinfo("Ура!", "Ты выйграл!")
                reset()
                
    if ords not in list_word:
        global stage 
        if stage > 6:
            stage = 0
            messagebox.showinfo("Проиграл!", f"Game over! Слово: {word}!")
            reset()
        else:
            stage+=1
        
        gallows_label["image"]=eval('gallows_s'+str(stage))

def reset():
    global word, unknown_word, stage, use_ords
    word=random.choice(words)
    stage=0
    unknown_word=['_' for i in range(len(word))]
    word_label["text"]=''.join(unknown_word)
    
    entry_ord.delete(0, END)
    
    gallows_label["image"]=eval('gallows_s'+str(stage))
    use_ords=[]
    ords_label['text']='Использованные буквы:\n' + ' '.join(use_ords)
    len_label['text']=('Длина слова: '+ str(len(word)))
    
def open_word_file(): os.system('words.txt')
    
def exit(): root.destroy()
    
def about(): messagebox.showinfo('Игра "Виселица"', "Автор: Nikita Fedosov\nВерсия: 1.0a\nGitHub: https://github.com/bolgaro4ka")

#Top menu
main_menu = Menu()
main_menu.add_cascade(label="Перезапустить", command=reset)
main_menu.add_cascade(label="Открыть файл со словами", command=open_word_file)
main_menu.add_cascade(label="О программе", command=about)
main_menu.add_cascade(label="Выход", command=exit)
    
#Images
gallows_s0 = PhotoImage(file="./img/0.png")
gallows_s1 = PhotoImage(file="./img/1.png")
gallows_s2 = PhotoImage(file="./img/2.png")
gallows_s3 = PhotoImage(file="./img/3.png")
gallows_s4 = PhotoImage(file="./img/4.png")
gallows_s5 = PhotoImage(file="./img/5.png")
gallows_s6 = PhotoImage(file="./img/6.png")
gallows_s7 = PhotoImage(file="./img/7.png")


#Interface
mystery_user_word=StringVar(value="")

gallows_label=ttk.Label(image=gallows_s0)
gallows_label.pack(side='right', padx=3, pady=3)

word_label=ttk.Label(text=''.join(unknown_word), font=("Colibri", 28), cursor='question_arrow')
word_label.pack(side='left', anchor=S, padx=3, pady=3)

len_label=ttk.Label(text='Длина слова: '+ str(len(word)))
len_label.pack(side='left', anchor=S, padx=3, pady=3)

ords_label=ttk.Label(text='Использованные буквы:\n' + ' '.join(use_ords), justify=CENTER)
ords_label.pack(side='left', anchor=NW, ipadx=30, ipady=30)

entry_ord = ttk.Entry(width=1, font=("Colibri", 28))
entry_ord.pack(side='left', anchor=S, padx=3, pady=3)

button = ttk.Button(text='Проверить', command=main)
button.pack(side='left', ipadx=12, ipady=12, anchor=S, padx=3, pady=3)

#Init menu
root.config(menu=main_menu)

#MainLoop
root.mainloop()