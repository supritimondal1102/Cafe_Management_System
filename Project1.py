#Define the manu of restaurent
menu = {
    'Pizza':90,
    'pasta':85,
    'Burger':70,
    'Salad':65,
    'Coffee':75,
    'Noodles':60,
}

#Greed
print("Welcome to PYTHON Restaurent")
print("Pizza: Rs90\n Pasta: Rs85\n Burger:Rs70\n Salad: Rs65\n Coffee: Rs75\n Noodles : Rs60 ")

order_total = 0
#90 + 70 = 160

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1] #0 + 90
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Ordered item {item_1} is not avaialable yet!")

another_order = input("Do you want to add another item? (Yes/No) ")
if another_order == "yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"ordered item {item_2} is not avaialable!")

print(f"The total amount of items to pay is {order_total}")                