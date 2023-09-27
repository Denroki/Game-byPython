from tkinter import *
import random

choices = {"paper": 1, "scissors": 2, "rock": 3}

def press_button(choice):
    global equation_text, uscore, pcscore

    computer = random.choice(list(choices.keys()))
    player = choice

    if player == computer:
        equation_text = f'Computer: {computer} You: {player} Result: tie'
    elif player == "rock":
        if computer == "paper":
            equation_text = f'Computer: {computer} You: {player} Result: You lose!'
            pcscore += 1
        elif computer == "scissors":
            equation_text = f'Computer: {computer} You: {player} Result: You win!'
            uscore += 1
    elif player == "paper":
        if computer == "scissors":
            equation_text = f'Computer: {computer} You: {player} Result: You lose!'
            pcscore += 1
        elif computer == "rock":
            equation_text = f'Computer: {computer} You: {player} Result: You win!'
            uscore += 1
    elif player == "scissors":
        if computer == "rock":
            equation_text = f'Computer: {computer} You: {player} Result: You lose!'
            pcscore += 1
        elif computer == "paper":
            equation_text = f'Computer: {computer} You: {player} Result: You win!'
            uscore += 1

    equation_label.set(equation_text)
    update_score()

def button_click(choice):
    press_button(choice)

def clear():
    global equation_text, uscore, pcscore
    equation_label.set("")
    equation_text = ""
    uscore = 0
    pcscore = 0
    update_score()

def update_score():
    score_text = f"Computer: {pcscore} - Your Score: {uscore}"
    fscore.config(state=NORMAL)
    fscore.delete(1.0, END)
    fscore.insert(END, score_text)
    fscore.config(state=DISABLED)

window = Tk()
window.title("Rock Scissors Paper")
window.geometry("500x500")

equation_text = ""
uscore = 0
pcscore = 0

equation_label = StringVar()

frame = Frame(window)
frame.pack()

scissor_image = PhotoImage(file='scissor.png')
rockImage = PhotoImage(file='rock.png')
paperImage = PhotoImage(file='paper.png')

button1 = Button(frame, text='Paper', height=50, width=50, font=35, image=paperImage, compound='bottom', command=lambda: button_click("paper"))
button1.grid(row=0, column=0)

button2 = Button(frame, text='Scissors', height=50, width=50, font=35, image=scissor_image, compound='bottom', command=lambda: button_click("scissors"))
button2.grid(row=0, column=1)

button3 = Button(frame, text='Rock', height=50, width=50, font=35, image=rockImage, compound='bottom', command=lambda: button_click("rock"))
button3.grid(row=0, column=2)

clear_button = Button(window, text='Clear', height=4, width=9, font=35, command=clear)
clear_button.pack()

label = Label(window, textvariable=equation_label, font=('consolas', 20), bg='#33cc33', width=50, height=8, compound='center')
label.pack()

fscore = Text(window, height=1, width=40)
fscore.config(state=DISABLED)
fscore.pack()

window.mainloop()
