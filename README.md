n=int(input("enter the number of items you want to buy: "))
if n>5:n=5
real_total=0
price={"milk":50,"bread":10,"egg":5,"sugar":35,"oil":50}
for i in range(n):
    item=input("you can buy milk,bread,egg,sugar,oil: ")
    number=int(input("enter the quantity: "))
    if item in price:
        total=price[item]*number
        real_total+=total
        print("the total price of",item,"is",total)
    else:
        print("item not available")
print("the total price of your shopping is ",real_total)
if real_total>100:
    print("you got 10% discount and you save :",real_total*0.1)
    print("the total price after discount is ",real_total*0.9)
else:
    print("you got no discount because your total amount is less than 100")
    print("the total price is ",real_total)
# Grocery-Billing-System_harshit_202501100700079_B
