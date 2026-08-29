class Customer:
    def __init__(self,customer_name,customer_id,phone_number):
        self.customer_name=customer_name
        self.customer_id=customer_id
        self.phone_number=phone_number
        self.accounts=[]

    def add_account(self,account):
        self.accounts.append(account)

    def show_accounts(self):
        if not self.accounts:
            print("No account found!")
            return
        for account in self.accounts:
            account.show_info()

    def total_balance(self):
        total=0
        for account in self.accounts:
           balance= account.get_balance()
           total=total+balance
        return total
    def show_customer_info(self):
        print("\n===== Customer Info =====")
        print(f"Customer Name : {self.customer_name}")
        print(f"Customer ID   : {self.customer_id}")
        print(f"Phone Number  : {self.phone_number}")
        print(f"Total Accounts: {len(self.accounts)}")
        print(f"Total Balance : Rs.{self.total_balance()}")   

            
                    

