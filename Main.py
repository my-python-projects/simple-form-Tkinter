from view.Register_Form import Register_Form
from connection.db import DB

if __name__ == '__main__':
    DB().create_conn()
    form = Register_Form()