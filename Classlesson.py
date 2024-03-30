class House:
    # Class representing a house
    def __init__(self, street, number):
        # Constructor to initialize the house with a street and number
        self.street = street
        self.number = number
    
    def build(self):
        # Method to simulate building the house
        print("Будинок на вулиці " + self.street + ", під номером " + str(self.number) + ", був побудований!")

# Create instances of the House class
House1 = House("Садова", 31)
House2 = House("Садова", 32)

# Print the street and number of House1
print(House1.street, House1.number)
House2.build() #call function build


    

