#Goal: “Create a Budget class that can instantiate objects based on different budget categories:
# like food, clothing, and entertainment. 
# These objects should allow for depositing and withdrawing funds from each category, 
# as well computing category balances and transferring balance amounts between categories”

#class Budget:
#    pass

#clothing = Budget()
#entertainment = Budget()

#clothing.withdraw(20)
#entertainment.deposit(5)

class Budget:

    #def __init__(self, foodvar, clothingvar, entertaimentvar)
    def __init__(self, fundsvar):
        self.funds = fundsvar
        #self.food = foodvar
        #self.clothing = clothingvar
        #self.entertaiment = entertaimentvar
        #return(self.food, self.clothing, self.entertaiment)

    def withdraw(self, withdrawal):
        self.withdrawing = withdrawal
        after_withdrawal = self.funds - after_withdrawing
        return after_withdrawal
    
    def deposit(self, depositing):
        self.deposited = depositing
        after_deposited = self.funds + deposited
        return after_deposited

clothing = Budget(200)
food = Budget(6)
entertaiment = Budget(50)

print(clothing.withdraw(20))
