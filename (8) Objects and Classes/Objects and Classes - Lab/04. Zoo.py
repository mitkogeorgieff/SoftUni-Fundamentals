class Zoo:
    __animals = 0

    def __init__(self, name):
        self.zoo_name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animals(self, species, name):
        if 'mammal' == species:
            self.mammals.append(name)
        elif "fish" == species:
            self.fishes.append(name)
        elif "bird" == species:
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        curr_list = []
        if species == "mammal":
            curr_list = self.mammals
            species = "Mammals"
        elif species == "fish":
            curr_list = self.fishes
            species = "Fishes"
        elif species == "bird":
            curr_list = self.birds
            species = "Birds"
        return f"{species} in {self.zoo_name}: {', '.join(curr_list)}\nTotal animals: {Zoo.__animals}"


zoo_name = input()
rows = int(input())

zoo = Zoo(zoo_name)

for animal in range(rows):
    species, name = input().split()
    zoo.add_animals(species, name)

info = input()
print(zoo.get_info(info))
