def add_two_numbers() -> int:
    userIn = input("")
    parseList = userIn.split(",")
    intSum = 0
    for e in parseList:
        intSum += int(e)
    return intSum



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
