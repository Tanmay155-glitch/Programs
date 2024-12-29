def adventure_game():
    print("You find yourself in a forest.")
    print("1. Go north")
    print("2. Go south")
    print("3. Go east")
    print("4. Go west")

    choice = input("What do you want to do? (1/2/3/4): ")

    if choice == '1':
        print("You go north and find a treasure chest!")
    elif choice == '2':
        print("You go south and encounter a wild animal.")
    elif choice == '3':
        print("You go east and discover a beautiful river.")
    elif choice == '4':
        print("You go west and find a path leading out of the forest.")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    adventure_game()
