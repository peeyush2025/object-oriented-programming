class Dog:
    species = "Canine"
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Breed: {self.breed}")
        print(f"Species: {Dog.species}")
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Rocky", "German Shepherd")
dog1.display_details()
dog2.display_details()
