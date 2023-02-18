class CreditCard:
    def __init__(self, customer_name, balance, bank, account, limit):
        self._customer_name = customer_name
        self._balance = balance
        self._account = account
        self._bank = bank
        self._limit = limit

    def get_customer_name(self):
        return self._customer_name

    def get_balance(self):
        return self._balance

    def get_bank(self):
        return self._bank

    def get_limit(self):
        return self._limit

    def make_payment(self, amount):
        if amount > self._balance:
            print("Transfer False. Your balance is not enough to pay")
        else:
            self._balance -= amount
        return self._balance

    def charge(self, amount):
        if self._balance + amount > self._limit:
            print("Transfer False. Your balance exceed limit")
        else:
            self._balance += amount
        return self._balance
    
    def __add__(self,other):
        return self._balance + other.get_balance()

    def __repr__(self):
        return 'name {} balance {}'.format(self._customer_name,self._balance)
        pass
card1 = CreditCard('Nam', 500, 'MB Bank', '11219279', 2000)
card2 = CreditCard('Minh', 1500, 'MB Bank', '11219272', 2000)
print(card1 + card2)

