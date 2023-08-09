import statistics

data = "100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"

#grades = data.split(",")
grades = [int(grade) for grade in data.split(',')]

total_sum = sum(grades)
total_num = len(grades)
average_sum = total_sum / total_num


#for grade in grades:
mini = min(grades)
maxi = max(grades)
#print(mini, maxi, round(average_sum, 2))
meani = statistics.mean(grades)
mediani = statistics.median(grades)
average_sum_round = round(average_sum, 2)

print("The minimum grade in data is : {} \n The maximum grade in data is : {} \n The average grade is: {}\n The mean of the grades is : {:0.2f}\n The median of the grades is {}".format(mini, maxi, average_sum_round, meani, mediani)) 