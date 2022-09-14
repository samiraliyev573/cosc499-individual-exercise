
from helper import print_ascending

# check the height of the tree
height = int(input("Welcome to tree exercise. Please input how big you want your tree to be like: "))

# check which direction we want to print. 1- Ascending, 2- Descending 
asc = int(input("Select if you want your tree in ascending (1) or descending (2) order: "))

print("Here is your tree \n")
# we do it in ascending order
if(asc == 1):
    print(print_ascending(height))


