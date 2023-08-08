ages = [12,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,11,7,9,64,78,37,3,8,68,22,4,60,33,82,45,23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,35,72,25,63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]

length = len(ages)
print("Length of ages list: {}".format(length))
reserved = 0

for age in ages:
    #print(age)
    #print(age+1)
    ages[reserved] = age + 1
    reserved = reserved + 1 
    
    if age >= 65:
        del(age)
    elif age <= 16 or age >= 25:
            print(ages.count(25))
    else:
        print(ages)
        continue
        


print("Ages:")
for age in ages:
    print(age)

print("Ages after adding one year:")
for i in range(len(ages)):
    ages[i] += 1
    print(ages[i])

ages = [age for age in ages if 16 <= age <= 65]
print("Ages after removing outside range:", ages)

count_16_to_25 = len([age for age in ages if 16 <= age <= 25])
print(f"Count of 16-25 year olds: {count_16_to_25}")