#importing needed modules.
from abc import ABC, abstractmethod
#class creation
class Data(ABC):
    def dataUsage(self, amount):
        print('Your data uage for this month: ',amount)

        @abstractmethod
        def data_amount(self,amount):
            pass


class dataPlan(Data):

    def data_amount(self,amount):
        print('Your data amount of {} exceeded your 12gb limit '.format(amount))

obj= dataPlan()
obj.dataUsage('20gb')
obj.data_amount('$20gb')

        
