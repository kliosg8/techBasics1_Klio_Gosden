import time

scores = {
    "Gryffindor": 0,
    "Ravenclaw": 0,
    "Hufflepuff": 0,
    "Slytherin": 0
}

greeting_message = "Welcome to Hogwarts, what's your name?"
sorting_message = "Let's sort you into your house!"
invalid_input = "Wrong input! Try again!"
age_prompt = "Please enter your age: "
age_range_error = "That doesn't look like a realistic age, try again"
age_young_but_okay = "You're way too young to be able to play this, but this is Hogwarts so why not, let's sort you into your house!"


def add_points(house, points):
    scores[house] += points
    return scores[house]

def main():  
    name = input(greeting_message + "\nEnter name: ")
    print(f"Hello, {name}!")
    time.sleep(1)  
    while True:
        try:
            age = int(input(age_prompt))
            if age <= 100 and age >= 5:
                print(sorting_message)
                break
            elif age <= 4 and age >= 1:
                print(age_young_but_okay)
                break
            else:
                print(age_range_error, name, "try again")
        except ValueError:
            print("Please enter a valid number.")
    time.sleep(1)
   
    print("\nDo you like dawn or dusk?")
    print("1) Dawn")
    print("2) Dusk")
    while True:
        answer = input("Answer: ").lower()
        if answer in ["1", "dawn"]:
            add_points("Gryffindor", 1)
            add_points("Ravenclaw", 1)
            print("\nI have some beautiful memories at dawn... good days")
            break
        elif answer in ["2", "dusk"]:
            add_points("Hufflepuff", 1)
            add_points("Slytherin", 1)
            print("\n*Sorting hat*: How many photos do you have of a sunset?")
            break
        else:
            print(invalid_input)

    time.sleep(2)

   
    print("\nWhen I'm dead, I want people to remember me as:")
    print("1) The good")
    print("2) The great")
    print("3) The wise")
    print("4) The bold")
    while True:
        answer = input("Answer: ").lower()
        if answer in ["1", "the good", "good"]:
            add_points("Hufflepuff", 2)
            print("\nI can already sense the people pleaser in you")
            break
        elif answer in ["2", "the great", "great"]:
            add_points("Slytherin", 2)
            print("\nCocky are we?")
            break
        elif answer in ["3", "the wise", "wise"]:
            add_points("Ravenclaw", 2)
            print("\nNobody is wise these days")
            break
        elif answer in ["4", "the bold", "bold"]:
            add_points("Gryffindor", 2)
            print("\nTypical")
            break
        else:
            print(invalid_input)

    time.sleep(2)

    
    print("\nWhat animal best represents you?")
    print("1) Owl")
    print("2) Snake")
    print("3) Fox")
    print("4) Cat")
    while True:
        answer = input("Answer: ").lower()
        if answer in ["1", "owl"]:
            add_points("Gryffindor", 3)
            print(f"\nYou think you're mysterious huh, {name}?")
            break
        elif answer in ["2", "snake"]:
            add_points("Slytherin", 3)
            print("\nWho hurt you?")
            break
        elif answer in ["3", "fox"]:
            add_points("Ravenclaw", 3)
            print("\nWe should keep an eye on you")
            break
        elif answer in ["4", "cat"]:
            add_points("Hufflepuff", 3)
            print("\nPeople who chose cat tend to get bullied, I don't know why... watch out")
            break
        else:
            print(invalid_input)

    time.sleep(2)


    print("\nAndroid or iOS?")
    print("1) Android")
    print("2) iOS")
    while True:
        answer = input("Answer: ").lower()
        if answer in ["1", "android"]:
            add_points("Hufflepuff", 2)
            add_points("Ravenclaw", 2)
            print("\nThat is the only right answer")
            break
        elif answer in ["2", "ios"]:
            add_points("Gryffindor", 2)
            add_points("Slytherin", 2)
            print("\nHow do you feel about choosing the wrong answer?")
            break
        else:
            print(invalid_input)

 
    time.sleep(0.8)
    input("\nPress enter to see your house")
    time.sleep(0.5)

    top_house = max(scores, key=scores.get)
    print(f"""
     -._.-._.-._.-._.-._.-._.-._.-
      you are in house {top_house}!
     _.-._.-._.-._.-._.-._.-._.-._""")

    time.sleep(0.8)
    input("\nPress enter to see the scoreboard:")
    time.sleep(0.5)

    print("\nScoreboard")
    for house, score in scores.items():
        print(f"{house}: {score}")


if __name__ == "__main__":
    main()
