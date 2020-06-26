from time import sleep
def mostrador(item):
    print(item)

def contador(i, f, p):
    for i in range(i, f + 1, p):
        mostrador(i)
        sleep(1)

contador(10, 20, 2)