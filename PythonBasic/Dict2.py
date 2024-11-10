# Define a dictionary containing car prices for different brands
car_price = {"opel": 5000, "toyota": 7000, "bmw": 10000}

# Access and print the price of the "bmw"
print(car_price["bmw"])

# Add a new car brand "mazda" with its price to the dictionary
car_price["mazda"] = 8000

# Print the updated car_price dictionary, which now includes "mazda"
print(car_price)


# Define a dictionary representing a person's information
person = {
    "first name": "Joe",
    "last name": "Black",
    "age": 43,
    "hobbies": ["painting", "IT", "weed"],  # List of hobbies
    "relatives": {  # Nested dictionary for relatives
        "wife": "Anna",
        "dog": "Tokyo",
        "mamka": "Larisa"
    }
}

# Access and print the person's third hobby
print(person["hobbies"][2])

# Access and print the name of the person's dog
print(person["relatives"]["dog"])

# Print all the keys in the person dictionary
print(person.keys())

# Print all the values in the person dictionary
print(person.values())


# Define a dictionary representing a computer's specifications
Computer = {
    "Brand": "Apple",
    "processor": {  # Nested dictionary with processor details
        "Destiny": "main operating system",
        "name": "Intel Core i5-12400F",
        "main parameters": "2.5GHz/18MB"
    },
    "Monitor": {  # Nested dictionary with monitor details
        "brand": "Apple",
        "size": "23.8",
        "IPS": "240"
    },
    "keyboard": {  # Nested dictionary with keyboard details
        "name": "AppleKeyBoard",
        "Destiny": "tool for interaction with CPU"
    }
}

# Note: This is a corrected version with dictionary syntax errors fixed

}