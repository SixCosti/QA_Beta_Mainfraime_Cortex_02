

allowance = 11850
poor_class = 34500
poor_class_tax = 20/100
middle_class = range(34501, 150000)
middle_class_tax = 40/100
rich = (150000 + 1)
rich_tax = 45/100




def getIncomeTax(salary):
    #if after_tax in salary:#
    if True:
        salary = int(input("Type your yearly income: "))
        if salary in range(0, 34500):
            after_tax == (salary - 11850)/20
            print(after_tax)
            return after_tax
        elif salary in range(34501 - 150000):
            after_tax = (salary - 11850)/40
            return after_tax
        elif salary >= 150000:
            after_tax = (salary - 11850)/45
            return after_tax
        else:
            return None
    else:
        print("Nope")



wage = 150000
getIncomeTax(wage)