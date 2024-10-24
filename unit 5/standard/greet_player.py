class Villager:
    def __init__(self, name, species, personality, catchphrase, neighbor=None):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
        self.neighbor = neighbor


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

# alice = Villager("Alice", "Koala", "guvnor")
# print(alice.furniture)

# alice.add_item("acoustic guitar")
# print(alice.furniture)

# alice.add_item("cacao tree")
# print(alice.furniture)

# alice.add_item("nintendo switch")
# print(alice.furniture)


# alice = Villager("Alice", "Koala", "guvnor")

# alice.print_inventory()

# alice.furniture = ["acoustic guitar", "ironwood kitchenette", "kotatsu", "kotatsu"]
# alice.print_inventory()


def of_personality_type(townies, personality_type):
    group = []
    for townie in townies:
        if townie.personality == personality_type:
            group.append(townie.name)
    return group

isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

print(of_personality_type([isabelle, bob, stitches], "Lazy"))
print(of_personality_type([isabelle, bob, stitches], "Cranky"))


def message_received(start_villager, target_villager):
    current = start_villager
   
    while current is not None:
        if current == target_villager:
            return True
        current = current.neighbor
    
    return False



isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
isabelle.neighbor = tom_nook
tom_nook.neighbor = kk_slider

print(message_received(isabelle, kk_slider))
print(message_received(kk_slider, isabelle))