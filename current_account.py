from account import Account


class CurrentAccount(Account):

    def __init__(self, account_holder, account_number, balance, transaction_fee=50):
        super().__init__(account_holder, account_number, balance)
        self.transaction_fee = transaction_fee

    def withdraw(self, amount):

        if amount <= 0:
            print("Invalid amount")
            return

        total_amount = amount + self.transaction_fee

        if total_amount > self.get_balance():
            print("Insufficient balance")
            return

        # Balance update
        self._update_balance(-total_amount)

        # Save history
        self.transaction_history.append({
            "type": "Withdraw",
            "amount": amount,
            "fee": self.transaction_fee,
            "balance": self.get_balance()
        })

        print(f"Rs.{amount} withdrawn successfully.")
        print(f"Transaction Fee : Rs.{self.transaction_fee}")

    def calc_interest(self):
        return 0