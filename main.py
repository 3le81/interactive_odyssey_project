# basic set up, with each character having a name, description and response

# class BaseCharacter():

#     def __init__(self, name, desc):
#         self.name = name
#         self.desc = desc
#         self.response = ""

#     def __str__(self):
#         return f"{self.name}\n{self.desc}"

# basic structure to implement:

import random


class Character:
    def __init__(self, name):
        self.name = name

    def interact(self, user_action):
        pass


class Hero(Character):
    def interact(self, user_action):
        if user_action == "ask":
            print(f"{self.name} shares a clue about the mystery.")
        elif user_action == "gift":
            print(f"{self.name} thanks you for the gift.")
        elif user_action == "trade":
            print(f"{self.name} trades an item that might be useful.")
        else:
            print(f"{self.name} looks confused by your action.")


class Villain(Character):
    def interact(self, user_action):
        if user_action == "ask":
            print(f"{self.name} laughs sinisterly and gives a cryptic hint.")
        elif user_action == "gift":
            print(f"{self.name} sneers at your gift, but allows you to pass.")
        elif user_action == "trade":
            print(f"{self.name} demands a high price for valuable information.")
        else:
            print(f"{self.name} seems uninterested in your action.")


def main_menu():
    print("Welcome to the Interactive Odyssey!")
    print("Choose your action:")
    print("1. Ask")
    print("2. Gift")
    print("3. Trade")
    print("4. Exit")


def main():
    hero = Hero("Hero")
    villain = Villain("Villain")

    gifts = ["map", "key", "amulet", "compass"]
    collected_gifts = []

    while True:
        main_menu()
        choice = input("Enter your action: ")

        if choice == "1":
            character = random.choice([hero, villain])
            user_action = "ask"
        elif choice == "2":
            character = random.choice([hero, villain])
            user_action = "gift"
            if len(gifts) > 0:
                gift = random.choice(gifts)
                collected_gifts.append(gift)
                gifts.remove(gift)
                print(f"You give a {gift} to {character.name}.")
            else:
                print("You have no more gifts to give.")
                continue
        elif choice == "3":
            character = random.choice([hero, villain])
            user_action = "trade"
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
            continue

        character.interact(user_action)

        if character == villain and "map" in collected_gifts and "key" in collected_gifts:
            print(
                "Congratulations! You have solved the mystery and defeated the Villain!")
            break


if __name__ == "__main__":
    main()
