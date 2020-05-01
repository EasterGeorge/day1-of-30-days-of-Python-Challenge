
def twofer(name):
    if (name==""):
        print("One for "+ name +", one for me.")
    else:
        print("One for you, one for me.")
        
if __name__ == '__main__':
    name = input("Input your name")
    twofer(name)