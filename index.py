riddle =  input("insert riddle ")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def solver(problem, num):
    resolvedMinus = ""
    resolvedPlus = ""
    for letter in problem.replace(" ", ""):
        if alphabet[alphabet.index(letter) - num]:
            resolvedMinus += alphabet[alphabet.index(letter) - num]
        elif alphabet[alphabet.index(letter) + num]:
            print(alphabet.index(letter) + num)
            resolvedPlus += alphabet[alphabet.index(letter) + num]
        else:
            print("ne radi")
    print(resolvedPlus.replace("", " "))
    print(resolvedMinus.replace("", " "))


for i in range(0, len(alphabet)-1):
    solver(riddle, i)
