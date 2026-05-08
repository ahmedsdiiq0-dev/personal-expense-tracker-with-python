expenses= []

print("-----------------------------")
print("Welcome to the personal Expense tracker ! ")
print("-----------------------------")

class item :
    def __init__(self,name,price,catg):
        self.name = name
        self.price = price
        self.catg = catg

    def add_to_list(self):
        expenses.append(self)


while True :
    item_name = input("Type the name of the item you want to add (type q to stop) : ")
    if item_name.lower() == "q" :
        break  
    item_price = input("Type the price of the item you want to add (type q to stop) : ")
    if item_price.lower() == "q" :
        break
    item_catg = input("Type the category of the item you want to add (type q to stop) : ")
    if item_catg.lower() == "q" :
        break
    try :
        item_price = float(item_price)
        new_item = item(item_name,item_price,item_catg)
        new_item.add_to_list()
        print("added !")
    except ValueError:
        print("invalid input !")
total_expenses = 0
for i in expenses :
    total_expenses += i.price
print("-----------------------------")
print(f"Your total expenses is : {total_expenses}")
for i in expenses :
    print(f"item name : {i.name} , item price : {i.price} , item category : {i.catg}")
print("-----------------------------")