def fibSequence(n):
    list = [0,1]
    if n <= 1:
        return list[n]
    elif (n + 1 < len(list)):
        return list[n + 1]
    else:
        fibNumber = fibSequence(n - 1) + fibSequence(n - 2)
        list.append(fibNumber)
    return (fibNumber)

print("The 15th number in the Fibonacci Sequence: ", fibSequence(15))
