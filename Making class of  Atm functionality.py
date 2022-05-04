class Atm:    #making Class
    
    def __init__(self):   # constructor
                            # Self= ItSelf Object  
        self.pin=""
        self.balance=0

        self.menu()

    def menu(self):   #making Function in Class is called Method
        UserInput=input('''                       How Can I help You


                     Please Select the Option
                          1. Enter 1 to Create PIN
                          2. Enter 2 to Amount Deposit 
                          3. Enter 3 to Withdrawal Amount
                          4. Enter 4 to Check Remaining Balance
                          5. Enter 5 to Exit
                                    ''')
        if UserInput=="1":
            self.CreatePin()  #call Method Name is CreatePin
        elif UserInput=="2":
            self.Deposit()    #call Method Name is Deposit
        elif UserInput=="3":
            self.withdrawal()   #call Method Name is withdrawal
        elif UserInput=="4":  
            self.checkBalance()  #call Method Name is check Balance
        else:
            print("Exit")



    def CreatePin(self):              #method
        self.pin=(input("Enter the PIN"))
        print("PIN Create Sucessfully")


    def Deposit(self):
        temp=(input("Enter the Pin"))
        if self.pin==temp:
            amount=int(input("Enter the Amount: "))
            self.balance=self.balance+amount
        else:
            print("Invalid PIN")

    def withdrawal(self):
        temp=input("Enter the Pin")
        if self.pin==temp:
            amount=int(input("Enter the Amount"))
            self.balance=self.balance-amount
        else:
            print("Invalid PIN")

    def checkBalance(self):
        temp=input("Enter the Pin")
        if self.pin==temp:
            print(self.balance)
        else:
            print("Invalid PIN")

            
