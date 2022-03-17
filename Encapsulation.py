class Car:
    def __init__(self,speed,color):
        self._speed = speed
        self.__color = color

    def set_speed(self,value):
        self.__speed = value

    def get_speed(self):
        return self._speed

ford =Car(200,'red')
honda = Car(250,'blue')
audi = Car(300,'black')






