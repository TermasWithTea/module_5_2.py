class House:

    def __init__(self, name, number_of_flour):
        self.name = name
        self.number_of_flour = number_of_flour

    def go_to(self, new_flour):
        if 1 <= new_flour <= self.number_of_flour:
            for floor in range(1, new_flour + 1):
                print(f"прибытие на {floor} этаж")
        else:
            print("такого этажа не существует")

    def __len__(self):
        return self.number_of_flour

    def __str__(self):
      return(f'Название:{self.name}, кол-во этажей:{self.number_of_flour}')


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(len(h1))
print(len(h2))
