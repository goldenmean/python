from collections import defaultdict
import heapq

def minTransactions(transactions):
    # Create a balance sheet using defaultdict
    balance = defaultdict(int)
    
    # Calculate net balance for each person
    for payer, receiver, amount in transactions:
        # Split amount in half since it's the total spent
        split_amount = amount / 2
        balance[payer] += split_amount
        balance[receiver] -= split_amount
    
    # Create lists of people who need to pay (debtors) and receive (creditors)
    debtors = []
    creditors = []
    print(balance)
    # Separate people into debtors and creditors based on their balance
    for person, amount in balance.items():
        if amount < 0:
            #both debtors and creditors are max heap so that we can pop the max value
            # debtors is built using amount which is negative for debtors so we get max heap automatically
            # creditors is built using -amount  (amount is positive) so -amount gives max heap
            heapq.heappush(debtors, (amount, person))
        elif amount > 0:
            heapq.heappush(creditors, (-amount, person))
    
    transaction_count = 0
    
    # Process all debts
    while debtors and creditors:
        #get the largest debt and credit amounts from the max heap
        debt, debtor = heapq.heappop(debtors)
        credit, creditor = heapq.heappop(creditors)
        
        print(debt, debtor, credit, creditor)
        debt = abs(debt)
        credit = abs(credit)
        
        transaction_count += 1
        
        # If debt is larger than credit
        if debt > credit:
            # debi - credit is the remaining debt after the transaction, debtor has to pay this
            debt = debt - credit
            heapq.heappush(debtors, (-(debt - credit), debtor))
        # If credit is larger than debt
        elif credit > debt:
            # credit - debt is the remaining credit after the transaction, creditor gets this
            credit = credit - debt
            heapq.heappush(creditors, (-(credit - debt), creditor))
        # if debt == credit then both are settled
    return transaction_count

# Test cases
def test_min_transactions():
    #print(minTransactions([[0, 1, 20]]))  # Should return 1
    #print(minTransactions([[0, 1, 5], [0, 2, 10], [2, 1, 15]]))  # Should return 2
    print(minTransactions([[0, 1, 5], [0, 2, 10], [2, 1, 15], [1, 2, 20]]))  

if __name__ == "__main__":
    test_min_transactions()