# class instance
class French:
    def say_hello(self):
        print('Bonjour')
#class instance 
class Chinese:
    def say_hello(self):
        print('Ni hao')
        
# can call either class
def intro(lang):
    lang.say_hello()

Alan = French()
Mitchell = Chinese()

intro(Alan)

intro(Mitchell)
