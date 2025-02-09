import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import winsound
import pygame 

class Question:
    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options
        self.answer = answer

def play_sound(correct):
    pygame.mixer.init()
    if correct:
        pygame.mixer.music.load("d.mp3")  # Doğru cevap sesi
    else:
        pygame.mixer.music.load("y.mp3")  # Yanlış cevap sesi
    pygame.mixer.music.play()

def check_answer(selected_option, question):
    global score_correct, score_wrong, question_index
    
    if question.options[selected_option] == question.answer:
        score_correct += 1
        play_sound(True)
        messagebox.showinfo("Sonuç", "Doğru!")
    else:
        score_wrong += 1
        play_sound(False)
        messagebox.showinfo("Sonuç", "Yanlış!")
    
    question_index += 1
    if question_index < len(questions):
        display_question()
    else:
        messagebox.showinfo("Sınav Bitti", f"Toplam Doğru: {score_correct}\nToplam Yanlış: {score_wrong}")
        root.quit()

def display_question():
    global question_index
    question = questions[question_index]
    
    lbl_question.config(text=question.prompt)
    for i, option in enumerate(question.options):
        buttons[i].config(text=option, command=lambda i=i: check_answer(i, question))

questions = [
    Question("Python'da bir listenin eleman sayısını öğrenmek için hangi fonksiyon kullanılır?", ["count()", "size()", "len()", "length()"], "len()"),
    Question("Hangisi Python'da bir döngü türüdür?", ["for", "repeat", "foreach", "loop"], "for"),
    Question("Python'da yorum satırı nasıl yazılır?", ["-- yorum", "// yorum", "# yorum", "/* yorum */"], "# yorum"),
    Question("Hangisi Python'da değişken tanımlamak için doğrudur?", ["var x = 5", "x := 5", "x = 5", "int x = 5"], "x = 5"),
    Question("Python'da bir diziyi tersten sıralamak için hangi fonksiyon kullanılır?", ["reverse()", "sort()", "flip()", "reversed()"], "reverse()")
]

score_correct = 0
score_wrong = 0
question_index = 0

root = tk.Tk()
root.title("Quiz Uygulaması")
root.geometry("400x300")

# Arka plan ekleme
background_image = Image.open("1.png")
background_image = background_image.resize((400, 300), Image.LANCZOS)
background_photo = ImageTk.PhotoImage(background_image)

background_label = tk.Label(root, image=background_photo)
background_label.place(relwidth=1, relheight=1)

lbl_question = tk.Label(root, text="", wraplength=350, font=("Arial", 12), bg="white")
lbl_question.pack(pady=20)

buttons = [tk.Button(root, text="", width=30, font=("Arial", 10)) for _ in range(4)]
for btn in buttons:
    btn.pack(pady=5)

display_question()
root.mainloop()
