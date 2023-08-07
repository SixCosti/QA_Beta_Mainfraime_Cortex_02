def pita():
    
    pit = int(input(("Pythagoras Calculator \n1. Find the length of A given B and C \n2. Find the length of B given A and C \n3. Find the length of C given A and B \n")))

   # a = int(input("lenght of side A: "))
   # b = int(input("lenght of side B: "))
   # c = int(input("lenght of side C: "))

    if pit < 1 or pit > 3:
        print("The options are on screen, 1, 2 or 3!")
    else:
        if pit == 1:
            b = int(input("lenght of side B: "))
            c = int(input("lenght of side C: "))
            print("Side A: ", (b**2)+(c**2))
        elif pit == 2:
            a = int(input("lenght of side A: "))
            c = int(input("lenght of side C: "))
            print("Side B:", (a**2)+(c**2))
        if pit == 3:
            a = int(input("lenght of side A: "))
            b = int(input("lenght of side B: "))
            print("Side C: ", (b**2)+(a**2))
        else:
            print("Wazzzzaaa")

pita()



