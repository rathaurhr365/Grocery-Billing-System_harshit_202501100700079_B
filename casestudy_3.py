from abc import ABC, abstractmethod

# Abstract Base Class
class Payment(ABC):
    def __init__(self, user_name):
        self.user_name = user_name
        self.original_amount = 0
        self.final_amount = 0

    @abstractmethod
    def pay(self, amount):
        pass

    def generate_receipt(self):
        print("\n----- PAYMENT RECEIPT -----")
        print(f"User: {self.user_name}")
        print(f"Original Amount: ₹{self.original_amount}")
        print(f"Final Amount Paid: ₹{self.final_amount}")
        print("---------------------------")


# Credit Card Payment
class CreditCardPayment(Payment):
    def pay(self, amount):
        self.original_amount = amount
        gateway_fee = 0.02 * amount
        gst = 0.18 * gateway_fee
        self.final_amount = amount + gateway_fee + gst
        print("Payment via Credit Card successful.")
        self.generate_receipt()


# UPI Payment
class UPIPayment(Payment):
    def pay(self, amount):
        self.original_amount = amount
        cashback = 50 if amount > 1000 else 0
        self.final_amount = amount - cashback
        print("Payment via UPI successful.")
        if cashback:
            print("Cashback applied: ₹50")
        self.generate_receipt()


# PayPal Payment
class PayPalPayment(Payment):
    def pay(self, amount):
        self.original_amount = amount
        fee = 0.03 * amount
        conversion_fee = 20
        self.final_amount = amount + fee + conversion_fee
        print("Payment via PayPal successful.")
        self.generate_receipt()


# Wallet Payment
class WalletPayment(Payment):
    def __init__(self, user_name, balance):
        super().__init__(user_name)
        self.balance = balance

    def pay(self, amount):
        self.original_amount = amount
        if amount > self.balance:
            print("Payment Failed: Insufficient wallet balance.")
        else:
            self.balance -= amount
            self.final_amount = amount
            print("Payment via Wallet successful.")
            print(f"Remaining Balance: ₹{self.balance}")
            self.generate_receipt()


# Polymorphism Function
def process_payment(payment, amount):
    payment.pay(amount)

name=input("enter the name: ")
cc = CreditCardPayment(name)
upi = UPIPayment(name)
paypal = PayPalPayment(name)
wallet = WalletPayment(name,50000)


shopping_amount = int(input("enter the shopping amount: "))
payment_method = input("Choose payment method (credit_card/upi/paypal/wallet): ").lower()

if payment_method == "credit_card":
    process_payment(cc, shopping_amount)
elif payment_method == "upi":
    process_payment(upi, shopping_amount)
elif payment_method == "paypal":
    process_payment(paypal, shopping_amount)
elif payment_method == "wallet":
    process_payment(wallet, shopping_amount)
else:
    print("Invalid payment method.")
