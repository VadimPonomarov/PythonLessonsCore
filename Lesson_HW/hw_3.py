from abc import ABC, abstractmethod
from typing import List, Type


class Rectangle():
    def __init__(self, x: str | int | float, y: str | int | float) -> None:
        self.__x = float(x)
        self.__y = float(y)

    def get_area(self) -> float:
        return self.__x * self.__y

    def get_len(self) -> float:
        return (self.__x + self.__y) * 2

    def __str__(self) -> str:
        return f'Rectangle with area: {self.get_area()}'

    def __add__(self, other) -> float:
        return self.get_area() + other.get_area()

    def __sub__(self, other) -> float:
        return self.get_area() - other.get_area()

    def __eq__(self, other) -> bool:
        return self.get_area() == other.get_area()

    def __ne__(self, other) -> bool:
        return self.get_area() != other.get_area()

    def __gt__(self, other) -> bool:
        return self.get_area() > other.get_area()

    def __lt__(self, other) -> bool:
        return self.get_area() < other.get_area()

    def __len__(self) -> float:
        return self.get_len()


a = Rectangle(3, 5)
a.get_area()
print('Rectangular a', a)
b = Rectangle(8, 9)
print('Rectangular b', b)
print('sum: ', a + b)
print('sub: ', a - b)
print('equality: ', a == b)
print('not equality: ', a != b)
print('length: ', 'a: ', a.__len__(), 'length: ', 'b: ', b.__len__())


class Human():

    def __init__(self, name: str, age: int) -> None:
        self.__name = name.capitalize()
        self.__age = age

    def __str__(self) -> str:
        return self.__name

    def get_about(self) -> dict:
        return {'name': self.__name, 'age': self.__age}


class Cinderella(Human):
    __counter = 0

    def __init__(self, name: str = None, age: int = None, size: int = None) -> None:
        super().__init__(name, age)
        self.__size = size
        self.set_counter()

    @classmethod
    def set_counter(cls) -> None:
        cls.__counter += 1

    def __iter__(self) -> dict:
        return self.get_about()

    def get_about(self) -> dict:
        return {**super().get_about(), 'size': self.__size}


class Prince(Human):

    def __init__(self, name: str, age: int, boot_size: int) -> None:
        super().__init__(name, age)
        self.__boot_size = boot_size

    def filter_cinderella_list(self, cinderella_list: List[Cinderella]) -> List[dict]:
        return [i.get_about() for i in cinderella_list if i.get_about().get('size') == self.__boot_size]


cinderellas = [Cinderella(name=f'Cinderella {i}', age=17 + i, size=35 + i) for i in range(11)]
for i in cinderellas:
    print(i)

prince = Prince('Prince', 18, 37)

print(prince.get_about())
print('True cinderella: ', prince.filter_cinderella_list(cinderellas))


class Printable(ABC):
    def __init__(self, name: str) -> None:
        self.__name = name

    def __str__(self) -> str:
        return self.__name

    @abstractmethod
    def print(self) -> None:
        pass


class Book(Printable):

    def __init__(self, name: str) -> None:
        super().__init__(name)

    def print(self) -> None:
        print(self)


class Magazine(Printable):

    def __init__(self, name: str) -> None:
        super().__init__(name)

    def print(self) -> None:
        print(self)


class Main():
    __printable_list = []

    @classmethod
    def add(cls, item: Book | Magazine):
        if type(item) in [Book, Magazine]:
            cls.__printable_list.append(item)

    @classmethod
    def filter_items(cls, type: Type[Book | Magazine]) -> List[Book | Magazine]:
        return [i for i in cls.__printable_list if isinstance(i, type)] if len(cls.__printable_list) else []

    @classmethod
    def show_all_magazines(cls) -> None:
        for i in cls.filter_items(Magazine):
            i.print()

    @classmethod
    def show_all_books(cls) -> None:
        for i in cls.filter_items(Book):
            i.print()


Main.add(Book('Book1'))
Main.add(Magazine('Magazine3'))
Main.add(Magazine('Magazine2'))
Main.add(Book('Book2'))

Main.show_all_magazines()
print('-' * 40)
Main.show_all_books()
