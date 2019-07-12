from Person import Person

class Register_Control:
    def __init__(self, name, email, password):
        self.person = Person(name, email, password)

        self.name = 'Name: {}'.format(self.person.getName())
        self.email = 'Email: {}'.format(self.person.getEmail())
        self.password = 'Password: {}'.format(self.person.getSenha())

        self.print_val()


    def print_val(self):

        print('\n Name: ', self.person.getName(), \
            '\n Email: ', self.person.getEmail(), \
            '\n Password: ', self.person.getSenha()
        )
        self.save()

    def save(self):
        try:
            self.arquivo = '{}.txt'.format(self.person.getName())

            self.f = open(self.arquivo, 'w')
            self.f.write(self.name)
            self.f.write('\n')
            self.f.write(self.email)
            self.f.write('\n')
            self.f.write(self.password)

        except:
            print('Error saving data')

        finally:
            self.f.close()
            print('Data saved successfully')