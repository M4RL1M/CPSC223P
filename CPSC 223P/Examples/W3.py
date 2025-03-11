# functions and arguments/parameters

# Tuesday 02/04 Lecture
def print_all(*args, **kwargs):
    print("positional arguments: ")
    for arg in args:
        print(arg)

    print("keyword arguments")
    for key, value in kwargs:
        print(key, value)

print_all("apple", "god", ["0","1"])



def add(x, y):
    result = x + y
    print(result)

add(7, 8)

print((lambda x, y : x+y )(7, 8))


# Thursday 02/06 Lab
# file 1 (commented out due to errors)
# import get_numbers #file name
def add_nums():
    #num1, num2 = get_numbers.get_nums()
    #sum = num1 + num2
    #print("Sum: ",sum)

# file 2
# def get_nums():
    num1 = float(input("Input the first:"))
    num2 = float(input("Input the second:"))
    return num1, num2
