import time

inventory = []
MAX_INVENTORY_SIZE = 5
flashlight_working = False
game_over = False
current_room = 1

items_in_room_1 = [
    {"name": "flashlight", "type": "tool", "description": "A flashlight, a little rusty but could still work."},
    {"name": "note","type": "clue","description": "A torn note that says: 'Leave before they test...'"},
    {"name": "key", "type": "tool", "description": "A rusty key."},
    {"name": "apple", "type": "food", "description": "A green apple."},
    {"name": "batteries", "type": "tool", "description": "2 batteries. They're still in good condition"}
    ]

items_in_room_2 = [
    {"name": "report", "type": "clue", "description": "Official employee report. This is an official report signed by Ash Thumber stating that the building has been exposed to a chemical leak"}
]


def show_inventory():
    if len(inventory) == 0:
        print("Your inventory is empty.")
    else:
        print("Inventory:")
        for item in inventory:
            print("-", item["name"])

def show_room_items():
    if current_room == 1:
        print("Items in the room:")
        for item in items_in_room_1:
            print("-", item["name"])

    elif current_room == 2:
        print("Items in the office:")
        for item in items_in_room_2:
            print("-", item["name"])

def pick_up(item_name):
    if len(inventory) >= MAX_INVENTORY_SIZE:
        print("Your inventory is full.")
        return

    if current_room == 1:
        room = items_in_room_1

    else:
        room = items_in_room_2

    for item in room:

        if item["name"] == item_name:

            inventory.append(item)
            room.remove(item)

            print("You picked up the", item_name)

def drop(item_name):
    for item in inventory:
        if item["name"] == item_name:
            inventory.remove(item)
            items_in_room_1.append(item)
            print(f"You dropped the {item_name}.")
            return    
    print("You do not have that item.")

def use(item_name):

    global game_over
    global flashlight_working

    for item in inventory:

        if item["name"] == item_name:

            if item["type"] == "food":
                print("You eat the apple.")
                time.sleep(1.5)
                print("You start to feel sick.")
                time.sleep(1.5)
                print("You realise you probably shouldn't have eaten an apple you found in an abandoned building.")
                time.sleep(1.5)
                print("The apple had absorbed chemicals.")
                time.sleep(2)
                print("You died.")
                time.sleep(1.5)
                print("Game over. Try again")
                game_over = True


                inventory.remove(item)

            elif item["name"] == "batteries":
                has_flashlight = False
                for inv_item in inventory:
                    if inv_item["name"] == "flashlight":
                        has_flashlight = True

                if has_flashlight:
                    flashlight_working = True
                    print("You put the batteries in the flashlight.")
                else:
                    print("You need something to use them with.")

            elif item["name"] == "flashlight":
                if flashlight_working == True:
                    print("You shine the flashlight around the dark hallway.")
                else:
                    print("hm, no batteries")

            elif item["name"] == "key":
                global current_room
                if current_room == 1:
                    print("You unlock the office door.")
                    print("You enter a hidden room.")
                    current_room = 2
                else:
                    print("The door is already unlocked.")

            elif item["type"] == "clue":
                print("You read the clue carefully.")

            else:
                print("You can't use that right now.")

            return

    print("You don't have that item.")


def examine(item_name):
    global game_over

    for item in inventory:
        if item["name"] == item_name:
            print(item["description"])
            if item_name == "report":
                print("You solved the mystery!")
                game_over = True
            return

    for item in items_in_room_1:
        if item["name"] == item_name:
            print(item["description"])
            return
        
    for item in items_in_room_2:
        if item["name"] == item_name:
            print(item["description"])
            if item_name == "report":
                print("The building was abandoned after a chemical leak.")
                print("You solved the mystery!")
                game_over = True
            return

    print("That item does not exist.")



def game_loop():

    global game_over

    print("================================")
    print(" ABANDONED BUILDING MYSTERY ")
    print("================================")
    time.sleep(1.3)
    print("You're investigating an abandoned building.")
    time.sleep(1.3)
    print("Try to find clues about why everyone seems to have left in a hurry")
    time.sleep(1.3)
    print("Type 'help' to see commands.")

    while game_over == False:


        command = input("\n> ").lower()

        match command.split():

            case ["help"]:
                print("\nCommands:")
                print("inventory")
                print("look")
                print("pickup [item name]")
                print("drop [item name]")
                print("use [item name]")
                print("examine [item name]")
                print("quit")

            case ["inventory"]:
                show_inventory()

            case ["look"]:
                show_room_items()

            case ["pickup", item_name]:
                pick_up(item_name)

            case ["drop", item_name]:
                drop(item_name)

            case ["use", item_name]:
                use(item_name)

            case ["examine", item_name]:
                examine(item_name)

            case ["quit"]:
                print("You leave the building.")
                break

            case _:
                print("Unknown command.")
        
    print("Congratulations! You escaped with the truth.")



if __name__ == "__main__":
    game_loop()
