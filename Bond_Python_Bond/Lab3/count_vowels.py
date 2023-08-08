word = input("Magic word: ")
vowels = 0

word_length = len(word)

index = 0

while index < word_length:
    char = word[index]
    
    if char.lower() in 'aeiou':
        vowel_count += 1
    
    index += 1

print("The word {} has {} vowels.".format(word, vowels)


      #NOT WORKING