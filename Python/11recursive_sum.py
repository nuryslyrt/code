def recursive_sum(mylist):
    sum = 0
    for elem in mylist:
        if type(elem) == type([]):
            sum = sum + recursive_sum(elem)
            return sum
        else:
            sum = sum + elem
    return sum
