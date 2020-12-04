"""The module allowing to open the help file"""
def read():
    """
    Prints the help file in the console
    """
    f = open('Data/conf/help.txt', 'r')

    content = f.read()
    print(content)

    f.close()
