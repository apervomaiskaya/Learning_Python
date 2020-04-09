class Car():
    #Класс для представления автомобиля.
    def __init__(self, make, model, year):
    #Инициализирует атрибуты описания автомобиля."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
    #Возвращает аккуратно отформатированное описание."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
    #Выводит пробег машины в милях
        print('Эта машина разгоняется до', self.odometer_reading, 'миль/час')

    def update_odometer(self, mileage):
        # Устанавливает на одометре заданное значение.
        # При попытке обратной подкрутки изменение отклоняется.
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('Вы не можете откручивать одометр назад!')

    def increment_odometer(self, miles):
        #Увеличивает показания одометра с заданным приращением."""
        self.odometer_reading += miles

class Battery(Car):
    """Простая модель аккумулятора электромобиля."""
    def __init__(self, battery_size=75):
        """Инициализирует атрибуты аккумулятора."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Выводит приблизительный запас хода для аккумулятора."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print('This car can go about', range, 'miles on a full charge.')

    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100
            print('Мощность батареи увеличена до 100%!')

class ElectricCar(Car):
    #Представляет аспекты машины, специфические для электромобилей.
    def __init__(self, make, model, year):
        """инициализирует атрибуты класса-родителя."""
        super().__init__(make, model, year)
        self.battery_size = Battery()

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        print('This car has a', self.battery_size, 'kWh battery.')

    def fill_gas_tank(self):
        """У электромобилей нет бензобака."""
        print("У электромобилей нет бензобака!")


