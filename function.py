def choice():
    options = ['Add','Sub','Mul','Div']
    for i in range(4):
        print(i," for ",options[i])
    choice.ch = int(input("Enter choice:"))

def input_data():
    global x,y
    x = int(input("Enter x:"))
    y = int(input("Enter y:"))

def add():
    return (x+y)
def sub():
    return (x-y)
def mul():
    return (x*y)
def div():
    return (x/y)

def operations():
    options = [add(),sub(),mul(),div()]
    print(options[choice.ch])

def repeat():
    while True:
        select = input("Do you want continue with same number then Press 'Y' for yes or Press 'N' for No:")
        if select == 'Y' or select == 'y':
            choice()
            operations()
        elif select == 'N' or select == 'n':
            select2 = input("Do you want continue with another number then Press 'Y' for yes or Press 'N' for No:")
            if select2 == 'Y' or select2 == 'y':
                choice()
                input_data()
                operations()
            else:
                print("Thank You")
                break

choice()
input_data()
operations()
repeat()
