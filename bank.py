from customer import Customer
class Bank:
    def __init__(self,bank_name):
        self.bank_name=bank_name
        self.customers=[]
    def add_customer(self,customer):
        self.customers.append(customer)

    def show_customers(self):
        if not self.customers:
            print("No customer found!")
            return
        for customer in self.customers:
            customer.show_customer_info()

    def find_customer(self,customer_id):
        for customer in self.customers:
          if  customer.customer_id==customer_id:
              return customer
        return None  
    def total_bank_balance(self):
        total=0
        for customer in self.customers:
            balance=customer.total_balance()
            total=total+balance
        return total
    def show_bank_info(self):
        print("\n===== Bank Information =====")
        print(f"Bank Name        : {self.bank_name}")
        print(f"Total Customers  : {len(self.customers)}")
        print(f"Total Balance    : Rs.{self.total_bank_balance()}")