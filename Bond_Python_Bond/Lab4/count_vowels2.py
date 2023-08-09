

words = input("Chose your destiny: ")
vowels = ["a","e","i","o","u"]

counts = 0

for word in words.split():
    if any(vowel in word for vowel in vowels) :
        counts += 1
    else:
        print("No vowels found in {}".format(word))

print("Number of words with vowels:", counts)


#NEEDS TESTING