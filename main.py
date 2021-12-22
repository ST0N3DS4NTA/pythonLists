if __name__ == '__main__':
    N = int(input())
    lst = list()

    for i in range(N):
        userInput = input().split(' ')

        if userInput[0] == "insert":
            lst.insert(int(userInput[1]), int(userInput[2]))

        if userInput[0] == "print":
            print(lst)

        if userInput[0] == "remove":
            lst.remove(int(userInput[1]))

        if userInput[0] == "append":
            lst.append(int(userInput[1]))

        if userInput[0] == "sort":
            lst.sort()

        if userInput[0] == "pop":
            lst.pop()

        if userInput[0] == "reverse":
            lst.sort(reverse=True)

