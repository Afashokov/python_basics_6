"""
Реализуйте базовый класс Car. У данного класса должны быть
следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны
сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar,
PoliceCar. Добавьте в базовый класс метод show_speed, который
должен показывать текущую скорость автомобиля. Для классов
TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните
вызов методов и также покажите результат.
"""
import random


class Car:
    speed: int
    color: str
    name: str
    is_police: bool = False

    def __init__(self, speed: int, color: str, name: str) -> None:
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        if self.speed > 0:
            print(f"{self.name}: стартовал")
            print(f"{self.name}: набрал скорость {self.speed}")

    def stop(self):
        print(f"{self.name}: остановился")
        self.speed = 0

    def turn(self, direction: str):
        print(f"{self.name}: повернул - {direction}")

    def show_speed(self):
        print(f"{self.name}: скорость = {self.speed} км/ч")


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f"{self.name}: превысил скорость")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f"{self.name}: превысил скорость")


class PoliceCar(Car):
    is_police: bool = True


opel = TownCar(115, 'white', 'Opel')
bugatti = SportCar(320, 'black', 'Bugatti')
man = WorkCar(65, 'yellow', 'Man')
bmw = PoliceCar(360, 'black', 'BMW')

cars = [opel, bugatti, man, bmw]

for i in range(random.randint(50, 100)):  # рандомный перебор объектов и методов
    to_do = random.randint(1, 4)
    if to_do == 1:
        current_car = random.randint(0, 2)
        if cars[current_car].speed == 0:
            cars[current_car].speed = random.randint(15, 405)
            cars[current_car].go()
    if to_do == 2:
        current_car = random.randint(0, 2)
        if cars[current_car].speed > 0:
            cars[current_car].turn('налево')
    if to_do == 3:
        current_car = random.randint(0, 2)
        if cars[current_car].speed > 0:
            cars[current_car].turn('направо')
    if to_do == 4:
        current_car = random.randint(0, 2)
        if cars[current_car].speed > 0:
            cars[current_car].stop()

for car in cars:
    car.show_speed()
