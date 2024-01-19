from tkinter import *
from PIL import Image, ImageTk
from random import randint

# Main Window
root = Tk()
root.title('Rock Paper Scissor')
root.configure(background="#9b59b6")

# Images
rock_img = ImageTk.PhotoImage(Image.open("rock-user.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper-user.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissors-user.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissors.png"))

# insert images
user_label = Label(root, image=scissor_img)
comp_label = Label(root, image=scissor_img_comp)
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

# scores
playScore = Label(root, text=0, font=100, bg='#9b59b6', fg='white')
computerScore = Label(root, text=0, font=100, bg='#9b59b6', fg='white')
computerScore.grid(row=1, column=1)
playScore.grid(row=1, column=3)

# INDICATORS

user_indicator = Label(root, font=50, text="USER", bg='#9b59b6', fg='white')
comp_indicator = Label(root, font=50, text="COMPUTER", bg='#9b59b6', fg='white')
user_indicator.grid(row=0, column=3)
comp_indicator.grid(row=0, column=1)

# messages
msg = Label(root, font=50, bg='#9b59b6', fg='white', text="")
msg.grid(row=3, column=2)


# update messages

def updateMessage(x):
    msg['text'] = x


# update user score
def updateUserScore():
    score = int(playScore["text"])
    score += 1
    playScore["text"] = str(score)


# update computer score
def updateCompScore():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)


# check winner

def checkWin(player, computer):
    if player == computer:
        updateMessage("Its a tie..!!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You Loose..")
            updateCompScore()
        else:
            updateMessage("You Win..!!")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You Loose..")
            updateCompScore()
        else:
            updateMessage("You Win..!!")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("You Loose..")
            updateCompScore()
        else:
            updateMessage("You Win..!!")
            updateUserScore()
    else:
        pass


# Update Choices

choices = ["rock", "paper", "scissor"]


def updateChoice(x):
    # for comp
    compChoice = choices[randint(0,2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)

    # for user
    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    checkWin(x, compChoice)


# buttons

rock = Button(root, width=20, height=2, text="ROCK", bg="#ff3e4d", fg="white",
              command=lambda: updateChoice("rock")).grid(row=2, column=1)
paper = Button(root, width=20, height=2, text="PAPER", bg="#FAD02E", fg="white",
               command=lambda: updateChoice("paper")).grid(row=2, column=2)
scissor = Button(root, width=20, height=2, text="SCISSOR", bg="#0ABDE3", fg="white",
                 command=lambda: updateChoice("scissor")).grid(row=2, column=3)

root.mainloop()
