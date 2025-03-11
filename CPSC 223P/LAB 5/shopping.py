# Name: Matthew Lim
# Date: 02/27/25
# Description: 

from collections import deque

today_sale = {}

def get_total_item(cart, /):
    total = 0.0
    for item in dict(cart):
        total = total + cart[item]
    # print("Total: ", total)
    return total

def check_out_queue(*names):
    queue = deque(names)
    # print("Queue:", queue)
    return queue

def add_customer_cart(name, /, **keywords):
    today_sale[name] = keywords
    # print(today_sale)

def look_up_customer_cart(name, /):
    if name in today_sale:
        for k, v in today_sale[name].items():
            print(k, ":", v)
        # print("Total: ", get_total_item(today_sale[name]))
    else:
        raise KeyError("Cart not found")

def remove_item(name, item, /):
    if name in today_sale:
        if item in today_sale[name]:
            del today_sale[name][item]
        # else:
        #     print("Item not found")
    # else:
    #     print("Name not found")
    
def apply_discount(name, /):
    discount = 0
    if ((len(name) % 3) == 0):
        discount = discount + 10
    if (name[0].lower() in "aeiou"):
        discount = discount + 10 
    # print("Name: ", name)
    # print("Discount: ", discount, "%")
    return discount

def add_item(name, item, /, price = 0):
    if name in today_sale:
        today_sale[name][item] = price
        # if price == 0.0:
        #     print("The item is free")
    # else:
    #     print("Name not found")

def sale(queue):
    print(" ") # Spacer
    print("********************")
    while deque(queue):
        print(queue)
        name = queue.popleft()
        print("Serving ", name)
        print("********************")
        if name in today_sale:
            print(name, "'s Cart:")
            look_up_customer_cart(name)
            total = get_total_item(today_sale[name])
            discount = apply_discount(name)
            print("Customer", name, "gets", discount, "% discount")
            final_total = total * (1 - discount / 100)
            print("Total:", final_total)
            print("********************")
            del today_sale[name]
        else:
            print("No cart found.")
    if len(queue) == 0:
        print("Queue is empty.")



