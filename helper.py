def print_ascending(height):
    output = ""
    # go through the height and print appropriate spaces along with the vales
    for i in range(1,height + 1):
        output += (int(height - i) * ' ') + ( i * '*') + ( int(i-1) * '*')+ '\n'
    return output

def print_descending(height):
    output = ""
    # go through the height in reverse order and print the tree appropriately
    for i in range(height, 0, -1):
        output += (int(height- i) * ' ') +( i * '*') + ( int(i-1) * '*')+ '\n'
    return output