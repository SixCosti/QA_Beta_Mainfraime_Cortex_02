

allowance = 11850
working_class = 34500
working_class_tax = 20/100
middle_class = range(34501, 150000)
middle_class_tax = 40/100
rich = (150000 + 1)
rich_tax = 45/100




def getIncomeTax(salary):
    if salary <= working_class:

        after_tax = (salary - allowance) * working_class_tax
        return after_tax
    elif salary in middle_class:
        after_tax = (salary - allowance) * middle_class_tax
        return after_tax
    elif salary >= rich:
        after_tax = (salary - allowance) * rich_tax
        return after_tax
    else:
        return None
   

wage = int(input("Type your yearly income: "))
income_tax = getIncomeTax(wage)

while True:
    if income_tax is not None:
        print("Here is your wage after tax: {}".format(income_tax))
    else:
        print("Wage out of range!")
    break