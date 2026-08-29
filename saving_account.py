from account import Account

class SavingAccount(Account):
    def __init__(self, account_holder, account_number, balance,interest_rate=5,minimum_balance=1000):
        super().__init__(account_holder, account_number, balance)
        self.interest_rate=interest_rate
        self.minimum_balance=minimum_balance

    def withdraw(self,amount):
        remaining_balance= self.get_balance() - amount
        if amount <= 0:
            print("Invalid amount")
            return
        if remaining_balance >= self.minimum_balance:
            super().withdraw(amount)

        else:
            print(f"Minimum balance after withdraw must be RS.{self.minimum_balance}") 


    # Abstract Method Implementation

    def calc_interest(self):
        interest= (self.get_balance() * self.interest_rate) / 100
        return interest

    # New Method

    def add_interest(self):
        interest=self.calc_interest()
        self._update_balance(interest)

        self.transaction_history.append({
            "type":"interest Added",
            "amount":interest,
            "balance":self.get_balance()
        })           

        print(f"Interest of Rs.{interest} added successfully.")

    def show_interest_details(self):
        print("\n===== Interest Details =====")
        print(f"Interest Rate    : {self.interest_rate}%")
        print(f"Current Balance  : Rs.{self.get_balance()}")
        print(f"Expected Interest: Rs.{self.calc_interest()}")