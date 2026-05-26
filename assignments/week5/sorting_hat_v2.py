import time
from colorama import Fore, Style, init
init(autoreset=True)

house_colors = {
    "Gryffindor": Fore.RED,
    "Ravenclaw": Fore.MAGENTA,
    "Hufflepuff": Fore.YELLOW,
    "Slytherin": Fore.GREEN
}

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

short_delay = 0.5
medium_delay = 1
long_delay = 2

min_age = 1
young_age = 4
max_age = 100

def add_points(house, points):
    scores[house] += points


def get_name_age():
    global name
    name = input(greeting_message + "\nEnter name: ")
    print(f"Hello, {name}!")
    time.sleep(medium_delay)  
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
    time.sleep(medium_delay)
    
def question_dawn_dusk():
    print("\nDo you like dawn or dusk?")
    print("1) Dawn")
    print("2) Dusk")
    while True:
        answer = input("Answer: ").lower()
        if answer in ["1", "dawn"]:
            add_points("Gryffindor", 1)
            add_points("Ravenclaw", 1)
            print(Fore.MAGENTA + Style.DIM + "\n*Sorting hat*: I have some beautiful memories at dawn... good days")
            break
        elif answer in ["2", "dusk"]:
            add_points("Hufflepuff", 1)
            add_points("Slytherin", 1)
            print(Fore.MAGENTA + Style.DIM + "\n*Sorting hat*: How many photos do you have of a sunset?")
            break
        else:
            print(Fore.RED + invalid_input)

    time.sleep(long_delay)

def question_memory():
    print("\nWhen I'm dead, I want people to remember me as:")
    print("1) The good")
    print("2) The great")
    print("3) The wise")
    print("4) The bold")
    while True:
        answer = input("Answer: ").lower()
        if answer in ["1", "the good", "good"]:
            add_points("Hufflepuff", 2)
            print(Fore.MAGENTA + Style.DIM + "\nI can already sense the people pleaser in you")
            break
        elif answer in ["2", "the great", "great"]:
            add_points("Slytherin", 2)
            print(Fore.MAGENTA + Style.DIM + "\nCocky are we?")
            break
        elif answer in ["3", "the wise", "wise"]:
            add_points("Ravenclaw", 2)
            print(Fore.MAGENTA + Style.DIM + "\nNobody is wise these days")
            break
        elif answer in ["4", "the bold", "bold"]:
            add_points("Gryffindor", 2)
            print(Fore.MAGENTA + Style.DIM + "\nTypical")
            break
        else:
            print(Fore.RED +invalid_input)

    time.sleep(long_delay)

def question_animal(name):
    print("\nWhat animal best represents you?")
    print("1) Owl")
    print("2) Snake")
    print("3) Fox")
    print("4) Cat")
    while True:
        answer = input("Answer: ").lower()
        if answer in ["1", "owl"]:
            add_points("Gryffindor", 3)
            print(Fore.MAGENTA + Style.DIM + f"\nYou think you're mysterious huh, {name}?")
            break
        elif answer in ["2", "snake"]:
            add_points("Slytherin", 3)
            print(Fore.MAGENTA + Style.DIM + "\nWho hurt you?")
            break
        elif answer in ["3", "fox"]:
            add_points("Ravenclaw", 3)
            print(Fore.MAGENTA + Style.DIM + "\nWe should keep an eye on you")
            break
        elif answer in ["4", "cat"]:
            add_points("Hufflepuff", 3)
            print(Fore.MAGENTA + Style.DIM + "\nPeople who chose cat tend to get bullied, I don't know why... watch out")
            break
        else:
            print(Fore.RED +invalid_input)

    time.sleep(long_delay)

def question_phone():
    print("\nAndroid or iOS?")
    print("1) Android")
    print("2) iOS")
    while True:
        answer = input("Answer: ").lower()
        if answer in ["1", "android"]:
            add_points("Hufflepuff", 2)
            add_points("Ravenclaw", 2)
            print(Fore.MAGENTA + Style.DIM + "\nThat is the only right answer")
            break
        elif answer in ["2", "ios"]:
            add_points("Gryffindor", 2)
            add_points("Slytherin", 2)
            print(Fore.MAGENTA + Style.DIM + "\nHow do you feel about choosing the wrong answer?")
            break
        else:
            print(Fore.RED + invalid_input)

def show_results():
    time.sleep(short_delay)
    input("\nPress enter to see your house")
    time.sleep(short_delay)

    top_house = max(scores, key=scores.get)
    color = house_colors[top_house]

    print(color + Style.BRIGHT + f"""
    -._.-._.-._.-._.-._.-._.-._.-
    You're in house {top_house}!
    _.-._.-._.-._.-._.-._.-._.-._""")

    time.sleep(medium_delay)
    input("\nPress enter to see the scoreboard:")
    time.sleep(medium_delay)

    print(Fore.BLUE + Style.BRIGHT + "\nScoreboard")
    for house, score in scores.items():
        print(f"{house}: {score}")


def main():
    get_name_age()
    question_dawn_dusk()
    question_memory()
    question_animal(name)
    question_phone()

    show_results()

if __name__ == "__main__":
    main()
