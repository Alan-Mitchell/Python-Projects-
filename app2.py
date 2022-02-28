

import app

def print_app2():
    name=(__name__)
    return name

if __name__ == '__name__':
    #the following is calling code from within the script
    print('I am running code {}'.format(print_app2()))

    #the following is calling code from the imported app.py
    print('I am running code {}'.format(app.print_app()))

