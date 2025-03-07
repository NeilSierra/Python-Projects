string = input("Enter string: ")
char = input("Enter character: ")

char_list = list(string)
char_list = [i if i != char else 0 for i in char_list]

def rScan(i):
    for j in range(len(char_list)):
        j += 1
        if i+j >= len(char_list):
            continue
        if char_list[i+j] == 0:
            return j

def lScan(i):
    for j in range(len(char_list)):
        j += 1
        if i-j < 0:
            continue
        if char_list[i-j] == 0:
            return j

def compare(x, y):
    if x != None and y != None:
        return min(x, y)
    elif x != None and y == None:
        return x
    else:
        return y

for i, item in enumerate(char_list):
    if item != 0:
        x = rScan(i)
        y = lScan(i)
        char_list[i] = compare(x, y)

print(" ".join(str(i) for i in char_list))