def divideBy2(decNumber):

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber / 2

        binString = ""
        while not remstack.isEmpty():
            binString = binString + repr(remstack.pop())
        return binString
