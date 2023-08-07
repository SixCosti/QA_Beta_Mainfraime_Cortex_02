

from ast import Continue, Return
from pdb import Restart


def calculator():
    first_numba = int(input("First Number: "))
    second_numba = int(input("Second Number: "))
    if type(first_numba) != int and type(second_numba) != int:
        print("Please type in an actual number!")
        Restart
    else:
        Continue
    greet = int(input("I'm Calculatron! -_-\nGeometry and algebra... Geometry and algeb... bip bup bap -robot noises-\n Choose your destiny!\n 1.) Addition\n 2.) Substraction\n 3.) Multiply\n 4.) Division\n 5.) Square\n"))

    if greet == 1:
        print(first_numba + second_numba)
    elif greet == 2:
        print(first_numba - second_numba)
    elif greet == 3:
        print(first_numba * second_numba)
    elif greet == 4:
        print(first_numba / second_numba)
    elif greet == 5:
        print(first_numba ** second_numba)
    else:
        print("Please choose 1 or 2 or 3 or 4 or 5!")
        Return


calculator()
