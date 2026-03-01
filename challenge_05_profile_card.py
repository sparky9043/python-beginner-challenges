"""
Enter your name: Alex
Enter your age: 24
Enter your height in metres: 1.75
Enter your favourite number: 7
"""
person_name = str(input("Enter your name: "))
person_age = int(input("Enter your age: "))
person_height_in_metres = float(input("Enter your height in metres: "))
person_favourite_number = int(input("Enter your favourite number: "))

person_height_in_centimetres = int(person_height_in_metres * 100)

print("================================")
print("\tYOUR PROFILE CARD")
print("================================")
print(f"Name:\t\t\t{person_name}")
print(f"Age:\t\t\t{person_age} years")
print(f"Height:\t\t\t{person_height_in_metres:.2f}m ({person_height_in_centimetres}cm)")
print(f"Favourite Number:\t{person_favourite_number}")
print("================================")