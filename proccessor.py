import paypalrestsdk

paypalrestsdk.configure({
  "mode": "sandbox",
  "client_id": "your_client_id",
  "client_secret": "your_client_secret"
})

price = 1.00

def check(transaction, expected):
    if not hasattr(transaction, "amount") or not hasattr(transaction.amount, "total"):
        return False

    try:
        total = float(transaction.amount.total[:-3])
    except ValueError:
        return False

    if total == float(expected) and transaction.state == "approved":
        return True
    else:
        return False

def get_transactions(count):
    transactions = paypalrestsdk.Transaction.all({"count": count})

    if transactions:
        return transactions
    else:
        return []

def process():
    transactions = get_transactions(5)

    if transactions:
        latest_transaction = transactions[0]

        if check(latest_transaction, price):
            print("Approved")
        else:
            print("Not approved")
    else:
        print("No transactions found.")

process()
