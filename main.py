
from helper import print_ascending, print_descending

# check the height of the tree
height = int(input("Welcome to tree exercise. Please input how big you want your tree to be like: "))

# check which direction we want to print. 1- Ascending, 2- Descending 
order = int(input("Select if you want your tree in ascending (1) or descending (2) order: "))

print("Here is your tree \n")
# we do it in ascending order


if(order == 1):
    print(print_ascending(height))
elif(order == 2):
    print(print_descending(height))
else:
    print("Unsupported order. Please try again. ")

