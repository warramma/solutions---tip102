class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []


    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"

    def set_catchphrase(self, new_catchphrase):
        alphabet = "abcdefghijklmnopqrstuvwxyz "
        if len(new_catchphrase) >= 20:
            return "Invalid catchphrase"
        else:
            for char in new_catchphrase:
                if char.lower() not in alphabet:
                    print("Invalid catchphrase")
                    return 
               
            print("catchphrase updated!")
            self.catchphrase = new_catchphrase
    def add_item(self, item_name):
        valid = ["acoustic guitar","ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]

        if item_name in valid:
            self.furniture.append(item_name)
    def print_inventory(self):
        my_dict = {}
        furniture = self.furniture
        for item in furniture:

            if item in my_dict:
                my_dict[item] +=1
            else:
                my_dict[item] = 1
        
        if not my_dict:
            print("Inventory empty!!!")
        else:
            inventory_string = ", ".join(f"{item}: {quantity}" for item, quantity in my_dict.items())
            print(inventory_string)
# bones = Villager("Bones", "Dog", "yip yip")
# bones.catchphrase = "ruff it up"

# print(bones.greet_player("Wardiyah"))
# print(bones.name)
# print(bones.species)  
# print(bones.catchphrase) 
# print(bones.furniture) 


# alice = Villager("Alice", "Koala", "guvnor")

# alice.set_catchphrase("sweet dreams")
# print(alice.catchphrase)
# alice.set_catchphrase("#?!")
# print(alice.catchphrase)

alice = Villager("Alice", "Koala", "guvnor")
print(alice.furniture)

alice.add_item("acoustic guitar")
print(alice.furniture)

alice.add_item("cacao tree")
print(alice.furniture)

alice.add_item("nintendo switch")
print(alice.furniture)


alice = Villager("Alice", "Koala", "guvnor")

alice.print_inventory()

alice.furniture = ["acoustic guitar", "ironwood kitchenette", "kotatsu", "kotatsu"]
alice.print_inventory()