def read():
    f = open('Data/conf/help.txt', 'r')

    content = f.read()
    print(content)

    f.close()
