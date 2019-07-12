from Person import Person

class Register_Control:

    def createPerson(self, name, email, password):
        self.person = Person(name, email, password)

        self.printVal()


    def printVal(self):

        print('\n Name: ', self.person.getName(), \
            '\n Email: ', self.person.getEmail(), \
            '\n Password: ', self.person.getSenha()
        )
        self.save()

    def save(self):
        try:
            self.name = 'Name: {}'.format(self.person.getName())
            self.arquivo = '{}.txt'.format(self.person.getName())
            self.f = open(self.arquivo, 'w')
            self.f.write(self.name)
            self.f.write('\n')

        except:
            print('Erro')

        finally:
            self.f.close()
            print('Dados salvos com sucesso')