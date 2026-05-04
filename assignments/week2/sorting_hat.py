
import time

scores = {
"Gryffindor": 0,
"Ravenclaw": 0,
"Hufflepuff": 0,
"Slytherin": 0
}

name = input("Welcome to Hogwarts, what's you name? \nEnter name: ")
print("Hello", name, "!")

time.sleep(1)

while True:
    age = int(input("Please enter your age: "))

    if age <= 100 and age >= 5:
        time.sleep(0.5)
        print("Lets sort you into your house!")
        break

    elif age <=4 and age >= 1:
        time.sleep(0.5)
        print("You're way to young to be able to play this, but this is Hogwarts so why not, lets's sort you into your house!")
        break

    else:
        time.sleep(0.5)
        print("That doesn't look like a realistic age,", name, "try again")

time.sleep(1)


print("\nDo you like dawn or dusk?")
while True:
    answer = input("Answer: ")

    if answer == "1" or answer.lower() == "dawn":
        scores["Gryffindor"] += 1
        scores["Ravenclaw"] += 1
        time.sleep(1)
        print("\nI have some beautiful memories at dawn...good days")
        break

    elif answer == "2" or answer.lower() == "dusk":
        scores["Hufflepuff"] += 1
        scores["Slytherin"] += 1
        time.sleep(1)
        print("\n*Sorting hat*: How many photos do you have of a sunset?")
        break

    else:
        print("Wrong input! Try again!")


time.sleep(2)

print("\nWhen im dead, i want people to remember me as: ")
print("1) The good")
print("2) The great")
print("3) The wise")
print("4) The bold")
while True:
    answer = input("Answer: ")

    if answer == "1" or answer.lower() == "the good" or answer.lower() == "good":
        scores["Hufflepuff"] += 2
        time.sleep(1)
        print("\nI can already sense the people pleaser in you")
        break

    elif answer == "2" or answer.lower() == "the great" or answer.lower() == "great":
        scores["Slytherin"] += 2
        time.sleep(1)
        print("\nCocky are we?")
        break

    elif answer == "3" or answer.lower() == "the wise" or answer.lower() == "wise":
        scores["Ravenclaw"] += 2
        time.sleep(1)
        print("\nNobody is wise these days")
        break

    elif answer == "4" or answer.lower() == "the bold" or answer.lower() == "bold":
        scores["Gryffindor"] += 2
        time.sleep(1)
        print("\nTypical")
        break

    else:
        print("Wrong input! Try again")

time.sleep(2)

print("\nWhat kind of instrument most pleases your ear?")
print("1) Violin")
print("2) Trumpet")
print("3) Piano")
print("4) Drums")
while True:
    answer = input("Answer: ")

    if answer == "1" or answer.lower() == "violin":
        scores["Slytherin"] += 4
        time.sleep(1)
        print("\nViolin sounds good only when you play it ;)")
        break

    elif answer == "2" or answer.lower() == "trumpet":
        scores["Hufflepuff"] += 4
        time.sleep(1)
        print("\nNobody chooses that one")
        break

    elif answer == "3" or answer.lower() == "piano":
        scores["Ravenclaw"] += 4
        time.sleep(1)
        print("\nYou must be a ravenclaw...or maybe not, who knows? Not me")
        break

    elif answer == "4" or answer.lower() == "drums":
        scores["Gryffindor"] += 4
        time.sleep(1)
        print("\nI was contemplating even putting that on the list")
        break

    else:
        print("Wrong input! Try again!")

time.sleep(2)

print("\nWhat animal best represents you?")
print("1) Owl")
print("2) Snake")
print("3) Fox")
print("4) Cat")
while True:
    answer = input("Answer: ")

    if answer == "1" or answer.lower() == "owl":
        scores["Gryffindor"] += 3
        time.sleep(1)
        print("\nYou think you're mysterious huh", name, "?")
        break

    elif answer == "2" or answer.lower() == "snake":
        scores["Slytherin"] += 3
        time.sleep(1)
        print("\nWho hurt you?")
        break

    elif answer == "3" or answer.lower() == "fox":
        scores["Ravenclaw"] += 3
        time.sleep(1)
        print("\nWe should keep an eye on you")
        break

    elif answer == "4" or answer.lower() == "cat":
        scores["Hufflepuff"] += 3
        time.sleep(1)
        print("\nPeople who chose cat tend to get bullied, i don't know why...watch out")
        break

    else:
        print("Wrong input! Try again!")

time.sleep(2)

print("\nPick your drink")
print("1) Energy drink")
print("2) Hot chocolate")
print("3) Coffee")
print("4) Tea")
while True:
    answer = input("Answer: ")

    if answer == "1" or answer.lower() == "energy drink":
        scores["Slytherin"] += 6
        time.sleep(1)
        print(
            "\nAre you sick of coffee drinkers warning you about your heart all the time?")
        break

    elif answer == "2" or answer.lower() == "hot chocolate":
        scores["Hufflepuff"] += 6
        time.sleep(1)
        print("\nCan i offer some stormy day and under the covers with that?")
        break

    elif answer == "3" or answer.lower() == "coffee":
        scores["Ravenclaw"] += 6
        time.sleep(1)
        print("\nAre you proud?")
        break

    elif answer == "4" or answer.lower() == "tea":
        scores["Gryffindor"] += 6
        time.sleep(1)
        print("\nWith or without milk?")
        break

    else:
        print("Wrong input! Try again!")

time.sleep(2)

print("\nAndroid or iOS?")

while True:
    answer = input("Answer: ")

    if answer == "1" or answer.lower() == "android":
        scores["Hufflepuff"] += 2
        scores["Ravenclaw"] += 2
        time.sleep(1)
        print("\nThat is the only right answer")
        break

    elif answer == "2" or answer.lower() == "ios":
        scores["Gryffindor"] += 2
        scores["Slytherin"] += 2
        time.sleep(1)
        print("\nHow do you feel about choosing the wrong answer?")
        break

    else:
        print("Wrong input! Try again!")

top_group = max(scores, key=scores.get)

time.sleep(0.8)
input("\nPress enter to see your house")
time.sleep(0.5)

print(
      """
       -._.-._.-._.-._.-._.-._.-._.-
        you are in house""", top_group, """!
       _.-._.-._.-._.-._.-._.-._.-._""")

time.sleep(0.8)

input("\nPress enter to see the scoreboard:")
time.sleep(0.5)

print("\nScoreboard")
print("Gryffindor: ", + scores["Gryffindor"])
print("Ravenclaw: ", + scores["Ravenclaw"])
print("Hufflepuff: ", + scores["Hufflepuff"])
print("Slytherin: ", + scores["Slytherin"])


