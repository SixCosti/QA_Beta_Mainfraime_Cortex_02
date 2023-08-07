def person_equal():

    age = int(input("Greetings and Salutations! \nYour age is required to see wher in the Dungeon category you would fit in! \nPlease do enter your age: "))

    if age >= 18:
        print("You are in category A.")
    elif age >= 16:
        print("You are in category B.")
    else:
        print("You are in category C.")


person_equal()