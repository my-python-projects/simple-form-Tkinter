from Register_Form import Register_Form
from db import DB

if __name__ == '__main__':
    DB().create_conn()
    form = Register_Form()