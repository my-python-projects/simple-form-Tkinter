import tkinter as tk
from Person import Person

class Register_Form:
    def __init__(self):
        self.main()

    def createLabel(self, txt, y):
        self.label = tk.Label(self.window, text=txt)
        self.label.place(x = 100, y = y)

    def createInput(self, y):
        self.input = tk.Entry(self.window)
        self.input.place(x = 100, y = y)
        return self.input

    def createBtnSubmit(self):
        self.button = tk.Button(self.window, text = 'Submit', width = 6, background = 'green', command = self.printDatas)
        self.button.place(x=100, y=233)

    def createPerson(self):
        self.name = self.inputName.get()
        self.email = self.inputEmail.get()
        self.senha = self.inputPassword.get()

        self.person = Person(self.name, self.email, self.senha)

    def printDatas(self):
        self.createPerson()

        self.respost = tk.Label(self.window, text = 'User created successfully')
        self.respost.place(x=100, y=40)

        print(
            '\n Name: ', self.person.getName(),
            '\n Email: ', self.person.getEmail(),
            '\n Password: ', self.person.getSenha()
        )

    def createForm(self):
        self.createLabel('Your Name: ', 80)
        self.inputName = self.createInput(100)

        self.createLabel('Email: ', 130)
        self.inputEmail = self.createInput(150)

        self.createLabel('Password: ', 180)
        self.inputPassword = self.createInput(200)

        self.createBtnSubmit()

    def main(self):
        self.window = tk.Tk()
        self.window.geometry('400x300+200+200')
        self.window.title('JProgram - Simple Registration Form')
        self.createForm()
        self.window.mainloop()

if __name__ == '__main__':
    form = Register_Form()