from tkinter import *
import random
from tkinter import messagebox

n = random.randrange(1, 101)
nrepete = []
estado1 = 7  # início
estado2 = 7

tentativa = 0


def execute():
    global tentativa, estado2, estado1
    if tentativa < 10:  # only play if you still have turns
        palpite = form.get()
        try:
            palpite = int(palpite)
            nrepete.append(palpite)
            if (palpite < 1) or (palpite > 100):
                raise ValueError
            if nrepete.count(palpite) >= 2:
                raise NameError

            tentativa += 1
            if palpite == n:
                message = "Congratulations!  You hit the number {} after {} guess(es)!".format(n, tentativa)
                messagebox.showinfo("You win!", message)

            else:
                SetStatus(tentativa, palpite)
                if tentativa > 1:
                    estado1 = estado2

                message = FornecerPista()
                messagebox.showinfo("Status", message)

                if tentativa == 10 and palpite != n:
                    message = "Sorry, but after {} attempts. You didn't get the number {} I was thinking!".format(tentativa, n)
                    messagebox.showinfo("Game over", message)

        except NameError:
            messagebox.showerror("Error", 'This value has already been tested! Try again.')
        except ValueError:
            messagebox.showerror("Error", 'Invalid value! Try again.')


    else:
        messagebox.showinfo("Game over", "You've already lost.  The answer was {}".format(n))


def SetStatus(tentativa, palpite):
    global estado2
    x = abs(n - palpite)

    if x == 1:
        estado2 = 6  # Very Fricking Hot
    elif x == 2 or x == 3:
        estado2 = 5  # Very Hot
    elif 4 <= x <= 6:
        estado2 = 4  # Hot
    elif 7 <= x <= 9:
        estado2 = 3  # Warm
    elif 10 <= x <= 15:
        estado2 = 2  # Cold
    elif 16 <= x <= 25:
        estado2 = 1  # Very Cold
    elif x >= 26:
        estado2 = 0  # Freezing


def FornecerPista():
    message = ""
    if estado1 == 7:
        messages = ["Freezing!", "Very cold!", "Cold!", "Warm!", "Hot!", "Very hot!", "boiling"]
        message = messages[estado2] + "\n"

    elif estado1 == estado2:
        messages = ['freezing', 'very cold', "cold", "warm", "hot", "very hot", "boiling"]
        message += "Your hunch continues {}!".format(messages[estado2])

    elif estado1 > estado2:
        messages = ['freezing', 'very cold', "cold", "warm", "hot", "very hot"]
        message += "Oops, your hunch got cold and now it's {}!".format(messages[estado2])
    else:
        messages = ['very cold', "cold", "warm", "hot", "very hot", "boiling"]
        message += "Oops, your hunch got heated and now it's".format(messages[estado2 - 1])

    return message


i = Tk()

i.title('Guess Game')
i.geometry("400x200")

texto = Label(i, text="Welcome to the Guess Game")
texto.pack()

texto = Label(i, text="You have 10 chances to hit the number I'm thinking")
texto.pack()

texto = Label(i, text="This is a value between 1 and 100. So, come on!")
texto.pack()

form = Entry(i, width=3)
form.pack()

b = Button(i, text="Execute", fg="green", command=execute)
b.pack()

i.mainloop()