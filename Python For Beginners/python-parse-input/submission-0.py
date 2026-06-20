from typing import List

def read_integers() -> List[int]:
    intInput = input("")
    intList = intInput.split(",")
    fin = [int(item) for item in intList]
    return fin

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
