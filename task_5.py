"""
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw
(отрисовка). Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш),
Handle (маркер). В каждом из классов реализовать переопределение
метода draw. Для каждого из классов метод должен выводить
уникальное сообщение. Создать экземпляры классов и проверить,
что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    title: str

    def __init__(self, title: str):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        super().draw()
        print(f'{self.title} пишет текст')


class Pencil(Stationery):
    def draw(self):
        super().draw()
        print(f'{self.title} рисует картинку')


class Handle(Stationery):
    def draw(self):
        super().draw()
        print(f'{self.title} выделяет текст')


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')

stationery = [pen, pencil, handle]
for item in stationery:
    item.draw()
