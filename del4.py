#Skriv in följande kod och modifiera den, så att den skriver ut figurerna a-j en i taget.
#a:
print("Version a: ")
for i in range(6):
    print("#.......")

#b:
print("Version b: ")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == y:
            s += "#"
        else:
            s += "."
    print(s)

#c:
print("Version c: ")
for i in range(6):
    print("..###...")

#d:
print("Version d: ")
for i in range(6):
    if i == 2:
        print("########")
    else:
        print("..##.....")

#e:
print("Version e: ")
string_original = "....#..."
for x in range(0, 6):
    str_p1 = string_original[:(5 - x)] + "#"
    str_p2 = string_original[(6 - x):]
    print(str_p1 + str_p2)

#f:
print("Version f: ")
for cur in range(0, 6):
    str = ""
    for x in range(0, 7):
        if x == cur or cur == 5-x:
            str += "#"
        else:
            str += "."
    print(str+".")

#g:
print("Version g: ")
for cur in range(0, 6):
    str = ""
    for x in range(0, 7):
        if x %2 == 0:
            str += "#"
        else:
            str += "."
    print(str+".")



#j:
print("Version j: ")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x%3 == y%3:
            s += "."
        elif x%3 == (y + 1)%3:
            s += "#"
        else:
            s += "O"
    print(s)

