class Car:
    def __init__(self, manufacturer = '', model = None, color = '', cylinder = 0.0):
        # __ privado, no se puede usar fuera de la clase
        self.__manufacturer = manufacturer
        self.__model = model
        self.__color = color
        self.__cylinder = cylinder
        # _ protegido, se puede usar fuera de la clase
        self._other = 'motor'

    # 1 manera de configurar get, setter
    def set_model(self, value):
        self.__model = value

    def get_model(self):
        return self.__model

    def set_color(self,value):
        self.__color = value

    def get_color(self):
        return self.__color

    # 2 manera de configurar get, setter. Importante el orden tal como esta ahora mismo
    @property
    def cylinder(self):
        return self.__cylinder

    @cylinder.setter
    def cylinder(self, value):
        self.__cylinder = value

    def details(self):
        detail = ""
        detail += f'car.manufacturer: {self.__manufacturer}\n'
        detail += f'car.manufacturer: {self.__model}\n'
        detail += f'car.manufacturer: {self.__color}\n'
        detail += f'car.manufacturer: {self.__cylinder}\n'
        return detail


car = Car('Subaru')
car.set_color('Gris')
car.set_model('Impreza')
car.cylinder = 1.5
print(car.get_color())
print(car.details())

mazda = Car()
print(mazda.details())
mazda._other = 'otro'
print(mazda._other)