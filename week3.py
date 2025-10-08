# Discount percent calculations using arguments!
def calculate_discount(price, discount_percentage):
    if discount_percentage >= 20:
        discount = price * (1 + discount_percentage / 100)
        final_price = price - discount
        return final_price

    else:
        return price


#Trying user inputs(prompt)
price = int(input("Enter price: "))
discount_percentage = int(input("Enter discount percentage: "))

#Calculate the final price
final_price = calculate_discount(price, discount_percentage)

#Display the result
if discount_percentage >= 20:
    print(f"The final price after a {discount_percentage}% discount is: {final_price:.2f}")
else:
    print(f"The final price is: {final_price:.2f}")

