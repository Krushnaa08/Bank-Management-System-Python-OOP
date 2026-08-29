from abc import ABC,abstractmethod

class Account(ABC):
    def __init__(self,account_holder,account_number,balance):
        self.account_holder=account_holder
        self.account_number=account_number
        self.__balance=balance
        self.transaction_history=[]

    def _update_balance(self,change):
        """
        Update account balance.
        Positive value = Deposit
        Negative value = Withdraw
        """
        self.__balance += change

    def get_balance(self):
        return self.__balance
    def deposit(self,amount):
        if amount <= 0:
            print("Invalid amount")
            return
        self._update_balance(amount)

        self.transaction_history.append({
            "type":"Deposit",
            "amount":amount,
            "balance":self.get_balance()
        })

        print(f"RS. {amount} deposited successfully")

    def withdraw(self,amount):
        if amount <= 0:
            print("Invalid amount")
            return
        if amount > self.get_balance():
            print("Insufficent balance")
            return
        
        self._update_balance(-amount)
        self.transaction_history.append({
            "type":"Withdraw",
            "amount":amount,
            "balance":self.get_balance()
        })

        print(f"RS.{amount} withdraw successfully")

    def show_info(self):
        print("\n===== Account Info =====")
        print("Account Holder :", self.account_holder)
        print("Account Number :", self.account_number)
        print("Current Balance:", self.get_balance())    

    def show_history(self):
        if not self.transaction_history:
         print("No transaction found!")
         return

        print("\n===== Transaction History =====")
        for transaction in self.transaction_history:
            print(f"Type    : {transaction['type']}")
            print(f"Amount  : Rs.{transaction['amount']}")

            if "fee" in transaction:
                print(f"Fee     : Rs.{transaction['fee']}")

            print(f"Balance : Rs.{transaction['balance']}")
            print("-" * 30)        

    
    @abstractmethod
    def calc_interest(self):
        pass           




