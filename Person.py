class Person:
    def __init__(self, name, email, senha):
        self.__name = name
        self.__email = email
        self.__senha = senha

    def getName(self):
        return self.__name

    def getEmail(self):
        return self.__email

    def getSenha(self):
        return self.__senha