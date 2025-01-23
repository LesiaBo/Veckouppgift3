#Öva på loopar och listor
#1a Skriv färdigt kodexemplet.
answer = 0
for i in range (11):
    answer += i
print("Summan av talen 1 till 10 är: " + str(answer))
# Svaret ska bli 55

#1b Räkna ut summan av alla tal mellan 1 och 100. (inklusive 1 och 100, rätt svar ska bli 5050)
answer = 0
for i in range (1, 101):
    answer += i
print("Summan av talen 1 till 100 är: " + str(answer))



#1c Skriv om 1b så att den använder en while-loop.
answer = 0
i = 1
while i <= 100:
    answer += i
    i += 1
print("Summan av talen 1 till 100 är: " + str(answer))

#2 Räkna ut summan av alla elementen i listan: [1, -2, 3, -2, 4, -3]
answer = 0
my_list = [1, -2, 3, -2, 4, -3]
length = len(my_list)
for i in range (length):
    answer += my_list[i]
print("Summan av alla element i listan är: " + str(answer))

#3a Skapa en lista med namnen på fyra filmer. Namnen ska vara strängar. Skriv ut hela listan 2med funktionen print.
best_swedish_films = ["Scener ur ett äktenskap", "Persona", "Det sjunde inseglet", "Smultronstället"]
print(best_swedish_films)

#3b Lägg till "Fellowship of the ring" sist i listan.
best_swedish_films.append("Fellowship of the ring")
print(best_swedish_films)

#3c Lägg till "The two towers" på första platsen i listan. (index noll)
best_swedish_films.insert(0,"The two towers")
print(best_swedish_films)

#3d Ta reda på vilken position (index) "Fellowship of the ring" har nu.
print(best_swedish_films.index("Fellowship of the ring")) #5

#3e Ta bort en annan av filmerna. Har Fellowship-filmen ändrat index?
best_swedish_films.pop(4)
print(best_swedish_films.index("Fellowship of the ring")) #4

#3f Ta reda på hur lång listan är. (len)
numbers_of_films = len(best_swedish_films)
print(numbers_of_films)

#3g Vänd listan baklänges.
best_swedish_films.reverse()
print(best_swedish_films)

#3h Sortera listan stigande i bokstavsordning.
best_swedish_films.sort()
print(best_swedish_films)
