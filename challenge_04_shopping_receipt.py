item_name_1 = input("Enter item 1 name: ")
item_price_1 = float(input("Enter item 1 price: "))
item_name_2 = input("Enter item 2 name: ")
item_price_2 = float(input("Enter item 2 price: "))
item_name_3 = input("Enter item 3 name: ")
item_price_3 = float(input("Enter item 3 price: "))

total_price = item_price_1 + item_price_2 + item_price_3

print("---------------------")
print(f"{item_name_1}\t\t${item_price_1:.2f}")
print(f"{item_name_2}\t\t${item_price_2:.2f}")
print(f"{item_name_3}\t\t${item_price_3:.2f}")
print("---------------------")
print(f"TOTAL\t\t${total_price:.2f}")