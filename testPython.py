def prob1():
    add = 0
    for i in range(10):
        add += i
    print(add)

def prob2():
    s1 = "Hello Class!"
    s2 = " I hope your Thanksgiving was great!"
    print(s1 + s2)

def prob3():
    pi = 22/7
    print(round(pi, 2))

def prob4():
    array = []
    for i in range(10):
        array.append(i)
    print(array)
    
if __name__ == '__main__':
    prob1()
    print("SPLIT")
    prob2()
    print("SPLIT")
    prob3()
    print("SPLIT")
    prob4()