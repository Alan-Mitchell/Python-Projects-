def calcBills():#this created a function
    myBills={'Electric':120.00,'Rent':1200.00,'Water':60.00,
             'Car Insurance':75.00,'Phone':65.00}
    toal=0
    for i in myBills:
        total += myBills[i]
    oweed='The total owed for bills this month is: ${}'.format(total)
    return owed
class name:
    def __init__(self,firstName,lastName):
        #Initializing values for future objects created from this class
        self.firstName=firstName
        self.lastName=lastName
    def printName(self):
        print('Hello, I am {0} {1}'.format(self.firstName, self.lastName))

#Passing in the actual object values

person=name('Dustin','Smith')
person.printName()


__main__        
        
