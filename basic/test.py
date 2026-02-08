import os

dec_num = 1.2

num = int(dec_num)

print(num)

# complex_num =  complex (2 + 3i)

Name = "sai"
print(type(Name))

"""

Multi line comment
Multi line comment
Multi line comment
Multi line comment

"""

print("hello", end="  * ")
print("world")


print("sai", "ram", sep="--")

# age = int(input("enter age:  "))

# print("Age: ", age)

print(5 << 2)

print(5 // 2)
print(5 / 2)

print(0.1 + 0.2 == 0.3)
print(3 ^ 4)

if num == 5:
    print("same")
elif num < 5 and num != 5:
    print("below")
else:
    print("above")


a, b = 5, 4

a, b = b, a

print(a, b)

print(r"\n")

my_tuple = (7, 8, 9)
print(my_tuple.index(9))
print(my_tuple[1:])
print(my_tuple + (4, 5))
print(my_tuple * 2)
# my_tuple[0] = 88  # not allowed
# print(my_tuple)

print("---------")


my_list = [11, 22, 44]
my_list.append(4)
print(my_list)

my_list.insert(1, 10)
print(my_list)

my_list.remove(22)
print(my_list)

my_list.sort()
print(my_list)


numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares)

L = [1, 2, 3, 4, 5]
for i in L:
    print(i, end=" ")
    i = i + 1


my_set = {2, 3, 4, "sai"}

my_set.add(False)
my_set.add(True)

print(my_set)


my_dict = {"name": "sai", "age": 36}

my_dict.update({"age": 45})
print(my_dict)

print("age" in my_dict)
print(45 in my_dict.values())
print("books" in my_dict)


my_dict.update({"books": ["book1", "book2"]})
print(my_dict)
print(my_dict.get("books"))

my_dict.pop("age")

print(my_dict)

os.system("cls")


def sayHello():
    print("Hay sai")


def add(a, b):
    """
    This function is to add two numbers
    """
    return a + b


# ** hello
print(add(5, 6.7))


def add_with_type(a: int, b: int) -> int:
    """
    This function is to add two numbers
    """
    return int(a + b)


sayHello()

add_with_type(add(5, 6.7))
print(add.__doc__)
