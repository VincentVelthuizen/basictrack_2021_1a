from tkinter import *


class Calculator(Frame):

    def __init__(self, master=None):
        # general settings for the window
        Frame.__init__(self, master=master)
        self.option_add("*Font", "arial 20 bold")
        self.master.title("Calculator")

        # In-/output field
        self.leftNumber = None
        self.rightNumber = None
        self.operator = None

        self.displayText = StringVar()
        self.display = Entry(root, textvariable=self.displayText, justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # setup buttons     [0,     1,      2,      3,      4]
        buttonGridLayout = ["C±^q", "789/", "456*", "123-", "0.=+"]
        for row, buttonRowlayout in enumerate(buttonGridLayout):
            for column, buttonText in enumerate(buttonRowlayout):
                if buttonText.isnumeric():
                    button = Button(root, text=buttonText,
                                    command=lambda number=buttonText: self.number_button(number))
                else:
                    button = Button(root, text=buttonText,
                                    command=lambda operator=buttonText: self.operator_button(operator))
                button.grid(row=(row + 1), column=column, sticky=N+S+E+W, padx=5, pady=5)

    def number_button(self, number):
        self.displayText.set(self.display.get() + number)

    def operator_button(self, operator):
        if operator == "C":
            self.displayText.set("")
        elif operator == "=":
            self.evaluate()
        elif operator == ".":
            if operator not in self.displayText.get():
                self.displayText.set(self.displayText.get() + operator)
        elif operator == "±":
            self.displayText.set(-1 * float(self.displayText.get()))
        elif operator == " ":
            pass
        else:
            self.leftNumber = float(self.displayText.get())
            self.displayText.set("")
            self.operator = operator

    def evaluate(self):
        self.rightNumber = float(self.displayText.get())
        if self.operator == "-":
            self.displayText.set(self.leftNumber - self.rightNumber)
        elif self.operator == "+":
            self.displayText.set(self.leftNumber + self.rightNumber)
        elif self.operator == "/":
            self.displayText.set(self.leftNumber / self.rightNumber)
        elif self.operator == "*":
            self.displayText.set(self.leftNumber * self.rightNumber)
        elif self.operator == "^":
            self.displayText.set(self.leftNumber ** self.rightNumber)
        elif self.operator == "q": # n-th root
            self.displayText.set(self.leftNumber ** (1 / self.rightNumber))
        self.operator = "done"


if __name__ == "__main__":
    root = Tk()
    Calculator(root).mainloop()
