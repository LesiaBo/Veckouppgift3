#Version1: Gör ett program som upprepade gånger ber användaren skriva in ett tal.
# När man skriver in strängen "quit" eller "avsluta" ska programmet ska det räkna ut summan av talen.
# Exempel:
#Välkommen till Kvittokompis! Avsluta genom att skriva: quit
#Skriv in ett belopp: 25
#Skriv in ett belopp: 50
#Skriv in ett belopp: quit
#Det blir 75 kr totalt. Välkommen åter!
amount = 0
input_from_user = ""
print("Välkommen till Kvittokompis! Avsluta genom att skriva: quit")
while input_from_user != "quit" and input_from_user != "avsluta":
    input_from_user = input("Skriv in ett belopp:")
    if input_from_user.isdigit():
        current_amount = int(input_from_user)
        amount += current_amount
print(f"Det blir {amount} kr totalt. Välkommen åter!")
#Test cases:
#100 -> 100 -> passed
#10, 20, 15 -> 45 -> passed
#=======================================================================================

#Version 2: programmet ska fråga hur många man är, och tala om hur mycket varje person i sällskapet ska betala.
#Hur många är ni? 3
#Det blir 75 kr totalt, alltså 25.0 kr per person. Välkommen åter!
total_amount = 0
dish_price = 0
number_of_customers = int(input("Hur många är ni? "))
print("Välkommen till vår restaurang! Skriv 'nej' om ni är klara med dina val")
while dish_price != "nej":
    dish_price = input("Skriv rättens pris:")
    try:
        dish_price = int(dish_price)
        total_amount += number_of_customers*dish_price
    except ValueError:
        print("Nu ska vi räkna...")
print(f"Det blir {total_amount} kr totalt, alltså {float(total_amount/number_of_customers)} kr per person. Välkommen åter!")

#Test cases:
#100, 1 person -> 100.0 -> passed
#100, 2 personer -> 200.0 -> passed
#10, 10, 40 personer -> 800 -> passed
#30, 20, 30, 1 person -> 80 -> passed
#=======================================================================================


#Version 3: programmet ska fråga hur många procent dricks man vill lägga på.
# Om användaren inte skriver något (tom sträng) ska programmet
# använda 10% som standardinställning.
tip = 10
to_pay = int(input("Hur mycket kostar din beställning? "))
error = ""
users_input = input("Hur många procent dricks vill du lägga på? ")
if users_input == "":
    print(f"Det blir en default dricks på {tip}%")
else:
    try:
        tip = int(users_input)
    except ValueError:
        error = "stop"
        print("Försök att ge nummer för dricks eller lämna det tomt för standardinställning ")
if error != "stop":
    print(f"Det blir {to_pay * (100 + tip) / 100} kr totalt, inclusive dricks {to_pay * tip/ 100}. Välkommen åter!")
#Test cases:
#1000, 20% -> 1200, 200 -> passed
#400, "" -> 440, 40-> passed