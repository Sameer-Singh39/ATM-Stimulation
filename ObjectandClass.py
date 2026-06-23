class Atm:
    def __init__(self): #
        self.pin=''
        self.balance=0
        self.menu()
        # print("Mai to execute ho gaya")
    def menu(self):
        user_input=input("""
        Hi how can I help you?
        1.Press 1 to create pin
        2.Press 2 to change pin
        3.Press 3 to check balance
        4.Press 4 to withdraw
        5.Anything else to exit
        """) 
        
        if user_input=='1':
         #create pin
         self.create_pin()
        elif user_input=='2':
        #change pin
         self.change_pin()
        elif user_input=='3':
        #check balance
         self.check_balance()
         
        elif user_input=='4':
        #withdraw
         self.withdraw()
         
        else:
            exit() 
            
    def create_pin(self):
        user_pin= input("Enter your pin : ")
        self.pin=user_pin
        user_balance=int(input("Enter your balance : "))
        self.balance=user_balance
            
        print("Pin created successfully")
        self.menu()
        
    def change_pin(self):
        old_pin=input("Enter your old pin :")
        if old_pin==self.pin:
         new_pin=input("enter your new pin : ") 
         self.pin=new_pin
         print("pin change successfully")
         self.menu()
        else:
            print("Your old pin is not correct. You cannot change your pin please remember your old.") 
            self.menu()
       
    def check_balance(self):
        pin=input("Enter your pin : ")
        if pin==self.pin:
            print("Your balance is : ",self.balance)
        else:
            print("Please enter a valid pin ")  
            
    def withdraw(self):
        user_pin=input("Enter your pin: ")
        if user_pin==self.pin:
         amount=int(input("Enter your amount : "))
         if amount <=self.balance:
             self.balance=self.balance-amount
             print("Withdraw successfully your balance  is : ",self.balance)
         else:
             print("Yoy have not enough money")    
        else:
            print("Please enter a valid pin ") 
        self.menu()    
            
                   
               
               
                       
        
obj=Atm()
# print(type(obj)) 
# obj.balance  