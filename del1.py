#1 Vad skrivs ut?
limit = 15
index = 5
while index <= limit:
    print(index)
    index = index + 2
#5
#7
#9
#11
#13
#15

#2 Vad skrivs ut?
for i in range(10):
    if i == 5:
        print("")
    else:
        print(i)
    i = i + 1
#0
#1
#2
#3
#4
#
#6
#7
#8
#9

#3 Vad blir summan? Skriv ner din bästa gissning innan du kör koden.
counter = 0
for i in range(6):
    counter +=i
print(counter)
#15

#4 Vad skrivs ut?
#För att förstå koden kan du sätta ut brytpunkter och köra med debugging.
# Det kan också underlätta att skriva samtidigt med papper och penna.
x = 0
y = 1
while y < 10:
    if y % 2 == 0:
        x -=y
    else:
        x += y * y
    y +=1
print(x, y)

#x=0+1=1; y=2
#X=-1, y=3
#x=-1+3*3=8, y=4
#x=8-4=4, y=5
#x=4+5*5=29, y=6
#x=29-6=23,y=7
#x=23+7*7=72, y=8
#x=72-8=64,y=9
#x=64+9*9=145,y=10
#145, 10

#5 Vad skrivs ut?
#Kan du göra om koden så att den skriver ut "time" i stället?
message = "its_time_to_get_coding"
print(message[3:7])
#_tim
message = "its_time_to_get_coding"
print(message[4:8])
#time

#6 Vad skrivs ut?
#Kan du flytta linjen ett steg åt höger?
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == y:
            s += "#"
        else:
            s += "."
    print(s)
# x=1, y=1, s=#
# x=2, y=1, s=#.
# x=3, y=1, s=#..
# x=4, y=1, s=#...
# x=5, y=1, s=#....
# x=6, y=1, s=#.....
# x=7, y=1, s=#......
# x=8, y=1, s=#.......
# #.......
# x=1, y=2, s=.
# x=2, y=2, s=.#
# ...
# x=8, y=2, s=.#......
# .#.....
# ..#.....
# ...#....
# ....#...
# .....#..
# ......#.

