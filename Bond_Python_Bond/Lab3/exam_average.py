

#mark1 = int(input("English: "))
#mark2 = int(input("Math: "))
#mark3 = int(input("ICT: "))

#average_mark = (mark1 + mark2 + mark3)

#if average_mark >= 65:
 #   print("Pass")
#elif average_mark < 65:
    #print("Fail!")
    #for mark in mark1, mark2, mark3:
        #if mark < 0 or mark > 100 :
 
        
marks = []

for subject in ["English", "Math", "ICT"]:
    valid_mark = False
    
    while not valid_mark:
        mark = int(input("Enter {subject} exam mark (0-100): "))
        if 0 <= mark <= 100:
            valid_mark = True
            marks.append(mark)
        else:
            print("Invalid mark. Please enter a mark between 0 and 100.")

average_mark = sum(marks) / len(marks)

print(f"Average mark: {average_mark:.2f}")

if average_mark >= 65:
    print("Result: Pass")
else:
    print("Result: Fail")