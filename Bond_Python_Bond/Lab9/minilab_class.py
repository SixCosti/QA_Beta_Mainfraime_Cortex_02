


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
        after_withdrawal = self.funds - withdrawal
        return after_withdrawal
    
    def deposit(self, depositing):
        self.deposited = depositing
        after_deposited = self.funds + depositing
        return after_deposited

clothing = Budget(200)
food = Budget(6)
entertaiment = Budget(50)

print("Clothing funds after withdrawal : ",clothing.withdraw(20))
print("Food funds after deposit : ",food.deposit(104))
print("Entertaiment funds after deposit: ",entertaiment.deposit(2500))
