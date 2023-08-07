def exam_grades():
	grade = int(input("Your Grade: "))


	if (grade < 1) or (grade > 100):
		print("You grade value must be between the offical markdown: 1-100!!!")
	else:
		if grade < 50:
			print("Fail!")
		elif grade >= 50 and grade <= 60:
				print("Pass!")
		elif grade <= 70 and grade >= 61:
			print("Merit!")
		# elif grade >= 71 and grade <= 100:
		else:
			print("Distiction!")
		
			# print("This will never happen.")

		 
exam_grades()