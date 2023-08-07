def graduation():
    level = int(input("Graduation Level: "))
    mark = int(input("Enter your grade: "))

    if mark < 1 or mark > 100:
        print("Please enter a valid grade! Official range is 1 - 100!")
    elif level < 1 or level > 2:
        print("Type a valid level! The official levels are 1 or 2.")
    else:
        if level == 1:
            if mark < 50:
                print("Fail!")
            elif 50 <= mark <= 60:
                print("Pass!")
            elif 61 <= mark <= 70:
                print("Merit!")
            else:
                print("Distinction!")
        elif level == 2:
            if mark < 40:
                print("Fail!")
            elif 40 <= mark <= 50:
                print("Pass!")
            elif 51 <= mark <= 65:
                print("Merit!")
            else:
                print("Distinction!")
        else:
            print("Type a valid level! The official levels are 1 or 2.")

graduation()
