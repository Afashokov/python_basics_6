"""
Создать класс TrafficLight (светофор) и определить у него
один атрибут color (цвет) и метод running (запуск). Атрибут
реализовать как приватный. В рамках метода реализовать
переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7
секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на
ваше усмотрение. Переключение между режимами должно
осуществляться только в указанном порядке (красный, желтый,
зеленый). Проверить работу примера, создав экземпляр и вызвав
описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и
завершать скрипт.
"""
import time
import itertools


class TrafficLight:
    __color: str
    __timing: dict

    def __init__(self, red_time: int = 7, yellow_time: int = 2, green_time: int = 10):
        self.__timing = {'красный': red_time,
                         'желтый ': yellow_time,
                         'зеленый': green_time}

    def running(self):
        for current_color, timer in itertools.cycle(self.__timing.items()):
            self.__color = current_color
            for second in range(timer):
                print(f"\rТекущий цвет светофора = {self.__color} {second + 1}", end="")
                time.sleep(1)
                if second == timer - 1:  # нужно отключить, чтобы всегда была одна строка
                    print()


try:
    traffic_light_hrz1 = TrafficLight(7, 2, 10)
    traffic_light_hrz1.running()
except KeyboardInterrupt:
    print('\nВыход из программы')
