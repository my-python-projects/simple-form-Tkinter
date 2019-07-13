from Person import Person
import datetime

class Register_Control:
    def __init__(self, name, email, password):
        self.get_date()

        self.person = Person(name, email, password)
        self.name = 'Name: {}'.format(self.person.get_name())
        self.email = 'Email: {}'.format(self.person.get_email())
        self.password = 'Password: {}'.format(self.person.get_password())

        self.print_console()

    def get_date(self):
        self.current_date = datetime.datetime.now()

        self.text_date = '{}_{}_{}'.format(self.current_date.day, self.current_date.month, self.current_date.year)
        self.text_time_data = 'Date created: {}'.format(self.current_date.strftime("%d/%m/%Y  %H:%M"))


    def print_console(self):

        print('\n Name: ', self.person.get_name(), \
            '\n Email: ', self.person.get_email(), \
            '\n Password: ', self.person.get_password()
        )

        self.save()

    def save(self):
        try:

            self.file_name = '{}_{}.txt'.format(self.person.get_name(),self.text_date)
            self.file = open(self.file_name, 'w')

            self.file.write(self.name)
            self.file.write('\n')
            self.file.write(self.email)
            self.file.write('\n')
            self.file.write(self.password)
            self.file.write('\n')
            self.file.write(self.text_time_data)

        except:
            print('Error saving data')

        finally:
            self.file.close()
            print('Data saved successfully')