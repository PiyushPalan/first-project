import tkinter as tk
from game import get_secret_number, check_guess


class GameGUI:

    def __init__(self):

        self.secret_number = get_secret_number()

        self.window = tk.Tk()
        self.window.title("Guess The Number")

        self.label = tk.Label(self.window, text="Guess a number (1-10)")
        self.label.pack()

        self.entry = tk.Entry(self.window)
        self.entry.pack()

        self.button = tk.Button(self.window, text="Submit", command=self.submit_guess)
        self.button.pack()

        self.result = tk.Label(self.window, text="")
        self.result.pack()

    def submit_guess(self):

        guess = int(self.entry.get())

        message = check_guess(self.secret_number, guess)

        self.result.config(text=message)

    def run(self):
        self.window.mainloop()