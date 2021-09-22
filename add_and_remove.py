
class AddRemove:

    name_county = {"Бразилия", "Бельгия", "	Германия", "Индия"}
    add_country = str(input("Введите любую страну\n>>> "))
    remove_country = str(input("Удалите любую страну\n>>> "))


    # def __init__(self, name_county, add_country, remove_country):
    #     self.name_county = name_county
    #     self.add_country = add_country
    #     self.remove_country = remove_country

    def add(self):
        return self.name_county.add(self.add_country)

    def remove(self):
        return self.name_county.remove(self.remove_country)


addremove = AddRemove()
addremove.add()
