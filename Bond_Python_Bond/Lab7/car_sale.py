
carSale = open("/Users/Admin/Source/Repos/QA_Beta_Mainfraime_Cortex_02/Bond_Python_Bond/Lab7/carSale.csv")

carSale_r = carSale.read()
my_list = carSale_r.split("\n")
print(my_list)
car_list = []

with open("/Users/Admin/Source/Repos/QA_Beta_Mainfraime_Cortex_02/Bond_Python_Bond/Lab7/carSale.csv", "r") as file:
    lines = file.readlines()
    #file_list = lines.split(",")
    for line in lines:
        car_list.append(line)

print(car_list)


#WORK I  PROGRESS... :(







#with open("/Users/Admin/Source/Repos/QA_Beta_Mainfraime_Cortex_02/Bond_Python_Bond/Lab7/carSale.csv", "r") as file:
 #   lines = file.readlines()
   
 #   for line in lines:
 #       data = [line.strip().split(',')]

 #   monthly_sum = []
 #   for index in range(1, len(data[0])):
 #       total = 0
 #       for row in data[1:]:
 #           total += int(row[index])
 #   monthly_sum.append(total)

 #   manufacturers = [row[0] for row in data[1:]]
 #   yearly_sales = []
 #   for row in data[1:]:
 #       total = sum(map(int, row[1:]))
 #       yearly_sales.append(total)


 #   print("Sum of cars sold in each month:", monthly_sum)
 #   print("Total yearly sales by each manufacturer:")
 #   for index, manufacturer in enumerate(manufacturers):
 #       print("{}: {}".format(manufacturer, yearly_sales[index] ))
