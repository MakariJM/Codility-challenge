        #Key Notes
#Start year 2020
#Each transaction shows amount and date executed, If amount is negative (less than 0) then it was a card payment, but from 0 onwards it is an incoming transfer.
#Date format YYYY-MM-DD
#Theres a fee for having a card at 5 per month, deducted from account balance, unless there were at least 3 payment via card of atleast 100 within the month.
#Get the balance at the end of the year 2020.

#Array A of N intergers for transaction amounts
#Array D of N strings for transaction dates reaturning final ballance at the end of 2020
#Transaction number K (for K within the range [0..N-1]) was executedon date represented by D[k] for amount A[k]. 


# Dictionary to store transactions for each month
def final_balance(A, D):
    defaultdict = 0
    transactions = defaultdict(int)
    
    # Iterate through the transaction amounts and dates
    for amount, date in zip(A, D):
        year, month, _ = date.split('-')
        key = f"{year}-{month}" 
        
        # Update the transaction amount for the corresponding month. Deduct negative amount (expenditure),and Add positive amount (income) 
        if amount < 0:
            transactions[key] -= amount  
        else:
            transactions[key] += amount  
    
    # Variables for fee and balance
    fee = 0
    balance = 0
    
    # Final balance and fee based on the transactions
    for key in transactions:
        balance += transactions[key] 
        if transactions[key] < 0:
            fee += 5  
        if key != D[0][:7] and fee < 15:
            fee += 5 
    # Returning the final balance after deducting the fee   
    return balance - fee  

# Sample Test
print(final_balance([100, 100, -10, 20, 30], ["2020-01-01", "2020-02-01", "2009-12-11", "2020-02-05", "2020-02-08"]))

