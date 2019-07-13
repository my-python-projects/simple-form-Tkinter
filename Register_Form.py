import tkinter as tk
from Register_Control import Register_Control

class Register_Form:
    def __init__(self):
        self.__createView()


    def __createView(self):
        self.window = tk.Tk()
        self.window.geometry('400x300+200+200')
        self.window.title('JProgram - Simple Registration Form')
        self.__createForm()
        self.window.mainloop()


    def __createForm(self):
        self.__createLabel('Your Name: ', 80)
        self.inputName = self.__createInput(100)

        self.__createLabel('Email: ', 130)
        self.inputEmail = self.__createInput(150)

        self.__createLabel('Password: ', 180)
        self.inputPassword = self.__createInput(200)
        self.inputPassword.config(show = '*')

        self.__createBtnSubmit()


    def __createLabel(self, txt, y):
        self.label = tk.Label(self.window, text=txt)
        self.label.place(x = 100, y = y)


    def __createInput(self, y):
        self.input = tk.Entry(self.window)
        self.input.place(x = 100, y = y)
        return self.input


    def __createBtnSubmit(self):
        self.button = tk.Button(self.window, text = 'Submit', width = 6, background = 'green', command = self.get_input_data)
        self.button.place(x=100, y=233)


    def get_input_data(self):
        self.control = Register_Control(self.inputName.get(), self.inputEmail.get(), self.inputPassword.get())
        self.respost = self. __createLabel('User created successfully', 40)