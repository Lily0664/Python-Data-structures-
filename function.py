def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price *(1 - discount_percent / 100)
    else:
        return price
    
# prompt user for input
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

final_price = calculate_discount(price, discount_percent)

if discount_percent >= 20:
    print(f"The final price after {discount_percent}% discount: {final_price}")

else:
    print(f"No discount applied. Final price: {final_price}")
