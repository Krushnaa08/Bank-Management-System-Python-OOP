from saving_account import SavingAccount
from current_account import CurrentAccount
from customer import Customer
from bank import Bank


print("=" * 50)
print("        BANK MANAGEMENT SYSTEM")
print("=" * 50)

# =====================================================
# Create Bank
# =====================================================

bank = Bank("National Bank of Pakistan")


# =====================================================
# Create Customers
# =====================================================

customer1 = Customer("Usman", "C001", "03001234567")
customer2 = Customer("Ahmed", "C002", "03111234567")


# =====================================================
# Create Accounts
# =====================================================

saving1 = SavingAccount("Usman", "PK001", 50000)
current1 = CurrentAccount("Usman", "PK002", 30000)

saving2 = SavingAccount("Ahmed", "PK003", 80000)
current2 = CurrentAccount("Ahmed", "PK004", 40000)


# =====================================================
# Perform Transactions
# =====================================================

print("\n===== Saving Account Transactions =====")

saving1.deposit(5000)
saving1.withdraw(10000)
saving1.add_interest()

saving2.deposit(10000)
saving2.withdraw(5000)
saving2.add_interest()


print("\n===== Current Account Transactions =====")

current1.deposit(3000)
current1.withdraw(5000)

current2.deposit(2000)
current2.withdraw(7000)


# =====================================================
# Add Accounts to Customers
# =====================================================

customer1.add_account(saving1)
customer1.add_account(current1)

customer2.add_account(saving2)
customer2.add_account(current2)


# =====================================================
# Add Customers to Bank
# =====================================================

bank.add_customer(customer1)
bank.add_customer(customer2)


# =====================================================
# Show Bank Information
# =====================================================

print("\n")
bank.show_bank_info()


# =====================================================
# Show All Customers
# =====================================================

print("\n===== All Customers =====")

bank.show_customers()


# =====================================================
# Search Customer
# =====================================================

print("\n===== Search Customer =====")

found = bank.find_customer("C001")

if found:
    print("Customer Found!\n")
    found.show_customer_info()

else:
    print("Customer not found!")


# =====================================================
# Show Customer Accounts
# =====================================================

print("\n===== Customer Accounts =====")

customer1.show_accounts()


# =====================================================
# Transaction History
# =====================================================

print("\n===== Saving Account History =====")
saving1.show_history()

print("\n===== Current Account History =====")
current1.show_history()


print("\n")
print("=" * 50)
print("      PROJECT EXECUTED SUCCESSFULLY")
print("=" * 50)