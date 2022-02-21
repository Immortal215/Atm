class Atm(object): 
    def __init__(self,cardnum,pinnum):
        self.cardnum=cardnum
        self.pinnum=pinnum
  
Bank = Atm("3204","32142341")
print("Pin Number =",Bank.pinnum)
print("Card Number =",Bank.cardnum)

