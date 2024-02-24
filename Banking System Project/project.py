#Banking System

class RBI:
    def __init__(self):
        self.Account = 10000
        self.Balance = 2500000

class SBI(RBI):
    def __init__(self):
        self.Account1=8000
        self.Balance1=2000000
        super().__init__()

class TamilNadu(SBI):
        
    def __init__(self):
        self.Account2=6500
        self.Balance2=1600000
        super().__init__()

class ChennaiBank(TamilNadu):
    def __init__(self):
        self.Account3=5000
        self.Balance3=1300000
        super().__init__() 

    def deposit(self):
        self.deposit=int(input("Enter amount to deposited:"))
        if self.deposit >0:
            self.Balance3=(self.Balance3+self.deposit)
            self.Balance2=(self.Balance2+self.Balance3)
            self.Balance1=(self.Balance1+self.Balance3)
            self.Balance=(self.Balance+self.Balance3)
            print("Deposit Successful")
        else:
            print("Error: Invalid deposit amount")


    def withdraw(self):
        self.withdraw=int(input("Enter amount to be withdraw:"))
        if self.Balance3>=self.withdraw:
            self.Balance3=(self.Balance3-self.deposit)
            self.Balance2=(self.Balance2-self.Balance3)
            self.Balance1=(self.Balance1-self.Balance3)
            self.Balance=(self.Balance-self.Balance3)
            print("widthraw Successful")
        else:
            print("Insufficient Balance")    

    
    def open_account(self):
         self.Account3=(self.Account3+1)
         self.Account2=(self.Account2+1)
         self.Account1=(self.Account1+1)
         self.Account=(self.Account+1)
        
    def close_account(self):
        self.Account3=(self.Account3-1)
        self.Account2=(self.Account2-1)
        self.Account1=(self.Account1-1)
        self.Account=(self.Account-1)




B=open(r"C:\Users\admin\Desktop\Banking System Project\Project.txt","r")
C=B.readlines()
B.close()

if C:
   A=eval(C[-1].replace("\n",""))
   x=ChennaiBank()
   x.Account=A['ReserveBank'][0]
   x.Balance =A['ReserveBank'][1]
   x.Account1=A['StateBank'][0]
   x.Balance1=A['StateBank'][1]
   x.Account2=A['TamilNadu'][0]
   x.Balance2=A['TamilNadu'][1]
   x.Account3=A['ChennaiBank'][0]
   x.Balance3=A['ChennaiBank'][1] 

else:
    x=ChennaiBank()
x.deposit()
print(x.Balance3,x.Balance2)
x.withdraw()
print(x.Balance3)
x.open_account()
print(x.Account3,x.Account2,x.Account1,x.Account)
x.close_account()
print(x.Account3,x.Account2,x.Account1,x.Account)



A={'ReserveBank':[],'StateBank':[],'TamilNadu':[],'ChennaiBank':[]}
A['ReserveBank'].extend([x.Account, x.Balance])
A['StateBank'].extend([x.Account1, x.Balance1])
A['TamilNadu'].extend([x.Account2, x.Balance2])
A['ChennaiBank'].extend([x.Account3, x.Balance3])


B=open(r"C:\Users\admin\Desktop\Banking System Project\Project.txt","a+")
B.write("{0}\n".format(A))
B.close()