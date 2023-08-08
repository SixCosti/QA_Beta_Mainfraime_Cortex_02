#1000 = 100 * (1+(10/100))

#investment = 100
#target = 1000
years = 0
#interest = 10

print(">>> Piggy bank! ")
investment = int(input("Investment: "))
target = int(input("Target: "))
interest = int(input("Interest: "))

while investment < target:
    investment *= (1 + (interest / 100))
    years += 1
    
print("It will take {} years for the investment to grow to {} pounds.".format(years, target))
