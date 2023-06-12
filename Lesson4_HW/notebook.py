import pickle

NoteType = dict({"id": int, "name": str, "price": float})


def asteriks(text: str = '') -> None:
    print('*' * 3, text)


class Notebook():
    def __init__(self, file_name: str = "notes.txt") -> None:
        self.__id = 0
        self.__notes: NoteType = []
        self.__file_name = file_name

    def __str__(self) -> str:
        return str(self.read_file())

    @property
    def item(self) -> list[NoteType]:
        return self.read_file()

    @item.deleter
    def item(self) -> None:
        self.__notes.pop()
        self.write_file()

    def delete_by_id(self, _id: int) -> None:
        self.__notes = [i for i in self.read_file() if i.get('id') != _id]
        self.write_file()

    def add_item(self, name: str, price: float) -> None:
        self.__id += 1
        self.__notes.append({"id": self.__id, "name": name, "price": price})
        self.write_file()

    def get_filtered(self, measures: [dict]) -> list[NoteType]:
        res = []
        for j in [i for i in self.read_file()]:
            [res.append(j) for k, v in j.items() if {k: v} in measures]
        return res

    def get_max_value(self) -> list[NoteType]:
        _max = max(map(float, [i.get('price') for i in self.read_file()]))
        return self.get_filtered([{"price": _max}])

    def read_file(self) -> list[NoteType]:
        try:
            with open(self.__file_name, 'br+') as file:
                return pickle.load(file)
        except Exception as err:
            print(err)

    def write_file(self) -> None:
        try:
            with open(self.__file_name, 'bw+') as file:
                pickle.dump(self.__notes, file)
        except Exception as err:
            print(err)


notebook1 = Notebook()
notebook1.add_item("Item1", 33)
notebook1.add_item("Item2", 34)
notebook1.add_item("Item3", 39)
notebook1.add_item("Item3", 35)
asteriks('Вивід всіх покупок')
print("Notebook", notebook1)
asteriks('Вивід всіх покупок, після видалення останньої')
del notebook1.item
print("Notebook_", notebook1)
asteriks('Вивід всіх покупок, з фільтрацією за списком критерієв')
a = notebook1.get_filtered([{'price': 33}, {"id": 2}, {'price': 33}])
print(a)
asteriks('Вивід покупки з найбільшим значенням ціни')
print(notebook1.get_max_value())
asteriks('Вивід всіх покупок, після видалення за id')
notebook1.delete_by_id(1)
print(notebook1)
