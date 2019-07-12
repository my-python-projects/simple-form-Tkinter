from Person import Person

class Register_Control:
    def __init__(self, name, email, password):
        self.person = Person(name, email, password)

        self.name = 'Name: {}'.format(self.person.get_name())
        self.email = 'Email: {}'.format(self.person.get_email())
        self.password = 'Password: {}'.format(self.person.get_password())

        self.print_console()


    def print_console(self):

        print('\n Name: ', self.person.get_name(), \
            '\n Email: ', self.person.get_email(), \
            '\n Password: ', self.person.get_password()
        )

        self.save()

    def save(self):
        try:
            self.file_name = '{}.txt'.format(self.person.get_name())

            self.file = open(self.file_name, 'w')
            self.file.write(self.name)
            self.file.write('\n')
            self.file.write(self.email)
            self.file.write('\n')
            self.file.write(self.password)

        except:
            print('Error saving data')

        finally:
            self.file.close()
            print('Data saved successfully')