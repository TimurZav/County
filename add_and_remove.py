
class AddRemove:
    name_county = {"Бразилия", "Бельгия", "	Германия", "Индия"}

    def __init__(self, name_county):
        self.name_county = name_county

    def add(self):
        add_country = str(input("Введите любую страну"))
        self.name_county.append(add_country)


