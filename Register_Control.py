from model.Person import Person
import datetime
import os
from model.DAO.PersonDAO import PersonDAO

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
        print(
            '\n Name: ', self.person.get_name(), \
            '\n Email: ', self.person.get_email(), \
            '\n Password: ', self.person.get_password()
        )
        self.save()

    def save(self):
        try:
            self.dir_path = os.path.dirname(os.path.realpath(__file__))
            self.folder = "logs"

            if not os.path.isdir(self.folder):
                os.mkdir(self.folder) # aqui criamos a pasta caso nao exista
                print ('Pasta criada com sucesso!')

            self.file_name = self.dir_path+ '/'+ self.folder+'/{}_{}.log'.format(self.person.get_name(),self.text_date)
            self.file = open(self.file_name, 'w')

            self.file.write(self.name)
            self.file.write('\n')
            self.file.write(self.email)
            self.file.write('\n')
            self.file.write(self.password)
            self.file.write('\n')
            self.file.write(self.text_time_data)

            self.person = {
                "nome": self.name,
                "email": self.email,
                "senha": self.password
            }
            
            PersonDAO().insert(self.person)

        except:
            print('\n Error saving data')

        finally:
            self.file.close()
            print('\n Data saved successfully')