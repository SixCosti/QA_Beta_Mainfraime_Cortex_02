min = 1
max = 100
attempts = 3


while attempts > 0:
    num = int(input("Guess my number: "))

    if min <= num <= max:
        print("You've chosen wisely...{}".format(num))
        break
    else:
        attempts -= 1
        print("Number out of range! Attempts: {}".format(attempts))
        #continue

if attempts == 0:
    print(None)