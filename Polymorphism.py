class French:
    def say_hello(self):
        print('Bonjour')

class Chinese:
    def say_hello(self):
        print('Ni hao')
        

def intro(lang):
    lang.say_hello()

Alan = French()
Mitchell = Chinese()

intro(Alan)

intro(Mitchell)
