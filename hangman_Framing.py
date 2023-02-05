from tkinter import *
import random
from collections import Counter

root = Tk()
root.geometry('1100x400+500+300')


def select(value):
    global guess
    guess = value
    print(guess)
    var_select.set(guess)

def play_again():
    global rando
    rando = random.choice(word_list)
    dash = len(rando)
    rando_word.set('__ ' *dash )

def play():
    play_again()

def enter():
    global guess
    if guess in rando:
        print('yes')
        guessed_letters.append(guess)
        letters_list.set(guessed_letters)
    else:
        print('nope')
        guessed_letters.append(guess)
        letters_list.set(guessed_letters)
    print(guessed_letters)

def replace():
    pass



rando_word = StringVar()
var_select = StringVar()
letters_list = StringVar()


guessed_letters = []
word_list = ['banana', 'devon', 'cat', 'look', 'whaaaaat']
butt = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


#Create Frames
left = Frame(root,  bg='green', bd=3)
left.place(x=0, width=400, height=400, y=0)
middle = Frame(root, padx=35, pady=25, bg='red')
middle.place(x=400, width=190, height=400, y=0)
right = Frame(root, bg='blue')
right.place(x=590, width=600, height=400, y=0)

guessed_frame = Frame(root, bg='purple')
guessed_frame.place(x=590, width=510, height=100,y=200)

answer_frame = Frame(root, bg='yellow')
answer_frame.place(x=590, width=510, height=100,y=300)

#Hangman window
li = Label(left, text="left", width=8, height=1, font=('Times',28), bg="yellow")
li.pack(fill=BOTH, expand=True)



#Middle window
your_choice = LabelFrame(middle, bd=10, text='Selection')
your_choice.pack(fill="both", expand="yes")
choice_entered = Label(your_choice, textvariable=var_select, font=('Times', 109))
choice_entered.pack()
enter_butt = Button(middle, text='Enter', command=enter)
enter_butt.pack(pady=20, padx=20)
play_butt = Button(middle, text='Play', command=play_again)
play_butt.pack(pady=20, padx=20)


#Keyboard window
guesses = Label(guessed_frame, text="Guesses:", font=('Times', 20)).grid(row=0, column=1,  sticky=W)
lab = Label(guessed_frame, font=('Times', 20), textvariable=letters_list).grid(row=0, column=2, pady=25)


#Hint window
answer_label = Label(answer_frame, height=1, bg='pink', anchor=S, textvariable=rando_word, font=('Times', 36))
answer_label.pack(expand=True, fill=BOTH)


varRow = 2
varColumn = 0

for button in butt:
    command = lambda x=button: select(x)
    Button(right, text=button, width=5, padx=4, pady=4, command = command).grid(row=varRow, column=varColumn, padx=4, pady=4)
    
    varColumn += 1
    if varColumn > 7 and varRow == 2:
        varColumn = 0
        varRow += 1
    if varColumn > 7 and varRow == 3:
        varColumn = 0
        varRow += 1
    if varColumn > 7 and varRow == 4:
        varColumn = 0
        varRow += 1
    if varColumn > 7 and varRow == 5:
        varColumn = 0
        varRow += 1
    if varColumn > 7 and varRow == 6:
        varColumn = 0
        varRow += 1


root.mainloop()