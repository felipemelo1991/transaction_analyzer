data = [
  (749.17, "Investment Return"),
  (-11.54, "Utilities"),
  (-247.58, "Online Shopping"),
  (981.17, "Investment Return"),
  (-410.65, "Rent"),
  (310.60, "Rent"),
  (563.70, "Gift"),
  (220.79, "Salary"),
  (-49.85, "Car Maintenance"),
  (308.49, "Salary"),
  (-205.55, "Car Maintenance"),
  (870.64, "Salary"),
  (-881.51, "Utilities"),
  (518.14, "Salary"),
  (-264.66, "Groceries")
]

def print_transactions(transactions):
  for transaction in transactions:
    amount = transaction[0]
    statement = transaction[1]
    print(f"${amount} - {statement}")

def print_summary(transactions):
  deposits = [transaction[0] for transaction in transactions if transaction[0]>=0]
  total_deposited = sum(deposits)

  withdrawals = [transaction[0] for transaction in transactions if transaction[0]<0]
  total_withdrawn = sum(withdrawals)
  
  balance = total_deposited + total_withdrawn

  print(total_deposited)
  print(total_withdrawn)
  print(balance)

def analyze_transactions(transactions):
  transactions_list = [transaction[0] for transaction in transactions]
  transactions_list.sort()
  largest_withdrawal = transactions_list[0]
  largest_deposit = transactions_list[-1]

  deposits = [transaction[0] for transaction in transactions if transaction[0]>=0]
  total_deposited = sum(deposits)
  if len(deposits) > 0:
    average_deposited = total_deposited/len(deposits)
  else:
    average_deposited = 0

  withdrawals = [transaction[0] for transaction in transactions if transaction[0]<0]
  total_withdrawals = sum(withdrawals)
  if len(withdrawals) > 0:
    average_withdrawals = total_withdrawals/len(withdrawals)
  else:
    average_withdrawals = 0

  print(largest_withdrawal)
  print(largest_deposit) 
  print(average_deposited)
  print(average_withdrawals)

while True:
  print("""
    Select one option:
    1) Print
    2) Analyze
    3) Stop
    """)
  choice = input().lower()
  if choice == "print" or choice == "1":
    print_summary(data)
  elif choice == "analyze" or choice == "2":
    analyze_transactions(data)
  elif choice == "stop" or choice == "3":
    break
  else:
    print("Invalid choice")
