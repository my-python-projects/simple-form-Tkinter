from Person import Person

class Register_Control:

    def createPerson(self, name, email, password):
        self.person = Person(name, email, password)

        self.printVal()


    def printVal(self):
        print(
            '\n Name: ', self.person.getName(),
            '\n Email: ', self.person.getEmail(),
            '\n Password: ', self.person.getSenha()
        )
